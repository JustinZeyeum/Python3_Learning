# A program asking user to input hours and rate per hour,
# which display the pay on the screen

hrs = input("Enter Hours:") # user input hours
rate = input("Enter Rate:") # user input pay rate

gross_pay = float(hrs) * float(rate) # program compute the gross pay calculation
print("Pay:", gross_pay) # the gross pay is printed out as pay.
