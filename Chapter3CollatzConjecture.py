#!Python3

#Read about the Collatz conjecture here: https://en.wikipedia.org/wiki/Collatz_conjecture

try:
    def collatz(number):
        while number != 1:
            if number%2==0:
                number = number//2
                print (number)
            else:
                number = 3*number+1
                print (number)
    collatz(int(input()))
except ValueError:
    print("Only numbers allowed.")
