from ast import For
from colorama import Fore
import random
from aggregate_best import *

f = open("words/valid_5_letter.txt", 'r')
valid = []
while True:
    word = f.readline()
    if not word:
        break
    valid.append(word.rstrip())

f.close()

l_100 = [1, 2, 3, 4]
l_1000 = [1, 2, 3]
sol1 = Aggregate_best()
rankList = sol1.find_average_dict("outputs/5_letter/output_1000_", l_1000)

print(Fore.BLUE+'WORDLE..')
print(Fore.RESET)
n = len(valid)
target = valid[random.randint(0, n)]
#target = 'crepe'
# print(target)
guess = 0
a, b, c = {}, {}, []


def predict(a, b, c):
    predicted = []
    if len(a) > 0 or len(b) > 0 or len(c) > 0:
        for i in valid:
            a1 = 1
            b1 = 1
            c1 = 1
            for j in a:
                if i[j] != a[j]:
                    a1 = 0
                    break
            for j in b:
                temp = b[j]

                for k in temp:
                    if k in i:
                        if i[j] == k:
                            b1 = 0
                            break
                    else:
                        b1 = 0
                        break
                ''' if j not in i:
                    b1 = 0
                    break '''
            for j in c:
                if j in i:
                    c1 = 0
                    break
            # print(a1, b1, c1)
            if a1 and b1 and c1:
                # print(i)
                predicted.append(i)

    print(sorted(predicted))
    print(f"Probabilty - {len(predicted)}/{n}")
    minRank = 10000
    for word in sorted(predicted):
        temp = rankList.index(word)
        if temp < minRank:
            minRank = temp
    print(f"Suggested Word - {rankList[minRank]}")


def check(word):
    print(" "*13, end='')
    global target
    test = [i for i in target]
    for i in range(5):
        if word[i] == test[i]:
            test[i] = '_'
            print(Fore.GREEN+word[i], end='')
            if i not in a:
                a[i] = word[i]
        elif word[i] in test:
            if word[i] not in b:
                b[i] = [word[i]]
            else:
                b[i].append(word[i])
            print(Fore.YELLOW+word[i], end='')

        else:
            if word[i] not in c:
                c.append(word[i])
            print(Fore.WHITE+word[i], end='')
    print(Fore.WHITE)
    print(a, b, c, sep='\n')


while guess < 6:
    if guess > 0:
        h = int(input('Hint - '))
        if h == 1:
            predict(a, b, c)
    inp = input('Guess - ')
    if inp == target:
        print('Congrats the word is ', end='')
        print(Fore.CYAN+target)
        print(Fore.RESET)
        break
    check(inp)

    guess += 1
if guess > 5:
    print("The word is ", end="")
    print(Fore.RED+target)
    print(Fore.RESET)
