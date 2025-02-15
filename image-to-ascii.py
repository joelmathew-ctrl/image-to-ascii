# Name: image-to-ascii.py
# Author: Joel Mathew
# Date: February 8th, 2025

from PIL import Image
import numpy as np

# Prompt the user for the filename
filename = input("Enter the name of the image file to convert to ASCII: ")

try:
    # Load and resize image
    image = Image.open(filename)  # Open image
    new_width = 600
    aspect_ratio = image.height / image.width
    new_height = int(new_width * aspect_ratio)  # Maintain aspect ratio
    image = image.resize((new_width, new_height))
    width, height = image.size

    image = image.convert("RGB")  # Ensure RGB format

    print("\nSuccessfully loaded and resized image!")
    print(f"Resized Image size: {width} x {height}\n")

    # Convert image to pixel array
    img_array = np.array(image)
    print("Successfully constructed pixel matrix!")
    print(f"Pixel matrix size: {img_array.shape[1]} x {img_array.shape[0]}")

    # Construct brightness matrix (grayscale conversion)
    brightness_matrix = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            r, g, b = img_array[y][x]
            brightness_matrix[y][x] = 0.21*r + 0.72*g + 0.07*b  # Average brightness

    print("Successfully constructed brightness matrix!")
    print(f"Brightness matrix size: {brightness_matrix.shape[1]} x {brightness_matrix.shape[0]}")

    # ASCII gradient (from dark to light)
    ascii_string = "`^\\\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    num_ascii_chars = len(ascii_string)  # Total characters in the gradient

    # Create ASCII matrix
    ascii_matrix = np.empty((height, width), dtype=str)

    # Map brightness to ASCII characters using direct indexing
    for y in range(height):
        for x in range(width):
            brightness = brightness_matrix[y][x]  # Get brightness value (0-255)
            
            # Normalize brightness to ASCII index
            ascii_index = int((brightness / 255) * (num_ascii_chars - 1))
            
            # Assign corresponding ASCII character
            ascii_matrix[y][x] = ascii_string[ascii_index]

    # Print ASCII art
    print("\nASCII Art:\n")
    for row in ascii_matrix:
        print("".join(row))  # Join row elements into a single line

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")
except Exception as e:
    print(f"An error occurred: {e}")