# isclaudex2discordbot

Claude 사용량이 2배인지 알려주는 Discord 봇.

- **2x 활성** → 봇 상태: 🟢 Online, `"2x 종료까지 2h 07m"`
- **2x 비활성** → 봇 상태: 🔴 Do Not Disturb, `"다음 2x까지 1h 30m"`

## Setup

```bash
# 1. Clone
git clone https://github.com/your-username/isclaudex2discordbot.git
cd isclaudex2discordbot

# 2. Install
uv venv && uv pip install -e .

# 3. Run
DISCORD_BOT_TOKEN=your_token_here uv run python bot.py
```
