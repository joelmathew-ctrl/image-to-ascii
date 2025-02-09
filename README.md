# Image to ASCII Converter

## Overview
This Python script, `image-to-ascii.py`, converts an image into ASCII art. It resizes the image, converts it to grayscale, and maps the brightness of each pixel to a corresponding ASCII character from a predefined gradient. The result is a text-based representation of the original image.

## Features
- **Image Resizing**: Automatically resizes the image while maintaining the aspect ratio.
- **Grayscale Conversion**: Converts the image to grayscale using a weighted average of the RGB channels.
- **ASCII Mapping**: Maps pixel brightness to a gradient of ASCII characters.
- **ASCII Art Output**: Prints the ASCII art to the console.

## Requirements
- Python 3.x
- `Pillow` library (for image processing)
- `numpy` library (for matrix operations)

## Installation
1. **Install Python**: Ensure you have Python 3.x installed on your system.
2. **Install Required Libraries**:
   ```bash
   pip install pillow numpy
   ```

## Usage

1. **Save the script**: Save the `image-to-ascii.py` script to your local machine.

2. **Run the script**: Open a terminal or command prompt and navigate to the directory where the script is saved.

3. **Execute the script**: Run the script using Python:
   ```bash
   python image-to-ascii.py
   ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
