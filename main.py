"""
Pierre HAVARD

Bar-code generator for EAN-13 or code 128
Information relative to this project :

https://en.wikipedia.org/wiki/International_Article_Number


This is a simple bar-code generator app. It generates a bar code depending on what you entered in the entry field.
This app automatically opens the default app for photos to show the barcode
"""

import tkinter
from Draw import draw
from BarCodeEAN13 import BarCodeEAN13
from BARCODE128 import BarCode128

# variables
WIDTH = 480
HEIGHT = 320

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
ascii_characters = [chr(i) for i in range(128)]

# initialization of the screen
screen = tkinter.Tk()
screen.title("Bar-code generator")
screen_X = screen.winfo_screenwidth()
screen_Y = screen.winfo_screenheight()
screen.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, screen_X // 2 - 720 // 2, screen_Y // 2 - 480 // 2))  # this make
# the screen centered
screen.iconbitmap("Logo/logo_bar_code.ico")
screen.resizable(False, False)


# initialization of the font (used for EAN-13)
font = ("Arial", 10)

# we set the StringVar for the Entry Label
entry_var = tkinter.StringVar()
var_type = tkinter.IntVar()

# set the function that will return what is in the Entry variable


def instantiate_barcode():
    """
    This is the function that is called when you press "Convert" button it instantiate the correct class depending on
    what is in the Entry field and then draw the barcode thanks to the draw function
    :return: Nothing but it open the default app to show the bar code image
    """
    # we set the type of the barcode
    info = entry_var.get()
    type_of_the_bar_code = "unknown"

    if len(info) != 0:

        only_numbers = True
        only_ascii_characters = True

        for i in range(len(info)):
            if (info[i] in numbers) is False:
                only_numbers = False

        for j in range(len(info)):

            if (info[j] in ascii_characters) is False:

                only_ascii_characters = False

        if len(info) == 13 and only_numbers is True:
            type_of_the_bar_code = "EAN-13"

        elif only_ascii_characters is True and len(info) < 20:
            type_of_the_bar_code = "Code-128"

    # we instantiate the BarCodeEAN13 class or the BarCode128 class to make the barcode appear
    if type_of_the_bar_code == "EAN-13":
        my_bar = BarCodeEAN13(info)
        if my_bar.check_digit() is True:
            draw(my_bar.core_list, my_bar.information, type_of_the_bar_code)

        else:
            error_label.place(x=145, y=185)

    elif type_of_the_bar_code == "Code-128":
        my_bar = BarCode128(info)
        draw(my_bar.core_list, my_bar.information, type_of_the_bar_code)

    elif type_of_the_bar_code == "unknown":
        input_too_long_label.place(x=170, y=185)


# we set the labels
main_entry = tkinter.Entry(screen, width=30, textvariable=entry_var)
text_or_number_label = tkinter.Label(screen, text="Text or number you want in the bar-code :")
main_entry.configure(font=font)
convert_button = tkinter.Button(screen, text="Convert", command=instantiate_barcode, width=10, height=3)
error_label = tkinter.Label(screen, text="Your bar code is entered incorrectly", fg="#FF0C00")
input_too_long_label = tkinter.Label(screen, text="Input too long", fg="#FF0C00")


# we place the elements
main_entry.place(x=130, y=70)
convert_button.place(x=200, y=110)
text_or_number_label.place(x=125, y=45)

# we launch the mainloop
screen.mainloop()
