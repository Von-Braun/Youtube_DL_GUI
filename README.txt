What's Included
---------------

NAME------------Description--------------------------------------------------
README.TXT     #This contains all the documentation and info for this program
updater.py     #this will update youtube-dl
youtube-gui.pyw #this is the main program that you will run


Required
--------

The following modules must be installed for youtube-gui to fully function:

youtube-dl
ffmpeg
python


Installation(in this order)
---------------------------
==python==
goto https://www.python.org/download/
click download python 2.x.x
run the downloaded installer

==youtube-dl==
type "pip install youtube_dl" into the cmd prompt

==ffmpeg==
[32-bit]
goto http://ffmpeg.zeranoe.com/builds and download the 32-bit static installer
[64-bit]
goto http://ffmpeg.zeranoe.com/builds and download the 64-bit static installer

copy the directory ffmpeg was installed to
goto Control Panel\System and Security\System\advanced system settings
click the advanced tab and goto environmental variables
edit path in systems variables and add ";<ffmpeg/bin directory>"
e.g. ";E:\ffmpeg-20151215-git-65877ab-win64-static\bin
edit PATHTEXT in systems variables and add ";.PY;.PYW"


How to use
----------
If this is the first time, please run youtube-dl.pyw.
That will generate config.ini(stores settings) and the downloads folder(where
your downloads will be stored).

You will first see three buttons a checkbox,dropbox & entry box:

[Paste & Download]
This will pull a url from the clipboard and download the file. It will be
placed in the selected directory.

[Open Folder]
This will open the selected directory.

[dropbox]
Enter a folder name(or select from the dropdown menu) to select the folder
to place downloads in(all folders are in the downloads folder). If a folder
does not exist it will be created.

[Download Playlist]
If this is checked youtube-dl will attempt to download the playlist in the
url.

[Entry Box]
This show the last downloaded url.

[Settings]
This allows you to configure how the file should be downloaded. More is
explained in the Settings menu section.


Settings Menu
-------------
When opened you will see: 
Subtitles
Formats
Video Format
Quality
Arguments
Audio Format
Temporary Directory
Directory
Clear
And lots of keep checkboxes

[clear]
Erases all data from the entry boxes(not including directory) and checkboxes

[Subtitles]
enter or select the two-charecter code of the requested launguage subtitles

[Formats]
options:
-f bestaudio #get the highest quality audio only/no video
-f bestvideo #same as bestaudio but with video
-f worst #get worst video and audio quality
-f best #get worst video and audio quality

[Video Format]
Select the files output format

[Quality]
This allows you to specifically select the videos quality. Your file will FAIL
to download if the selected quality is not available.

[Arguments]
Any extra arguments for youtube-dl seperated by spaces. Some examples are
included.

[Audio Formats]
Only downloads audio and outputs to this format

[Temporary Directory]
allows you to select a temporary directory to place the downloaded file.

[Directory]
The current directory of the downloads folder.


Bug Reporting & contact info
----------------------------
please contact me at gerardkoufax@gmail.com


------------------------------------------------------------------------------
Copyright (C) 1988-2155 Altos Computer Systems & Gerard Koufax.

Youtube-GUI ver 6.6.6
All rights reserved. This program or any portion thereof may not be 
reproduced or used in any manner whatsoever without the express written 
permission of the programmer.

Youtube-GUI is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.

Produced in the United States of America.