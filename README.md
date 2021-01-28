# Vinyl Music Player
This is a simple music player made with Python and Tkinter, code is simple and easy to understand.

NOTE - This application is intended to be used either for personal use or for educational purposes, use in any any other field is at your own risk even though the Licence allows
usage for such purposes.

NOTE - This application has been tested with successful results with the Windows operating system, it has been test with unsuccessful results on Mac OS ans has not been tested on Linux, hence I only expect the application to run on Windows and not any other OS

NOTE - Any executable file in this repository may be blocked by your OS or by your browser or some other security software, these files if downloaded and blocked may cause them to go corrupt and not work properly, to get around this, I recommend that you download the whole repository at once and then use the executable files. I also give confirmation that no file in this repository is capable of doing harm or good to you/your computer software/your computer hardware.

# Profile views -
<img src="https://camo.githubusercontent.com/69977ae9b6a50d8ed4c1043533cb99a87a1ba443024fd9c622abf7b0b18aa545/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f73686172616e2d707974686f6e2f636f756e742e737667" />
INVITE YOUR FRIENDS TO VIEW MY PROFILE AND REPOSITORIES OR I TAKE YOUR DOG

# Usage -

## Steps to use - 
<br> 

1 - Download and unzip the repository.


2 - Open your terminal or command prompt and execute the following commands.

`pip install pygame`

`pip install tinytag`

`pip install pillow`

3 - Run `Vinyl.py`.

4 - After the music player screen appears it should look something like this...


![Image 1](player.jpg)

5 - On the Music Player window click `File` and then click `Open`.

6 - A file-dialog should come up, choose a `.mp3` `.wav` `.ogg` `.xm` or `.mod` file

7 - The song name should come up on the listbox, click the play button.

8 - Done!!! Your song should be playing now.

# Features

1 - Light and dark mode - Click modes and choose Light or Dark

2 - Shows picture of artist - If a file called `cover.jpg` is available in the same folder as your song it will display that image after opening the song, intended to display a picture of the artist who made the songs in the folder. If `cover.jpg` is not available then it will display this...

![Image 1](Vinyl%20Music%20Player%20icon.png)

3 - Volume slider - Allows you to change the volume of the song being played. (Note that the volume changed in the app is relative to system volume, so if system volume is 50% and app volume is 100% the volume of the sound being played is 100% of 50)

# Installer
The file `Vinyl Music Player x64 Installer.exe` is a distributable installer for the app. Can be used just like a regular app installer.

# Executable version
Goto [this link](https://drive.google.com/file/d/19aDlEZ0dXFmlA1n2pQvHug5h86BjO2o-/view?usp=sharing), make sure third party cookies and all cookies are enabled are enabled for google drive and download it, in build\exe.win-amd64-3.9 run Vinyl.exe

# Build to executable
Steps to convert to executable-
1- Open Cmd and type `pip install cx_freeze`

2- cd to the downloaded folder and run `python build.py build` for microsoft store python installations and `py build.py build` for installations downloaded from python.org

3- Copy the images, namely `Vinyl.jpg` `player.jpg` `PauseButton.png` `PlayButton.png` and put it in build\exe.win-amd64-3.9

4- Run Vinyl.exe

# Communicate with me
Use [Discussions ](https://github.com/Sharan-Python/vinyl-music-player/discussions) to talk about this repo
# Credits 
icons for the buttons- Provided by Ipython08

Volume slider- provided by Ipython08

New Vinyl Music Player icon- provided by Ipython08
