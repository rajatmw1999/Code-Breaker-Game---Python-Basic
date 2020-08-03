import random
n = random.randint(100,999)
print(n)

third = n%10
n=(n-third)/10
second = int(n%10)
n=(n-second)/10
first = int(n)

def check():
    val = input("Guess the Number: ")
    val = int(val)
    thirdu = val%10
    val=(val-thirdu)/10
    secondu = int(val%10)
    val=(val-secondu)/10
    firstu = int(val)

    if(firstu==first) and (secondu == second) and (thirdu == third):
        return "Woooohoooo!! You won!"
    elif(firstu == first) or (secondu == second) or (thirdu == third):
        print("You are close buddy!")
        check()
    elif(firstu == second) or (firstu == third) or (secondu == first) or (secondu == third) or (thirdu==first) or (thirdu==second):
        print("Wrong positions, though close!")
        check()
    else:
        print("Can your guess be any more wrong.")
        check()


result = check()
print(result)