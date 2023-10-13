# Osintgram 2🔎📸

##### A *OSINT* Tool for anonymous advanced information gathering
##### Based on the great [Osintgram](https://github.com/Datalux/Osintgram) from Datalux
# Information:

This project is currently not at my highest priority.
<br>Some features may not work correctly and there might be some logical flaws.

I can fix it in approximately 1-2 weeks :) 
<br>Thanks for your patience

(I am working on a way to load the media objects with a delay, so that you don't get timed out.)

# Table of contents

- [Instagram ToS](#instagram-tos)
- [Features](#features)
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
- No Login required
- Stable API
- Intuitive folder structure system
- Automatic login through session ID

**except hashtags, tagged, commented, wcommented
# Installation

### Current version: 1.1
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
