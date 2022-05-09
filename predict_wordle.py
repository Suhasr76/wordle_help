from ast import For
from colorama import Fore
import colorama
import random
from aggregate_best import *

f = open("valid.txt", 'r')
valid = []
while True:
    word = f.readline()
    if not word:
        break
    valid.append(word.rstrip())

f.close()

# print(valid)

''' f1 = open('valid.txt', 'w')


for i in valid:
    f1.write(i+'\n') '''


# print(target)

a, b, c = {}, {}, []
global glo_flag
glo_flag = False

# dependencies

l_100 = [1, 2, 3, 4]
l_1000 = [1, 2, 3]
sol1 = Aggregate_best()
rankList = sol1.find_average_dict("output_1000_", l_1000)


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
    if len(predicted) == 1:
        print(f"Answer - {predicted[0]}")
        glo_flag = True
    print(sorted(predicted))
    minRank = 10000
    for word in sorted(predicted):
        temp = rankList.index(word)
        if temp < minRank:
            minRank = temp
    print(f"Probabilty - {len(predicted)}/{len(valid)}")
    # print(minRank)
    print(f"Suggested Word - {rankList[minRank]}, minRank - {minRank}")


'''

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
                b.append(word[i])
            print(Fore.YELLOW+word[i], end='')

        else:
            if word[i] not in c:
                c.append(word[i])
            print(Fore.WHITE+word[i], end='')
    print(Fore.WHITE)
    print(a, b, c, sep='\n') '''


inp = 1
while inp:

    a1 = [(i) for i in input('Green {pos letter} - ').split(' ')]
    # a2 = [i for i in input('a2 - ').split(" ")]
    b1 = [(i) for i in input('yellow {pos letter} - ').split(' ')]
    c1 = [i for i in input('Grey {letter} - ').split(' ')]
    print(a1, b1, c1)
    if len(a1) > 1:
        for i in range(0, len(a1), 2):
            # print(i)
            if int(a1[i]) not in a:
                a[int(a1[i])] = a1[i+1]
    if len(b1) > 1:
        for i in range(0, len(b1), 2):
            # print(i)

            if int(b1[i]) not in b:
                b[int(b1[i])] = [b1[i+1]]
            else:
                b[int(b1[i])].append(b1[i+1])
        ''' for i in b1:
            if i not in b:
                b.append(i) '''
    if len(c1) > 0 and '' not in c1:
        for i in c1:
            if i not in c:
                f = True
                for j in b:
                    if i in b[j]:
                        f = False
                        break
                if f:
                    c.append(i)
    print(a, b, c)
    if glo_flag:
        break
    predict(a, b, c)
