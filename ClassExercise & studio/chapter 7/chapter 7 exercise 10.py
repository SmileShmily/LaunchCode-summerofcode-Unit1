def sepia_image(img_file="cy.png"):
    """Sepia Tone images are those brownish colored images that may remind you
    of times past. The formula for creating a sepia tone is as follows:
    newR = (R × 0.393 + G × 0.769 + B × 0.189)
    newG = (R × 0.349 + G × 0.686 + B × 0.168)
    newB = (R × 0.272 + G × 0.534 + B × 0.131)
    Write a function to convert an image to sepia tone. Hint: Remember that rgb
    values must be integers between 0 and 255."""

    oldimg, newimg, width, height, win = setup_image(img_file)

    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            try:
                p = newimg.getPixel(col, row)
                p.red = int(p.red * 0.393 + p.green * 0.769 + p.blue * 0.189)
                p.green = int(p.red * 0.349 + p.green * 0.686 + p.blue * 0.168)
                p.blue = int(p.red * 0.272 + p.green * 0.534 + p.blue * 0.131)
                newimg.setPixel(col, row, p)
            except:
                continue


        write_image(img_file, newimg, win, "_sepia")