# isclaude2xdiscordbot

A Discord bot that shows whether Claude usage is currently 2x.

- **2x active** → Bot status: 🟢 Online, `"2x ends in 2h 07m"`
- **2x inactive** → Bot status: 🔴 Do Not Disturb, `"Next 2x in 1h 30m"`

## Add to your server

[Invite the bot](https://discord.com/oauth2/authorize?client_id=1486301903825666159&permissions=0&integration_type=0&scope=bot)

## Self-hosting

```bash
git clone https://github.com/kongchu2/isclaude2xdiscordbot.git
cd isclaude2xdiscordbot
uv venv && uv pip install -e .
DISCORD_BOT_TOKEN=your_token_here uv run python bot.py
```

## Credits

Powered by [isclaude2x.com](https://isclaude2x.com/) by [@mehulmpt](https://github.com/mehulmpt/isclaude2x).
