# Bot To Play Music In Telegram Voice Chats

## Note

Neither This, or PyTgCalls Are Fully Stable.

## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nxthsara/pyrovoicechatsheroku/)


## Credits

- [Roj](https://github.com/rojserbest): Main Developer
- [Marvin](https://github.com/BlackStoneReborn): Bug Reporter
- [Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX): PyTgCalls
