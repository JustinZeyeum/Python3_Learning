# A program asking user to input hours and rate per hour,
# Pay the hourly rate for the hours up to 40
#and 1.5 times the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay()
#and use the function to do the computation.
#The function should return a value.
# which display the pay on the screen
def computepay(fh,fr):
    if fh > 40:
        regp = fh * fr # regular pay calculation
        otp = (fh - 40.0) * (fr * 0.5) # overtime pay calculation
        gross_pay = regp + otp #  gross pay
    else:
        gross_pay = fh * fr # gross pay
    return gross_pay

hrs = input("Enter Hours:") # user input hours
rate = input("Enter Rate:") # user input pay rate/hour
fh = float(hrs) # convert int to float
fr = float(rate) # convert int to float
p = computepay(fh,fr) # calling the function
print("Pay",p)
