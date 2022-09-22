# School-Tello-UI

This is a program I made for school! It might not be the best but it works. 

There is a GUI that you can controll the drone in.
You cannot use the video from the tello api since i'm slready using pygame

## Controlls

The buttons on the top are the movements
on the right bottom are to move the heights
on the left bottom you can make the drone flip
Press escape to stop the drone

## SETUP:

- Install Python from python.org
- Install PyCharm ( It'll probably already be installed if you are using a school computer )
- Open the terminal ( It should be on the the bottom of pycharm ) then write `python3 setup.py install` in the terminal
- Right Click on the code and click "Run Code" or something of that sort

## Debugging:
- if it says that there is no connection, you need to connet to the Tello WiFi ( info below this )
- if there is a long line of text, read it from the bottom up. There might be something that says that you need to install something. To install the program, type `pip install <program>` ofcourse replace <program> with what ever it says to install
- ask me lmao if i'm still there
 - if you are reading this in the future for other classes, copy and paste the last 3 ish lines that seem important into google. If the results don't match type `Tello EDU` into the beginning or the end of the search. 
- There might be a message that says that this connection is already in use. That usually means that pygame is still running. So close that app. (This will only happen if the code was run once but it crashed)

## How to go on the tello WiFi

There should be a button on the drone. If it starts blinking different lights, there should be a WiFi on your computer that says Tello-<Numbers> Connect to that.

## If you want to add something or are trying to read the code

pygame is a interface that draws on the screen. 
Tello is a api made by Code4FunSydney bad code but it works https://github.com/code4funSydney/Tello
