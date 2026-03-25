import os
from pathlib import Path
import aiohttp
import discord
from discord.ext import tasks

# Load .env file
_env_path = Path(__file__).parent / ".env"
if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
API_URL = "https://isclaude2x.com/json"
POLL_INTERVAL_SECONDS = 60


def _fmt_hm(total_seconds: int) -> str:
    h, remainder = divmod(max(total_seconds, 0), 3600)
    m = remainder // 60
    if h > 0:
        return f"{h}h {m}m"
    return f"{m}m"


class IsClaudeX2Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self._session: aiohttp.ClientSession | None = None

    async def setup_hook(self):
        self._session = aiohttp.ClientSession()
        self.update_status.start()

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def fetch_api(self) -> dict | None:
        try:
            async with self._session.get(API_URL, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status == 200:
                    return await resp.json()
        except Exception as e:
            print(f"API fetch error: {e}")
        return None

    @tasks.loop(seconds=POLL_INTERVAL_SECONDS)
    async def update_status(self):
        data = await self.fetch_api()
        if data is None:
            return

        is_2x = data.get("is2x", False)

        if is_2x:
            seconds = data.get("2xWindowExpiresInSeconds", 0)
            status = discord.Status.online
            activity_text = f"it's 2x! 2x ends in {_fmt_hm(seconds)}"
        else:
            seconds = data.get("standardWindowExpiresInSeconds", 0)
            status = discord.Status.dnd
            activity_text = f"Next 2x in {_fmt_hm(seconds)}"

        activity = discord.Activity(type=discord.ActivityType.watching, name=activity_text)
        await self.change_presence(status=status, activity=activity)

    @update_status.before_loop
    async def before_update_status(self):
        await self.wait_until_ready()

    async def close(self):
        self.update_status.cancel()
        if self._session:
            await self._session.close()
        await super().close()


if __name__ == "__main__":
    bot = IsClaudeX2Bot()
    bot.run(DISCORD_BOT_TOKEN)
