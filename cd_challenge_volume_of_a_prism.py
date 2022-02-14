"""
Create a function that calculates the volume of a rectangular prism in cubic feet.
The formula to find the volume is V = l * w * h where l, w, and h are length, width, and height, respectively.
First, create three variables representing length, width, and height.
Assign each of them an integer as user input using the input() function and int().
Next, create a function to calculate the volume of the rectangular prism.
It should have 3 parameters representing l, w, and h and return the volume calculated using those 3 parameters.
Use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet."
You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.
"""

length = int(input("Please enter the length of your rectangular prism"))
width = int(input("Please enter the width of your rectangular prism"))
height = int(input("Please enter the height of your rectangular prism"))


def volume(le, wi, he):
    return le * wi * he

new_volume = str(volume(length, width, height))

print("The volume of the rectangular prism is " + new_volume + " cubic feet.")
