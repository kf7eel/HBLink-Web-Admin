# HBLink-Web-Admin
A web based administration tool for HBLink written in Python 3.

## Features:

  * Add/Edit/Delete Bridges
  * Add/Edit/Delete Bridge rules
  * Add/Edit/Delete Master, Peer, Openbridge, and XLX Peer connections



<img src="web-admin-1.png?raw=true">



<img src="web-admin-2.png?raw=true">



<img src="web-admin-3.png?raw=true">



## Currently in developement:
* _*Easy import from current configurations*_
* User authentication
* Talkgroup list management
* Ability to exclude single talkgroup from list when adding talkgroup triggers to rule.

# 4-28-2020 - # Warnings...

This tool is in ALPHA testing, use at your own risk.

Things to remember:
* ALWAYS, ALWAYS, ALWAYS make a backup of rules.py and hblink,cfg prior to using the web interface. Once you start using the interface, it will completely change the layout of both files.
* DO NOT run this on a publicly accessable port as there is no user authentication (yet).

Keep a backup of your original rules.py and hblink.cfg in the event that this tool doesn't work. It is still in developement, and I am a novice at Python, so there are a lot of bugs :).

Also create a backup of the modified rules.py, rules_web.py, and functions.py. There were a couple instances where these files got erased during testing, I think that has been fixed though.

Openbridge configurations must have "both_slots" in order to show up in web interface.

This tool is still evolving, there will be bug fixes, etc. in the future.

# Setup

1. Download from GitHub.

`git clone https://github.com/kf7eel/HBLink-Web-Admin.git
`

2. Copy config.SAMPLE to config.py

` cp config.SAMPLE config.py
`

3. Edit config to your setup. Change "hblink_loc" to the directory of your hblink configuration files. Other variables are optional.

4. Create a backup of HBLink rules.py and hblink.cfg.

` cd /folder/where/hblink/is/ ; 
cp hblink.cfg hblink.pre_web.bak ; 
cp rules.py rules.pre_web.bak
`

5. Edit rules.py.

Add `from functions import *` and `from rules_web import *
` at the top of rules.py.

6. Select `BRIDGES = {...everything in between brackets...}` and copy it to a new file called _rules_web.py_. Save rules_web.py in the same folder as rules.py. 

7. In rules.py, change `BRIDGES = {...` to `old_BRIDGES = {...everything in between brackets...}`

8. Create a blank file for custom functions called functions.py. Must be in the same folder as rules.py.

`touch functions.py
`

9. Go back to the folder containing HBLink Web Admin and change all files in cgi-bin to executable.

`chmod +x cgi-bin/*
`

10. Go back to the folder where HBLink web admin is and start the Pytohn web server. Remember, there is presently no user authentication, so do not start server on publicly accessible port.

`python3.7 -m http.server --cgi 8090
`

11. In your web browser, got to the ip address of the HBLink server on port 8090 or what ever you set it to in the command above.

12. Enjoy!
