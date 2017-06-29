def median(p, col, row):
    """When you scan in images using a scanner they may have lots of noise due
    to dust particles on the image itself or the scanner itself, or the images
    may even be damaged. One way of eliminating this noise is to replace each
    pixel by the median value of the pixels surrounding it."""
    neighbors = []
    # Put the 8 surrounding pixels into neighbors
    for i in range(col-1, col+2):
        for j in range(row-1, row+2):
            try:
                neighbor = newimg.getPixel(i, j)
                neighbors.append(neighbor)
            except:
                continue
    nlen = len(neighbors)
    if nlen:
        red = [neighbors[i][0] for i in range(nlen)]
        green = [neighbors[i][1] for i in range(nlen)]
        blue = [neighbors[i][2] for i in range(nlen)]
        # Sort the lists so we can later find the median.
        for i in [red, green, blue]:
            i.sort()
        # If the list has an odd number of items in it.
        if nlen % 2:
            p.red = red[len(red)/2]
            p.green = green[len(green)/2]
            p.blue = blue[len(blue)/2]
        else:
            p.red = (red[len(red)/2] + red[len(red)/2-1])/2
            p.green = (green[len(green)/2] + green[len(green)/2-1])/2
            p.blue = (blue[len(blue)/2] + blue[len(blue)/2-1])/2

    return p