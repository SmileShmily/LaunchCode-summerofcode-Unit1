def smooth_image(img_file="cy_double.png"):
    """After you have scaled an image too much it looks blocky. One way of reducing
    the blockiness of the image is to replace each pixel with the average values
    of the pixels around it. This has the effect of smoothing out the changes in
    color. Write a function that takes an image as a parameter and smooths the
    image. Your function should return a new image that is the same as the old
    but smoothed."""

    oldimg, newimg, width, height, win = setup_image(img_file)

    for col in range(newimg.getWidth()):
        for row in range(newimg.getHeight()):
            p = newimg.getPixel(col, row)
            neighbors = []
            # Put the 8 surrounding pixels into neighbors
            for i in range(col - 1, col + 2):
                for j in range(row - 1, row + 2):
                    try:
                        neighbor = newimg.getPixel(i, j)
                        neighbors.append(neighbor)
                    except:
                        continue
            nlen = len(neighbors)
            # Average out the RBG values
            if nlen:
                # Uncommented, the following line would leave most of the white
                # untouched which works a little better for real photographs, imo.
                # ~ if nlen and p[0]+p[1]+p[2] < 690:
                p.red = sum([neighbors[i][0] for i in range(nlen)]) / nlen
                p.green = sum([neighbors[i][1] for i in range(nlen)]) / nlen
                p.blue = sum([neighbors[i][2] for i in range(nlen)]) / nlen
                newimg.setPixel(col, row, p)


        write_image(img_file, newimg, win, "_smooth")