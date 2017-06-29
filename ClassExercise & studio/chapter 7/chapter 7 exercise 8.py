def greyscale_image(img_file="cy.png"):
    "Write a function to convert the image to grayscale."
    oldimg, newimg, width, height, win = setup_image(img_file)

    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            p = newimg.getPixel(col, row)
            avg = (p[0] + p[1] + p[2]) / 3
            p.red = p.green = p.blue = avg
            newimg.setPixel(col, row, p)


        write_image(img_file, newimg, win, "_grey")