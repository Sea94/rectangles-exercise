# Rectangles exercise
## Description
This repo contains the python script along with an executable file running a simple application for interacting with two rectanlges.
The rectangles can be moved around the screen with a mouse and resized with arrow keys. The notification message is shown in case the rectangles overlap.

The application is written in Python 3.7 using [Pygame](https://www.pygame.org/docs/).

## Requirements
To run the script locally, first make sure you have Python 3.7+ [installed](https://www.python.org/downloads/).

Install dependencies:
`pip install pygame`

## Running the app
You can run the application directly by executing the `rectangles` exec file.

Otherwise, navigate to the folder with the `rectangles.py` script and run the command: `python rectangles.py`

## Known issues
* User can drag the rectangle outside the application window.
* Resizing the rectangle is done discretely on arrow key input. If the button is kept pressed, the rectangle doesn't keep resizing smoothly.
* The rectangles overlay the overlap notification message.

## Directions for improvement
* Fix the known issues.
* Make rectangles resizable with mouse events rather than keyboard input to use single interaction modality.
* Possibly, only highlight the intersection area when the rectangles overlapinstead of highlighting the whole rectangle shape.
