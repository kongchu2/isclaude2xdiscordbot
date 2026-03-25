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

## Discord Bot 생성

1. [Discord Developer Portal](https://discord.com/developers/applications)에서 Application 생성
2. Bot 탭에서 토큰 발급
3. OAuth2 → URL Generator에서 `bot` scope 선택 후 서버에 초대

별도 권한은 필요하지 않습니다.

## API

[isclaude2x.com/json](https://isclaude2x.com/json) 엔드포인트를 60초마다 폴링합니다.
