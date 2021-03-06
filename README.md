What This Program Does
----------------------
This is a GUI for the command line program [**Youtube-DL.**](https://rg3.github.io/youtube-dl/)

**Example Images**

* https://s12.postimg.org/ymfhv8r3x/look11.png

* https://s12.postimg.org/vr2eodn3x/look10.png

* https://s12.postimg.org/r2met6xx9/look5.png

* https://s12.postimg.org/p9ji4vcql/look3.png

* https://s12.postimg.org/4ryjt80n1/look9.png

What's Included
---------------

NAME------------Description--------------------------------------------------

README.TXT:     this contains all the documentation and info for this program

updater.py:     this will update youtube-dl

youtube-gui.pyw:  this is the main program that you will run


Required
--------

The following must be installed for youtube-gui to fully function:

* youtube-dl

* ffmpeg

* python


Installation(in this order)
---------------------------

* python

  * go to https://www.python.org/download/

  * click download python 2.x.x

  * run the downloaded installer

* youtube-dl

  * type "pip install youtube_dl" into the cmd prompt

* ffmpeg

1. 
  * [32-bit]: go to http://ffmpeg.zeranoe.com/builds and download the 32-bit static installer

  * [64-bit]: go to http://ffmpeg.zeranoe.com/builds and download the 64-bit static installer

2. copy the directory ffmpeg was installed to

3. go to Control Panel\System and Security\System\advanced system settings

4. click the advanced tab and goto environmental variables

5. edit path in systems variables and add ";<ffmpeg/bin directory>"

6. e.g. ";E:\ffmpeg-20151215-git-65877ab-win64-static\bin

7. edit PATHTEXT in systems variables and add ";.PY;.PYW"


How to use
----------

If this is the first time, please run youtube-dl.pyw.

That will generate config.ini(stores settings) and the downloads folder(where your downloads will be stored).

You will first see three buttons, a checkbox,dropbox & entry box:

**[Paste & Download]**

  * This will pull a url from the clipboard and download the file. It will be  placed in the selected directory.

**[Open Folder]**

  * This will open the selected directory.

**[dropbox]**

  * Enter a folder name(or select from the dropdown menu) to select the folder to place downloads in(all folders are in the downloads folder). If a folder does not exist it will be created.

**[Download Playlist]**

  * If this is checked youtube-dl will attempt to download the playlist in the url.

**[Entry Box]**

  * This shows the last downloaded url.

**[Settings]**

  * This allows you to configure how the file should be downloaded. More is explained in the Settings menu section.


Settings Menu
-------------

When opened you will see: 

* Subtitles

* Formats

* Video Format

* Quality

* Arguments

* Audio Format

* Temporary Directory

* Directory

* Clear

* And lots of keep checkboxes

**[clear]**

  * Erases all data from the entry boxes(not including directory) and checkboxes

**[Subtitles]**

  * Enter or select the two-charecter code of the requested launguage subtitles

**[Formats]**

options:

* -f bestaudio #get the highest quality audio only/no video

* -f bestvideo #same as bestaudio but with video

* -f worst #get worst video and audio quality

* -f best #get worst video and audio quality

**[Video Format]**

  * Select the files output format

**[Quality]**

  * This allows you to specifically select the videos quality. Your file will FAIL to download if the selected quality is not available.

**[Arguments]**

  * Any extra arguments for youtube-dl seperated by spaces. Some examples are included.

**[Audio Formats]**

  * Only downloads audio and outputs to this format

**[Temporary Directory]**

  * Allows you to select a temporary directory to place the downloaded file.

**[Directory]**

  * The current directory of the downloads folder.


Bug Reporting & contact info
----------------------------
please contact me at gerardkoufax@gmail.com
