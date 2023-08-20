import random
import cv2
import pyautogui
import numpy as np
import pygetwindow as gw
import time

# Print all window titles
for window in gw.getAllWindows():
    print(window.title) # BlueStacks App Player

# Get the window
window = gw.getWindowsWithTitle('BlueStacks App Player')[0]

# Get the coordinates
left, top, width, height = window.left, window.top, window.width, window.height

# Take a screenshot
screenshot = pyautogui.screenshot(region=(left, top, width, height))

screenshot.save('game_screenshot.png')

# Convert the screenshot to a NumPy array
image = np.array(screenshot)

# Convert the image from RGB to BGR (OpenCV uses BGR by default)
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('Processed Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# stats button Region coordinates: (7, 109) to (68, 177)
# %50 button Region coordinates: (696, 483) to (753, 505)
# upgrade damage Region coordinates: (386, 132) to (488, 157)
# %100 button Region coordinates: (772, 484) to (832, 507)
# upgrade crit Region coordinates: (808, 342) to (910, 368)

# Define the regions to click
click_regions_stats = [
    ((7, 109), (68, 177)),     # stats button
    ((696, 483), (753, 505)),  # %50 button
    ((386, 132), (488, 157)),  # upgrade damage
    ((772, 484), (832, 507)),  # %100 button
    ((808, 342), (910, 368))   # upgrade crit
]




# rewind section button Region coordinates: (7, 477) to (75, 546)
# perform rewind button Region coordinates: (238, 218) to (346, 244)
# click rewind button Region coordinates: (551, 464) to (661, 488)
# perform rewind button Region coordinates: (238, 218) to (346, 244)
# click rewind button Region coordinates: (551, 464) to (661, 488)
# upgrade elixir mastery button Region coordinates: (763, 170) to (891, 202)
# upgrade confirm button Region coordinates: (414, 366) to (528, 391)

click_regions_rewind = [
    ((7, 477), (75, 546)),     # rewind button
    ((238, 218), (346, 244)),  # perform rewind button
    ((551, 464), (661, 488)),  # click rewind button
    ((238, 218), (346, 244)),  # perform rewind button
    ((551, 464), (661, 488)),  # click rewind button
    ((763, 170), (891, 202)),  # upgrade elixir mastery button
    ((414, 366), (528, 391))   # upgrade confirm button
]

# battle button Region coordinates: (832, 47) to (922, 81)
# campaign button Region coordinates: (312, 151) to (629, 211)
# start with x2 button Region coordinates: (482, 364) to (597, 392)

click_regions_battle = [
    ((832, 47), (922, 81)),     # battle button
    ((312, 151), (629, 211)),   # campaign button
    ((482, 364), (597, 392))    # start with x2 button
]

# in battle, click randomly on the screen
# Region coordinates: (315, 129) to (68, 475)
# Region coordinates: (363, 489) to (572, 556)

click_regions_in_battle = [
    ((68, 129), (315, 475)),    # in battle, click randomly on the screen
    ((363, 489), (572, 556)),   # in battle, click randomly on the screen
    ((68, 129), (315, 475))
]

# battle end (120 day reached)
# return main menu button Region coordinates: (360, 443) to (459, 471)

click_regions_exit_battle = [
    ((360, 443), (459, 471))    # return main menu button
]

# Function to click a specific region
def click_region(region):
    x_start, y_start = region[0]
    x_end, y_end = region[1]
    x_click = random.randint(x_start, x_end) + left
    y_click = random.randint(y_start, y_end) + top
    pyautogui.click(x_click, y_click)


def click_stats():
    for region in click_regions_stats:
        click_region(region)
        sleep_time = random.uniform(0.5, 2)
        time.sleep(sleep_time)


def click_rewind():
    for region in click_regions_rewind:
        click_region(region)
        sleep_time = random.uniform(0.5, 2)
        time.sleep(sleep_time)


def click_battle():
    for region in click_regions_battle:
        click_region(region)
        sleep_time = random.uniform(0.5, 2)
        time.sleep(sleep_time)


def click_in_battle():
    for region in click_regions_in_battle:
        click_region(region)
        sleep_time = random.uniform(3, 10)
        time.sleep(sleep_time)


def click_exit_battle():
    for region in click_regions_exit_battle:
        click_region(region)
        sleep_time = random.uniform(0.5, 2)
        time.sleep(sleep_time)


window.activate()
time.sleep(2)
# Main loop to restart the whole sequence
while True:
    click_stats()
    click_rewind()
    click_battle()

    battle_start_time = time.time()
    click_in_battle()
    while True:
        if time.time() - battle_start_time > 80:  # 90 seconds
            break

    click_exit_battle()
    time.sleep(2)  # Add a delay before restarting the whole sequence, if needed
