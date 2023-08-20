# Days Bygone Region Detection Script (For Personal Customization Only)

This project contains a script designed to interact with the Days Bygone game running on the BlueStacks App Player. It's designed to assist users with accessibility needs or those seeking to customize their interface, without modifying or interfering with the game itself. This code must not be used to violate the Terms of Service of the game or service.

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Determining Regions](#determining-regions)
6. [Disclaimer](#disclaimer)

## Introduction

This script provides a way for users to interact with Days Bygone, allowing for personal customization and interface assistance.

## Requirements

The script requires the following libraries:

- `cv2`
- `numpy`
- `pyautogui`
- `pygetwindow`

Install these packages using pip:

```bash
pip install opencv-python numpy pyautogui pygetwindow
```

## Configuration

Before using the script, you may need to configure the regions to match the exact coordinates of the buttons and elements within your BlueStacks window. This may vary based on the resolution and scale of your computer.

### How to Determine Regions

Use the provided code snippet to draw rectangles around regions in an image to find coordinates. Modify the regions according to your requirements.

## Usage

1. Run the main script, which will interact with the Days Bygone window.
2. The script assists in various actions like clicking stats, rewinding, battling, etc., without modifying the game or interfering with the game experience.

### Code for Region Detection

To determine the coordinates of the regions within your game window, use the following code snippet:

```python
import cv2
import numpy as np

def draw_rectangle(event, x, y, flags, param):
    global drawing, top_left, bottom_right
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        top_left = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            bottom_right = (x, y)
            img_temp = img.copy()
            cv2.rectangle(img_temp, top_left, bottom_right, (0, 255, 0), 2)
            cv2.imshow('Select Region', img_temp)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
        print(f"Region coordinates: {top_left} to {bottom_right}")

drawing = False
top_left = (0, 0)
bottom_right = (0, 0)
img = cv2.imread('game_screenshot.png')
cv2.namedWindow('Select Region')
cv2.setMouseCallback('Select Region', draw_rectangle)
cv2.imshow('Select Region', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Disclaimer

This code is intended for personal customization, interface assistance, or accessibility support. It must not be used in a way that violates the Terms of Service of Days Bygone or any other games or services.
