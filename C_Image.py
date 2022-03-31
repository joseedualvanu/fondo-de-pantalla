"""
MODULO C
    Description: modifiy and save the wallpaper

    Args:
		--
    Returns:

    Error:
        --
    Note:
        See https://www.datacamp.com/community/tutorials/docstrings-python
"""

def c_image(direction,log_name,amount,days,amount_day,start_time,direction_save):
    log_file = open(log_name, 'a')
    log_file.write('C - Image\n')
    print('C - Image')
    log_file.close()

    # Importing the PIL library
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

    # Open an Image
    img = Image.open(direction + 'Fondo.jpeg')

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # Custom font style and font size
    # myFont = ImageFont.truetype('FreeMono.ttf', 65)
    myFont_1 = ImageFont.truetype(direction +'Archivo/Fonts/ArchivoNarrow-Bold.ttf', 190)
    # myFont_1 = ImageFont.truetype(direction +'Archivo/Fonts/ArchivoNarrow-Bold.ttf', 196)
    myFont_2 = ImageFont.truetype(direction +'Archivo/Fonts/Qualy-Bold.ttf', 100)
    myFont_3 = ImageFont.truetype(direction +'Archivo/Fonts/Qualy-Bold.ttf', 50)
    # Add Text to an image
    # Amount
    I1.text((1920, 980), str(amount), font=myFont_1, fill =(185, 0, 43))
    # I1.text((10, 100), str(days), font=myFont, fill =(100, 0, 0))
    # Amount_day
    I1.text((2300, 650), str(amount_day), font=myFont_2, fill =(185, 0, 43))
    # Date
    I1.text((50, 50), start_time.strftime("%x"), font=myFont_3, fill =(100, 0, 0))

    # Display edited image
    # img.show()

    # Save the edited image
    #img.save(direction + "wallpaperactivo2.jpeg")
    img.save(direction_save + "wallpaperactivo.jpg")
