# avg2.py
# this program takes three a=exam score entered for the user and converts them to an average
# Multiple input Practice
def main():
    print "This program computes the average of three exam scores."
    score1, score2, score3 = input("Enter three scores separated by a comma: ")
    average = (score1 + score2 +score3) / 3.0
    print "The average of the scores is:", average
main()
