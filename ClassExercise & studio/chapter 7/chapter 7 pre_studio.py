'''Take the Luther Bell image and tint it red'''
import image

img = image.Image("luther.jpg")
win = image.ImageWin()
for x in range(img.getWidth()):
    for y in range(img.getHeight()):
        p = img.getPixel(x, y)
        red = p.getRed()
        green = p.getGreen()
        blue = p.getBlue()
        new_p = image.Pixel(255, green, blue)
        #or
        #new_p=image.Pixel(red,0,0)
        img.setPixel(x, y, new_p)
img.draw(win)
win.exitonclick()

