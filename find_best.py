import random
from aggregate_best import *


f = open("words/valid_6_letter.txt", 'r')
valid = []
while True:
    word = f.readline()
    if not word:
        break
    valid.append(word.rstrip())

f.close()

valid = sorted(valid)


l_100 = [1, 2, 3, 4]
l_1000 = [1, 2, 3]
sol1 = Aggregate_best()
#rankList = sol1.find_average_dict("outputs/5_letter/output_1000_", l_1000)


class Predict:
    def find_lists_dicts(self, predict, target, green, yellow, grey):
        ''' green = {}
        yellow = {}
        grey = [] '''
        correct = []
        for i in range(len(predict)):
            if predict[i] == target[i]:
                green[i] = predict[i]
                correct.append(i)
            else:
                if predict[i] in target:
                    for j in range(len(target)):
                        if predict[i] == target[j]:
                            if i in yellow:
                                yellow[i].append(predict[i])
                            else:
                                if i in green:
                                    if green[i] != predict[i]:
                                        yellow[i] = [predict[i]]
                                else:
                                    yellow[i] = [predict[i]]

                else:
                    grey.append(predict[i])
        return [green, yellow, grey]

    def predict(self, a, b, c):
        # print(a, b, c)
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
                if a1 and b1 and c1:
                    # print(i)
                    predicted.append(i)
        # if len(predicted) == 1:
            # print(f"Answer - {predicted[0]}")
            # glo_flag = True
            # print(sorted(predicted))
            # print(f"Probabilty - {len(predicted)}/{len(valid)}") ------------------------------------

        return sorted(predicted)

    def find_number_of_tries(self, predict, target, poss_list, count, history, a, b, c, valid_guess, max_guess):
        # print(predict, '->', end='')
        if len(poss_list) == 1:
            ''' for i in history:
                print(f"{i} -> ", end='')
            print(f"\nDone - Total tries->{count}") '''
            if count <= 6:
                valid_guess.append(count)
            else:
                max_guess.append(count)
            return
        # print(f"Try - {count}, Poss_list={len(poss_list)}")

        # print("check", a, b, c)
        a, b, c = self.find_lists_dicts(predict, target, a, b, c)
        poss_list = self.predict(a, b, c)

        ''' minRank = 10000
        for word in poss_list:

            temp = rankList.index(word)
            if temp < minRank:
                minRank = temp
        # print(minRank)
        new_predict = rankList[minRank] '''
        new_predict = poss_list[random.randrange(0, len(poss_list))]
        # print("New Predicted -", new_predict)
        # if len(poss_list) < 50:
        # print(poss_list)
        history.append(new_predict)
        self.find_number_of_tries(
            new_predict, target, poss_list, count+1, history, a, b, c, valid_guess, max_guess)

    def start_to_find_no_of_steps(self):
        f = open('outputs/6_letter/output_1000_3.txt', 'w')
        final = []
        for word in valid:
            count = 0
            valid_guess = []
            max_guess = []
            while count < 1000:
                # print(f"{word} ----------------")
                target = valid[random.randrange(0, len(valid))]
                a = {}
                b = {}
                c = []
                self.find_number_of_tries(
                    word, target, valid, 0, [word], a, b, c, valid_guess, max_guess)
                count += 1
                ''' if len(valid_guess) > 0 and len(max_guess) > 0:
                string = word + " " + " "+str(len(valid_guess)) + str(round(sum(valid_guess)/len(
                    valid_guess), 3)) + " "+str(len(max_guess))+" "+str(round(sum(max_guess)/len(max_guess), 3))+"\n"
                print(string)
                f.write(string) '''

            l = [word]
            if len(valid_guess) > 0:
                temp = round((sum(valid_guess)/len(valid_guess)), 3)
                l.extend([len(valid_guess), temp])
            else:
                l.extend(["none"])
            if len(max_guess) > 0:
                temp = round((sum(max_guess)/len(max_guess)), 3)
                l.extend([len(max_guess), temp])
            else:
                l.extend(["none"])
            final.append(l)
            string = "\t".join([str(i) for i in l])
            print(string)
            # f.write(string+"\n")
            count += 1

        final = sorted(final, key=lambda x: (x[2], x[1]))

        for line in final:
            string = "\t".join([str(i) for i in line])
            f.write(string+'\n')
        f.close()

        ''' predict = valid[random.randrange(0, len(valid))]
        target = valid[random.randrange(0, len(valid))]
        print(f"Main P-{predict} T-{target}")
        a = {}
        b = {}
        c = []
        self.find_number_of_tries(
            predict, target, valid, 0, [predict], a, b, c) '''


temp = Predict()
''' predicted = input("Predicted - ")
target = input("Target    - ")
a, b, c = temp.find_lists_dicts(predicted, target)
temp.predict(a, b, c) '''
temp.start_to_find_no_of_steps()
# print(temp.find_lists_dicts('labbc', 'aabcb'))
