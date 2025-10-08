""" import random
number=random.randint(1, 10)
print("guess a number from 1-10")
while number:
    guess = int(input("Choose a number"))
    if guess < number:
        print("Try again")
    elif guess > number:
        print("Try again")
    elif guess == number: 
        print("Congratulations!") """








""" def lang(x):
    t = 0
    s = 0
    for char in x:
        if char == "t" or char =="T":
            t+=1    
        elif char == "s" or char =="S":
            s+=1     
        if t > s:
            print("Eng")
        else:
            print("french")    
    lang("Cadee stole the capybara from Zi. Also Mason is the worst")

    def spaces(y,t):

spaces("CCC..", ".C.C.C") """