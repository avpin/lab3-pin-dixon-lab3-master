# Programmers: Aaron & Richard
# Course:  CS151, Professor Franceshci
# Date: September 28, 2017
# Lab Assignment:  Lab 3
# Problem Statement:  Whether the distance a skier travels is good or not.
# Data In: The type of hill and their velocity.
# Data Out:  Time, distance, and if their distance is par or below par.
# Other files needed:  N/A
# Credits: None

import math
print("This program will determine whether your distance traveled from the ski jump is par or above par")

#User will enter the type of hill they will ski on.
height = input("Enter the type of hill. (Enter normal or large): ")

#This will determine the height, points per meter, and par based on the type of hill the user inputs.
if height == "normal":
    height = 46
    points_per_meter = 2
    par = 90
    print("The height is",height,"meters.")
elif height == "large":
    height = 70
    points_per_meter = 1.8
    par = 120
    print("The height is",height,"meters.")

#User will enter the velocity they go down the hill at.
velocity = input("Enter your velocity down the hill (in meters/sec): ")
velocity = float(velocity)

#This is the equation that will calculate the time.
time = math.sqrt((2*height)/9.8)

#This is the equation that will calculate the distance.
distance = velocity*time

#This is the equation that will calculate the points earned and output it to the user.
points_earned = 60+(distance-par)*points_per_meter
points_earned = int(points_earned)
print("You earned",points_earned,"points.")

#This will tell the user how well they did on their jump
if points_earned>=61:
    print("Great job!")
elif points_earned<10:
    print("What happened??")
else:
    print("Sorry, you didn't go very far.")
print("Thank you for using our program!")
