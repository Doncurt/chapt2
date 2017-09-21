# convert2.py
# A program that convert Celsius temps to Fahrenheit and also executes this 5 mintes in a loop to collect diffrent temps
# redone by donovan Adams
def main():
    print "this is a program that converts Celcius to  fahrenheit"
    for i in range(5):
        celsius = input("What is the Celsius temperature? ")
        fahrenheit = 9.0 / 5.0 * celsius + 32
        print "The temperature is", fahrenheit, "degrees Fahrenheit."
    print "Thank you for computing with me!"
main()
