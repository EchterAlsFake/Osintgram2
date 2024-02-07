# IMPORTANT:
#### This project is currently unstable and unmaintained. There will be an update in the future!

Upate:
I'll shift from Instagrapi to Instaloader. Please wait some more days...


# Osintgram 2🔎📸

##### A *OSINT* Tool for anonymous advanced information gathering
##### Based on the great [Osintgram](https://github.com/Datalux/Osintgram) from Datalux

# Table of contents

- [Instagram ToS](#instagram-tos)
- [Features](#features)
- [In case you get Blocked](#block)
- [Installation](#installation)
- [Building from Source](#building-from-source)
- [Credits](#credits)
- [License](#license)

# Instagram ToS
 ```
!!! PROHIBITED BY INSTAGRAM !!!

INSTAGRAM PROHIBITS USING THEIR PRIVATE API
INSTAGRAM PROHOBITS USING AUTOMATED TOOLS
```

# Features

- Everything from the original Osintgram by Datalux*
- automatic download of all media from specific hashtag
- search for hashtags with a query
- download media from hashtags
- No Login required
- Stable API
- Intuitive folder structure system
- Automatic login through session ID

**except hashtags, tagged, commented, wcommented

# Prevent Instagram Account bans

Instagram has a lot of limitations since the Osintgram by Datalux.

Try the following if you get errors, related to the API, login or loading objects:

- Change IP (NO VPN, restart router instead)
- Change device fingerprint
- Change User Agent
- Login with Browser, and use the Session ID from developer settings
- Use different Account
- Add 2FA to your account
- Change Delay of API actions

While developing, I am using over 15 different Accounts and over 10 different IP addresses.
<br>It's hard, but possible!


# Installation

### Current version: 1.2
### Download from [Releases](https://github.com/EchterAlsFake/Osintgram2/releases)

# Building from Source
### Supported distros:

- Termux (Android)  ! NO root access required
- Kali Linux / Nethunter
- Ubuntu
- Parrot OS
- Arch Linux
- OpenSUSE
- Fedora

The build script will automatically compile the application with Pyinstaller.
<br>This gives you the newest function, even before they are released! (Can lead to errors)

Wget:
``` 
wget -O - "https://raw.githubusercontent.com/EchterAlsFake/Osintgram2/master/install.sh" | bash
``` 
Curl:
``` 
curl -s "https://raw.githubusercontent.com/EchterAlsFake/Osintgram2/master/install.sh" | bash
``` 

ChatGPT automatically generated the build script.
<br>If you find errors, feel free to report them :) 


# Credits

#### API: [instagrapi](https://github.com/subzeroid/instagrapi)
#### Idea: [Original Osintgram](https://github.com/datalux/Osintgram)
#### GUI : [Qt](https://qt.io)
# License

Licensed under the GPLv3 License.
<br>Copyright (C) 2023 EchterAlsFake | Johannes Habel
