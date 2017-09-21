# convert3.py
# A program that convert Celsius temps to Fahrenheit and prints a table
# redone by donovan Adams
def main():
    print "This is a program that converts Celcius to  Fahrenheit."
    print "Here are the temperatures every 10 degrees"
    print " ____________________"
    for i in [10,20,30,40,50,60,70,80,90,100]:
        celsius = i
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print "The temperature is", fahrenheit, "degrees Fahrenheit."
        i = i + 10
main()
