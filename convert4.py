# convert4.py
# A program that convert Fahrenheit temps to Celcius and prints a table
# redone by donovan Adams
def main():
    print "This is a program that converts Celcius to  Fahrenheit."
    print "Here are the temperatures every 10 degrees"
    print " ____________________"
    for i in [10,20,30,40,50,60,70,80,90,100]:
        fahrenheit = i
        celsius =  (fahrenheit - 32) * (5.0 / 9.0)
        print "The temperature is", fahrenheit, "degrees Celcius."
        i = i + 10
main()
