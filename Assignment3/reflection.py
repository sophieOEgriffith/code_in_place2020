"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)
    height = image.height
    width = image.width
    reflected = SimpleImage.blank(width, height * 2)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            reflected.set_pixel(x, y, pixel)
            reflected.set_pixel(x, height * 2 - (y + 1), pixel)

    return reflected


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    filename = get_file()
    original = SimpleImage(filename)
    original.show()
    reflected = make_reflected(filename)
    reflected.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()
