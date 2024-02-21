print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
run = input("Enter the problem you want to run: ")
run = int(run)

if run == 1:
    # your code for problem 1 goes here
    # 1. Write a program that prints out the numbers 1 to 1000
    print("Running problem 1")
    for i in range(1,1001):
        print(i)
if run == 2:
    # your code for problem 2 goes here
    # 2. Write a program that prints out the odd numbers between 1 and 1000
    print("Running problem 2")
    for i in range(1,1001, 2):
        print(i) 

if run == 3:
    # your code for problem 3 goes here
    # 3. Write a program that prints out the numbers between 0 and 1000 that are divisible by 3
    print("Running problem 3")
    for i in range(0, 1001, 3):
        print(i) 

if run == 4:
    # your code for problem 4 goes here
    # 4. Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5
    print("Running problem 4")
    for i in range(1, 1001):
        if i % 3 == 0 or i % 5 ==0: # use this when you want to divide by 2 variables
            print(i)
if run == 5:
    # your code for problem 5 goes here
    # 5. Write a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200. (+10 points) Extra credit if the programs asks again if the number is less than 200 
    print("Running problem 5")
    num=int(input("Enter a number GREATER than 200: "))
    for i in range(1, num):
        if i % 11 == 0 or i % 13 == 0:
            print(i)
            num1 = int(input("Enter a number LESS than 200: "))
            for i in range(1, num):
                if i % 11 == 0 or i % 13 == 0:
                    print(i)
if run == 6:
    # your code for problem 6 goes here
    # 6. Write a program that prints out each letter of a string line by line (+5 points)
    print("Running problem 6")
    string=input("Enter a word: ")
    for l in range(0,len(string)):
        print(string[l])
if run == 7:
    # your code for problem 7 goes here
    # 7. Write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 letters long. (+10 points)
    print("Running problem 7")
    string=input("Enter a word that is 10 letters long or more: ")
    for l in range(0,len(string), 2):
        print(string[l])
if run == 8:
    # your code for problem 8 goes here
    # 8. Write a program that rolls 1000 dice and prints out the number of times each number was rolled. (+15 points)
    print("Running problem 8")
    import random
    ones=0
    twos=0
    threes=0
    fours=0
    fives=0
    sixes=0
    for rolls in range(1,1000):
        dice = random.randint(1,6)
        if dice == 1:
            ones += 1
        elif dice == 2:
            twos += 1
        elif dice == 3:
            threes += 1
        elif dice == 4:
            fours += 1
        elif dice == 5:
            fives += 1
        else:
            sixes += 1
        print(rolls * 1)
        print(f"1's were rolled {ones} times, 2's were rolled {twos} times, 3's were rolled {threes} times, 4's were rolled {fours} times, 5's were rolled {fives} times, 6's were rolled {sixes} times")
if run == 9:
    # your code for problem 9 goes here
    # 9. Write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not. (+15 points)
    num = int(input("enter your  number: "))
    if num % 1 == 0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
        

if run == 10:
    # your code for problem 10 goes here
    # 10. Write a program that prints out the prime numbers less than 1000. (+20 points)
    for num in range(1,1001):
        if num>1:
            for i in range(2, num):
                if (num%i)==0:
                    break
                else:
                    print(f"{num}, i've worked on this question for 6 days and no youtuber could help me be so fr")
        
        

