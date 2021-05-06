"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
DEFAULT_FILE = 'images/simba-sq.jpg'

'''
Bug: only works for default image-size, which also must be square.
'''

def main():
    ##Set-up blank image - currently uses default sizing above.

    filename = get_file()
    original_image = SimpleImage(filename)
    original_image.show()

    patch_width = original_image.width
    patch_height = original_image.height
    image_width = N_COLS * patch_width
    image_height = N_ROWS * patch_height

    final_image = SimpleImage.blank(image_width, image_height)

    #Create patch and add it to final_image
    pink_patch = make_recolored_patch(filename, 1.5, 0, 1.5)
    green_patch = make_recolored_patch(filename, .07, 1.5, .08)
    blue_patch = make_recolored_patch(filename, .2, .2, 1.8)
    yellow_patch = make_recolored_patch(filename, 1.8, 1.8, .07)
    orange_patch = make_recolored_patch(filename, 1.2, .7, .08)

    #Set first patch - pink
    final_image = set_patch(final_image, pink_patch, 1, 1)

    #set second patch - green
    final_image = set_patch(final_image, green_patch, 2, 1)

    # set third patch - orange
    final_image = set_patch(final_image, orange_patch, 3, 1)

    # set fourth patch - yellow
    final_image = set_patch(final_image, yellow_patch, 1, 2)

    # set fifth patch original
    final_image = set_patch(final_image, original_image, 2, 2)

    # set sixth patch - blue
    final_image = set_patch(final_image, blue_patch, 3, 2)

    final_image.show()

def set_patch(image, patch, row, col):
    '''
    Implement this function to add a patch to the new image.
    It takes in a newly created patch and writes it onto the final image.
    :param image: the image that the patch will be written onto
    :param patch: the patch that will be written onto the image
    :param row: the row that the patch will be placed in
    :param col: the column that the patch will be placed in
    '''
    width = patch.width
    height = patch.height
    for y in range(height):
        for x in range(width):
            pixel = patch.get_pixel(x, y)
            image.set_pixel(x + width * (row - 1), y + height * (col - 1), pixel)

    return image

def make_recolored_patch(filename, red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param filename: Filename entered by user in main
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(filename)
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()