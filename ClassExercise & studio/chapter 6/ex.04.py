'''Modify the turtle bar chart program from the previous chapter so that the bar for any value of 200 or more is filled with red,
 values between [100 and 200) are filled yellow, and bars representing values less than 100 are filled green.
'''
def turtle(chart):
    if chart>=200:
        return "red"
    else:
        if chart>100 and chart<200:
            return "yellow"
        else:
            return "green"
chart=50
print("The bar for:",turtle(chart))