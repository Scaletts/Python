'''Darkening an image requires adjusting its pixels toward black as a limit, whereas lightening an image requires adjusting them toward white as a limit. Because black is RGB (0, 0, 0) and white is RGB (255, 255, 255), adjusting the three RGB values of each pixel by the same amount in either direction will have the desired effect. Of course, the algorithms must avoid exceeding either limit during the adjustments.

Lightening and darkening are actually special cases of a process known as color filtering. A color filter is any RGB triple applied to an entire image. The filtering algorithm adjusts each pixel by the amounts specified in the triple. For example, you can increase the amount of red in an image by applying a color filter with a positive red value and green and blue values of 0. The filter (20, 0, 0) would make an image’s overall color slightly redder. Alternatively, you can reduce the amount of red by applying a color filter with a negative red value. Once again, the algo- rithms must avoid exceeding the limits on the RGB values.

Develop three algorithms for lightening, darkening, and color filtering as three related Python functions, lighten, darken, and colorFilter. The first two functions should expect an image and a positive integer as arguments. The third function should expect an image and a tuple of integers (the RGB values) as argu- ments. The following session shows how these functions can be used with the images image1, image2, and image3, which are initially transparent:'''
from images import Image


def colorFilter(image, colorAmount):

    def baseValue(value, offset):
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)

    (r, g, b) = colorAmount
    for h in range(image.getHeight()):
        for w in range(image.getWidth()):
            (red, green, blue) = image.getPixel(w, h)
            (red, green, blue) = (baseValue(red, r), baseValue(green, g), baseValue(blue, b))
            image.setPixel(w, h, (red, green, blue))


def lighten(image, amount):
    colorFilter(image, (amount, amount, amount))


def darken(image, amount):
    colorFilter(image, (-amount, -amount, -amount))

def main():
    img = Image("123.png")

    # colorFilter(img, (50, 0, 0))  # Increase Red

    # colorFilter(img, (0, 50, 0))   #Increase Green

    # colorFilter(img, (0, 0, 50))    # Increase Blue

    # lighten(img, 50)

    darken(img, 20)

    img.draw()


if __name__ == '__main__':
    main()