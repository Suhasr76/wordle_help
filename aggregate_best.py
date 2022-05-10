
l_100 = [1, 2, 3]
l_1000 = [1, 2, 3]


class Aggregate_best:

    def find_average_dict(self, prefix, l_test):
        average = []
        finalFilename = prefix+"final.txt"

        dict = {}
        for number in l_test:
            filename = prefix+str(number)+'.txt'
            f = open(filename, 'r')
            while True:
                line = f.readline()
                if not line:
                    break
                attributes = line.rstrip().split("\t")
                if attributes[0] in dict:
                    dict[attributes[0]].append(attributes[1:])
                else:
                    dict[attributes[0]] = [attributes[1:]]
                # print(attributes)
        ''' for i in dict:
            print(i, dict[i]) '''
        final_dict = {}
        for i in dict:
            temp = dict[i]
            valid, invalid = 0, 0
            c1, c2 = 0, 0
            for per in temp:
                valid += round(float(per[0])*float(per[1]), 4)
                c1 += int(per[0])
                if per[2] != 'none':
                    invalid = round(float(per[2])*float(per[3]), 4)
                    c2 += int(per[2])
            final_dict[i] = [c1, round(valid/c1, 4)]
            if c2 != 0:
                final_dict[i].extend([c2, round(invalid/c2, 4)])

        final_list = sorted(dict, key=lambda x: [final_dict[x][1]])

        final = open(finalFilename, "w")
        for i in final_list:
            string = i+"\t"+"\t".join([str(i) for i in final_dict[i]])
            #print('s', string)
            final.write(string+'\n')

        return final_list


#sol = Aggregate_best()
#final_list = sol.find_average_dict("outputs/6_letter/output_100_", l_100)
# print(*final_list)
