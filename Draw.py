# this file contain the draw function that draw the bar code
from PIL import ImageDraw, Image, ImageFont
from BarCodeEAN13 import BarCodeEAN13


def draw(binary_info, info, type):
    """

    :param binary_info: list of strings of binary numbers (1 is a line 0 is a blank)
    :param info: the information the bar code contain it is going to be shown at the bottom of the bar code
    :param type: EAN-13 or Code128
    :return: nothing but the 'bar_code.png' file is updated and it is show
    """

    cursor = 0
    font = ImageFont.truetype("Font/OpenSans-Regular.ttf", 23)

    if type == "EAN-13":

        image = Image.new('RGB', (290, 210), (255, 255, 255))
        image.save("bar_code.png")
        surface_to_draw_on = ImageDraw.Draw(image)

        for i in range(len(binary_info)):

            for j in range(len(binary_info[i])):
                if binary_info[i][j] == "1":
                    surface_to_draw_on.line((50 + cursor, 40, 50+cursor, 180), fill=(0, 0, 0), width=2)
                    cursor += 2

                else:
                    cursor += 2

        surface_to_draw_on.line((58, 175, 144, 175), fill=(255, 255, 255), width=20)
        surface_to_draw_on.line((152, 175, 232, 175), fill=(255, 255, 255), width=20)
        surface_to_draw_on.text((30, 160), info[0], (0, 0, 0), font=font)
        surface_to_draw_on.text((62, 160), info[1:7], (0, 0, 0), font=font)
        surface_to_draw_on.text((154, 160), info[7:], (0, 0, 0), font=font)
        image.save("bar_code.png")
        image.show()

    elif type == "Code-128":

        image = Image.new('RGB', (len(binary_info)*22 + 100, 210), (255, 255, 255))  # the size of the image is set
        # depending on the size of the information to encode
        image.save("bar_code.png")
        surface_to_draw_on = ImageDraw.Draw(image)
        surface_to_draw_on.text(((len(binary_info)*22)//2, 170), info, (0, 0, 0), font=font)

        for i in range(len(binary_info)):
            binary_info[i] = str(binary_info[i])
            for j in range(len(binary_info[i])):

                if binary_info[i][j] == "1":

                    surface_to_draw_on.line((50 + cursor, 30, 50 + cursor, 170), fill=(0, 0, 0), width=2)
                    cursor += 2

                else:
                    cursor += 2
        image.save("bar_code.png")
        image.show()
