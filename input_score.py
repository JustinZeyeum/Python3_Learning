# Program to prompt for a score between 0.0 and 1.0.
# If the score is out of range print error.
# If the score is between 0.0 and 1.0 print a grade using the following table:
# Score grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range,
#print a suitable error message and exit.
score = input("Eneter Score: ")
try:
    fs = float(score)
except:
    print("Error, enter a numeric input")
#fs = 1.0
if fs >= 0.9 :
    print("A")
elif fs >= 0.8 :
    print("B")
elif fs >= 0.7 :
    print("C")
elif fs >= 0.6 :
    print("D")
elif fs < 0.6 :
    print("F")
else:
    print("Sorry, this is out of range")
