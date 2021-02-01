# Telegram Torrent Leecher 🔥🤖
Working example at [Universal Fast Mirror](https://t.me/Universal_Fast_Mirror)

A Telegram Torrent (and youtube-dl) Leecher based on [Pyrogram](https://github.com/pyrogram/pyrogram)

# Benefits :-
    ✓ Telegram File mirrorring to cloud along with its unzipping, unrar and untar
    ✓ Unzip
    ✓ Unrar
    ✓ Untar
    ✓ Custom file name
    ✓ Custom commands
    ✓ You can also upload files downloaded from /ytdl command
    ✓ You can also deploy this on your VPS
    ✓ Option to select either video will be uploaded as document or streamable
    ✓ Added support for youtube playlist 😐
    ✓ Renaming of Telegram files support added. 😐
    
# TO-DO
-   [ ] Adding mp3 files support while playlist downloading.
-   [ ] Password support while Unarchiving the files.
-   [ ] Selection of required files during leeching the big files using aria(/leech command)

### Credit goes to SpEcHiDe for his Publicleech repo.

## installing...

## Process to run this BOT on VPS

- Clone this repo:
```
git clone https://github.com/Technical-Jigar/Torrent-Leech-Bot
cd Torrent-Leech-Bot
```

- Install requirements
For Debian based distros
```
sudo apt install python3

sudo snap install docker
```
Install Docker by following the [official docker docs](https://docs.docker.com/engine/install/debian/)

## Setting up config file
```
cp bot/g_config.py bot/config.py
```
After this step you will see a new file named ```config.py``` in bot directory.

Follow and fill all the required variables that were already filled in the sample config file, but with your details. And you can also fill all other variables according to your need and all those are explained below.

## Deploying

- Start docker daemon (skip if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t torrentleech-gdrive
```
- Run the image:
```
sudo docker run torrentleech-gdrive
```

### The Legacy Way
Simply clone the repository and run the main file:

```sh
git clone https://github.com/gautamajay52/TorrentLeech-Gdrive
cd TorrentLeech-Gdrive
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py appropriately>
python3 -m tobrot
```

### an example config.py 👇
```py
from bot.sample_config import Config

class Config(Config):
  TG_BOT_TOKEN = ""
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  AUTH_CHANNEL = [-1001234567890]
```

### Variable Explanations

##### Mandatory Variables

* `TG_BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

* `APP_ID`
* `API_HASH`: Get these two values from [my.telegram.org/apps](https://my.telegram.org/apps).
  * N.B.: if Telegram is blocked by your ISP, try our [Telegram bot](https://telegram.dog/UseTGXBot) to get the IDs.

* `AUTH_CHANNEL`: Create a Super Group in Telegram, add `@GoogleIMGBot` to the group, and send /id in the chat, to get this value.

* `DESTINATION_FOLDER`: Name of your folder in ur respective drive where you want to upload the files using the bot.

* `OWNER_ID`: ID of the bot owner, He/she can be abled to access bot in bot only mode too(private mode).

## FAQ

##### Optional Configuration Variables

* `DOWNLOAD_LOCATION`

* `MAX_FILE_SIZE`

* `TG_MAX_FILE_SIZE`

* `FREE_USER_MAX_FILE_SIZE`

* `MAX_TG_SPLIT_FILE_SIZE`

* `CHUNK_SIZE`

* `MAX_MESSAGE_LENGTH`

* `PROCESS_MAX_TIMEOUT`

* `ARIA_TWO_STARTED_PORT`

* `EDIT_SLEEP_TIME_OUT`

* `MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START`

* `FINISHED_PROGRESS_STR`

* `UN_FINISHED_PROGRESS_STR`

* `TG_OFFENSIVE_API`

* `CUSTOM_FILE_NAME`

* `LEECH_COMMAND`

* `YTDL_COMMAND`

* `GLEECH_COMMAND`

* `TELEGRAM_LEECH_COMMAND_G`

* `PYTDL_COMMAND_G`

* `UPLOAD_COMMAND`

* `SAVE_THUMBNAIL`

* `CLEAR_THUMBNAIL`

* `UPLOAD_AS_DOC`: Takes two option True or False. If True file will be uploaded as document. This is for people who wants video files as document instead of streamable.

## Available Commands
       
* `/log`: This will send you a txt file of the logs.

* `/ytdl`: This command should be used as reply to a [supported link](https://ytdl-org.github.io/youtube-dl/supportedsites.html)

* `/pytdl`: This command will download videos from youtube playlist link and will upload to telegram.


* `/leech`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files, if there is more than one file, in the specified torrent]

* `/leech archive`: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]

* `/leech unzip`: This will unzip the .zip file and dupload to telegram.

* `/leech unrar`: This will unrar the .rar file and dupload to telegram.

* `/leech untar`: This will untar the .tar file and upload to telegram.

* `/rename`: To rename the telegram files.


* ~Only work with direct link and youtube link for now~It is like u can add custom name as prefix of the original file name.
Like if your file name is `gk.txt` uploaded will be what u add in `CUSTOM_FILE_NAME` + `gk.txt`

~Only works with direct link/youtube link.No magnet or torrent.~

And also added custom name like...

You have to pass link as 
`www.download.me/gk.txt | new.txt`

the file will be uploaded as `new.txt`.


## How to Use?

* send any one of the available command, as a reply to a valid link/magnet/torrent. 👊


## Credits, and Thanks to
* [SpEcHiDe](https://github.com/SpEcHiDe/PublicLeech) for his wonderful code😚
* [Dan Tès](https://telegram.dog/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)
* [Robots](https://telegram.dog/Robots) for their [@UploadBot](https://telegram.dog/UploadBot)
* [@AjeeshNair](https://telegram.dog/AjeeshNait) for his [torrent.ajee.sh](https://torrent.ajee.sh)
* [![CopyLeft](https://telegra.ph/file/b514ed14d994557a724cb.jpg)](https://telegra.ph/file/fab1017e21c42a5c1e613.mp4 "CopyLeft Credit Video")
