import time
from pathlib import Path

import pyautogui
from PIL import Image


"""
HOW TO USE :
I suggest first opening an instance of your DEFAULT web browser (like Firefox), and open an empty tab (no other tab).
Make sure your Nexus account is currently logged in.
Add whatever collection you wish to download to Vortex.

Whenever the "DOWNLOAD" button from the Vortex UI appears is when my script is starting to be useful : when Vortex
starts iterating over the list of mods to be installed and showing you the "download" prompts, you can run my script.

The script looks for the "download" button from the vortex UI : it means you HAVE to let Vortex show the prompts for 
my scripts to detect it. Likewise, my script will then look for the Nexus's page "SLOW DOWNLOAD" button, so you HAVE
to let vortex open the nexus URL. I suggest not using your computer until the collection is done downloading, or unless
vortex is giving you other prompts that hide the "download" button's prompt. THE DOWNLOAD BUTTON MUST BE VISIBLE :
the script doesn't magically detect that the prompt is here, the WHOLE download button MUST be visible on the screen. 

Once a mod's download is started, the script will go back to looking for a "download" button from the Vortex UI.
So if it's a big download, you can keep using the computer and wait for Vortex to show the next prompt. I strongly 
advise NOT touching anything (keyboard or mouse) whenever Vortex shows a prompt for downloading a mod, because 
the script takes control of the mouse pointer to do everything (you'll actually see the pointer move at the buttons 
locations). 

The script was developed, used, and adjusted on a 1080p monitor (which means if you have a bigger or larger 
screen resolution, you may or may not have to retake the screenshots yourself, and adjust the confidence factors
used for the locateOnScreen method calls; it might take a few tries).

With this, downloading a collection of ~500 mods will still take several hours, but you won't need to download 
everything manually. However I recommend checking on it regularly, especially the first few dozens of mods, 
to be sure the "download" button of the vortex's UI and the "slow download" button of the nexus's page are correctly 
detected and clicked. Personally, I sat in front of my computer and gamed on my Switch until I was assured it was 
working as intended.

I'm sharing to help those who don't want to pay for a Premium account on Nexus and are willing to try another way.
It's still slow, it may be buggy, and the script is certainly not optimal. It suits my needs, and I hope it can help
somebody else. However if you are unhappy with its performances, I suggest you simply don't use it, I don't have much 
more time for this and debugging/troubleshooting can be very time-consuming.

Extremely basic script :
1. Waits for a picture of the WHOLE "download" button from the Vortex UI to appear on the screen and clicks it
2. Waits for a picture of the WHOLE "slow download" button from Nexus's download page to appear and clicks it
3. Then goes back to waiting for Vortex's "download" button to appear...
"""



# Load the image file of the "download" button
# Note that the pictures were cropped from a 1080p screenshot, and are used by the locateOnScreen to detect
# the buttons on the screen : you may have to retake these pictures and adjust the confidence factors depending
# on your system and screen resolution
download_button_image = Path('./VORTEX_DOWNLOAD_BTN.PNG')
slow_download_btn_img = Path('./NEXUS_SLOW_DOWNLOAD_BTN.PNG')

# Confidence factors for calls to locateOnScreen : the vortex UI has several buttons that look like the "download"
# button; if the confidence factor is too low, the script will click the wrong buttons, but if it's too high,
# it will sometimes never detect the "download" button. This was chosen with a resolution of 1080p, the factors may
# have to be adjusted depending on your system
first_vortex_btn_confidence = 0.935
second_vortex_btn_confidence = 0.95  # Can try with same value as first factor

# Initializing a counter and a time to sleep : if the counter goes too high, the checks are performed less often
# And at the next mod download iteration, the counter is set back to zero
nothing_found_counter = 0
time_to_sleep = 1

# Keep searching for vortex's "download" button
while True:
    # Search for the "download" button on the screen
    download_button_pos = pyautogui.locateOnScreen(Image.open(download_button_image),
                                                   confidence=first_vortex_btn_confidence)
    time.sleep(1)
    if download_button_pos is not None:
        # The "download" button was found
        print("Found the download button at:", download_button_pos)

        # Click the "download" button
        pyautogui.click(download_button_pos)
        download_button_pos = pyautogui.locateOnScreen(Image.open(download_button_image),
                                                       confidence=second_vortex_btn_confidence)
        # Sometimes vortex's window loads with the previous download button : verify a second time
        if download_button_pos is not None:
            pyautogui.click(download_button_pos)

        # The 'download' button should have been clicked :
        # it's opening a web browser or a tab with the "SLOW DOWNLOAD" button
        nothing_found_counter = 0
        download_started = False
        # Checking in a nested while loop : the web page may sometimes be very slow to open for various reasons
        while not download_started:
            # Wait for the page's "slow download" button to appear
            time.sleep(
                2)  # Adjust the duration of the sleep as needed, depending on your system and internet connection

            # Click the "slow download" button
            slow_download_button_pos = pyautogui.locateOnScreen(Image.open(slow_download_btn_img))

            if slow_download_button_pos is not None:
                print("Found the slow download button at:", slow_download_button_pos)
                pyautogui.click(slow_download_button_pos)
                time.sleep(6)  # At least 5, corresponding to nexus's timer "download starts in..."
                download_started = True
                # At this point the download has started; back to the outer loop, looking for a "download" btn in Vortex

            else:
                print("Could not find the slow download button on the screen.")
                # Next iteration of the while loop : maybe the web page was too slow to load

    else:
        # The "download" button was not found
        nothing_found_counter += 1
        if nothing_found_counter < 10:
            time_to_sleep = 2  # If a bunch of small mods are one after another
        elif nothing_found_counter < 50:
            time_to_sleep = nothing_found_counter
        else:
            time_to_sleep = 50  # The collection might be fully downloaded, or it's downloading a large mod

        print(f"Could not find the download button on the screen. Sleeping {time_to_sleep} seconds.")
        # Wait for some time before searching again
        time.sleep(time_to_sleep)  # Adjust the time_to_sleep values as needed
