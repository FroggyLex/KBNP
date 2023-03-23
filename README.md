# KBNP

# WHAT IS IT?

Extremely basic script :
1. Waits for a picture of the WHOLE "download" button from the Vortex UI to appear on the screen and clicks it
2. Waits for a picture of the WHOLE "slow download" button from Nexus's download page to appear and clicks it
3. Then goes back to waiting for Vortex's "download" button to appear...

It will simply save you the mind-numbing hassle of clicking links for hours... The script will STILL take hours to download your collection, though!

# WHAT IS IT NOT ?

* It doesn't actually bypass nexus's premium : it simply emulates a user clicking on a visible "download" button of the vortex interface, then a user cliking on a visible "slow download" button of the nexus's mod download page. Your download speed is still limited.
* It doesn't emulate a user clicking on ANYTHING ELSE that is NOT the "download" button of the vortex interface THEN the nexus "slow download" button. It must be exactly in that order, and it must be exactly those buttons. It won't work for anything else than exactly the vortex interface then the nexus interface.
* It doesn't magically guess where the buttons are : that's what the two .png files are for. The script will load those images, check on your screen if one of these buttons is present, and click them. If the button is not fully visible, it will not click it. Also, depending on your system, the buttons visible on your screen may be slightly different than the given images : in that case, the script won't click the buttons. If that happens, you will have to take screenshots of the buttons yourself, and replace the images I provided.


# DEPENDENCIES (you MUST install them ALL if you want it to work)

* A Nexus account logged into your default web browser, obviously

* Whatever the collection you want to install asked you to do. My script ONLY manages clicking the download buttons, and nothing else!

* `Python3` for your OS (tested with `Python 3.10`)

* (optional) `pip`, to install the following dependencies easily

* `opencv-python` for Python's `OpenCV` dependency

* `pillow` for Python's `PIL` dependency

* `pyautogui` for Python's dependency

# HOW TO USE

First, install the dependencies listed above. Installation will dependend on your OS : googling "How to install X on (my os)" should easily give you basic tutorials. You should be all setup in a few minutes.

Then, download and extract the content of this repo, and execute the `main.py` file. You may do so by opening the folder in a terminal, and simply typing:

`python3 ./main.py`

* I suggest opening an instance of your DEFAULT web browser (like Firefox), and opening an empty tab (no other tab).
Make sure your Nexus account is currently logged in.
Add whatever collection you wish to download to Vortex and follow their steps.

* Whenever the "DOWNLOAD" button from the Vortex UI appears is when my script is starting to be useful : when Vortex
starts iterating over the list of mods to be installed and showing you the "download" prompts, you can run my script.

* The script looks for the "download" button from the vortex UI : it means you HAVE to let Vortex show the prompts for 
my scripts to detect it. Likewise, my script will then look for the Nexus's page "SLOW DOWNLOAD" button, so you HAVE
to let vortex open the nexus URL. I suggest not using your computer until the collection is done downloading, or unless
vortex is giving you other prompts that hide the "download" button's prompt. THE DOWNLOAD BUTTON MUST BE VISIBLE :
the script doesn't magically detect that the prompt is here, the WHOLE download button MUST be visible on the screen. 

* Once a mod's download is started, the script will go back to looking for a "download" button from the Vortex UI.
So if it's a big download, you can keep using the computer and wait for Vortex to show the next prompt. **I strongly 
advise NOT touching anything (keyboard or mouse) whenever Vortex shows a prompt for downloading a mod**, because 
the script takes control of the mouse pointer to do everything (you'll actually see the pointer move at the buttons 
locations). 

# Note / warning

 The script was **developed, used, and adjusted on a 1080p monitor** (which means if you have a bigger or larger 
screen resolution, **you may or may** not have to retake the screenshots yourself, and adjust the confidence factors
used for the locateOnScreen method calls; it might take a few tries).

With this, downloading a collection of ~500 mods will still take several hours, but you won't need to download 
everything manually. However I recommend checking on it regularly, especially the first few dozens of mods, 
to be sure the "download" button of the vortex's UI and the "slow download" button of the nexus's page are correctly 
detected and clicked. Personally, I sat in front of my computer and gamed on my Switch until I was assured it was 
working as intended.

I'm sharing to help those who don't want to or can't pay for a Premium account on Nexus and are willing to try another way.
It's still slow, it may be buggy, and the script is certainly not optimal. It suits my needs, and I hope it can help
somebody else. However if you are unhappy with its performances, I suggest you simply don't use it : I don't have much 
more time for this and optimizing/debugging can be very time-consuming.
