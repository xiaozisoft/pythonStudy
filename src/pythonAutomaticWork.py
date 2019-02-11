import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certatin'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrace and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)


def spam():
    eggs = 'spam local'
    print(eggs)


def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)


eggs = 'global'
bacon()
print(eggs)

print("\n#3.6 global key: \n")


def spam2():
    global eggs
    eggs1 = "spam"


eggs1 = 'global'
spam2()
print(eggs1)


print("\n#3.7 exception handling key: \n")


def spam36(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error : Invalid argument')


print(spam36(2))
print(spam36(12))
print(spam36(0))
print(spam36(1))

print("\n#3.7 exception handling key: \n")

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


print("\n#3.11 collatz sequence: \n")


def collatz(number):
        if number % 2 == 0:
            print(number / 2)
            return number / 2
        else:
            print(3 * number + 1, "\n")
            return 3 * number + 1


collatzData = int(input())

while collatzData != 1:
    collatzData = \
        collatz(collatzData)



