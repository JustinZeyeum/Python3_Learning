# A program asking user to input hours and rate per hour,
# Pay the hourly rate for the hours up to 40
#and 1.5 times the hourly rate for all hours worked above 40 hours.
# which display the pay on the screen

hrs = input("Enter Hours:") # user input hours
rate = input("Enter Rate:") # user input pay rate/hour
fh = float(hrs) # convert int to float
fr = float(rate) # convert int to float

if fh > 40:
    regp = fh * fr # regular pay calculation
    otp = (fh - 40.0) * (fr * 0.5) # overtime pay calculation
    gross_pay = regp + otp #  gross pay
else:
    gross_pay = fh * fr # gross pay
print("Pay:", gross_pay) # the gross pay is printed out as pay.
