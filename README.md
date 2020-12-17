# Rectangles exercise
## Description
This repo contains the python script along with a [link to a downloadable executable file](https://drive.google.com/file/d/1AvFMvsM9kbSJ0WEoxaZSdLYx9Gq14-MX/view?usp=sharing) running a simple application for interacting with two rectanlges.
The rectangles can be moved around the screen with a mouse and resized with arrow keys. The notification message is shown in case the rectangles overlap.

<div style="background:#010023;" align="center">
  <p>
  <img src="demo.gif" width="400" />
  </p>
</div>

The application is written in Python 3.7 using [Pygame](https://www.pygame.org/docs/).

## Requirements
To run the script locally, first make sure you have Python 3.7+ [installed](https://www.python.org/downloads/).

Install dependencies:
`pip install pygame`

## Running the app
You can run the application directly by executing the `rectangles` exec file, which you can [download from Google Drive](https://drive.google.com/file/d/1AvFMvsM9kbSJ0WEoxaZSdLYx9Gq14-MX/view?usp=sharing) (stored externally due to file size limit on githib). Once downloaded, run the file locally. It might take up to 20 sec for the app to load.

_The exec file was created with [pyinstaller](https://www.pyinstaller.org/) utility and tested on MacOS Catalina 10.15.7._

Otherwise, navigate to the folder with the `rectangles.py` script and run the command: `python rectangles.py`

## Known issues
* User can drag the rectangle outside the application window.
* Resizing the rectangle is done discretely on arrow key input. If the button is kept pressed, the rectangle doesn't keep resizing smoothly.
* The rectangles overlay the overlap notification message.

## Directions for improvement
* Fix the known issues.
* Make rectangles resizable with mouse events rather than keyboard input to use single interaction modality.
* Possibly, only highlight the intersection area when the rectangles overlapinstead of highlighting the whole rectangle shape.
