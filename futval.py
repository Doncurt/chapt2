# futval.py
# A program to compute the value of an investment
#  input of the principal, years of investment and the APR
# by: John M. Zelle
def main():
    print "This program calculates the future value of an investment."
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annualized interest rate: ")
    years= input("How many years are you investing for")
    for i in range(years):
        principal = principal * (1 + apr)
    print "The amount in 10 years is:", principal
main()
