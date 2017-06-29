'''One of the simplest things you can do using the turtle module is to draw a line.
 There are always four steps you need to do in order to use the turtle module:

    Import the turtle module. If we skip this step, there’ll be no turtle to control.
    Create a turtle to control.
    Draw things. Do stuff. This will also automatically create the screen.
    Run turtle.done(). (NOT bob.done()!)

Notice that turtle.done() will pause the program. You’ll need to close the window in order to continue.'''

# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "bob"
bob = turtle.Turtle()

# Step 3: Move in the direction Bob's facing for 50 pixels
bob.forward(50)

# Step 4: We're done!
turtle.done()