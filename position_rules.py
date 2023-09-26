# -*- coding=utf-8 -*-
def turn(tuplea):
    return (('0x'+tuplea[0][0][0],'0x'+tuplea[0][0][1]),tuplea[0][1]),tuplea[1]
if __name__=="__main__":
    gramdic={}
    with open("DARPA_2000_real_http_data", 'r') as filein:
        dataset=filein.readlines()
        for line in dataset:
            for i in range(len(line.strip())-8+1):
                gram=line.strip()[i:i+8]
                if gram in gramdic:
                    gramdic[gram]+=1
                else:
                    gramdic[gram]=1
        gram_list=sorted(gramdic.items(),key=lambda x:x[1],reverse=True)
        gram_list=[x for x in gram_list if x[1]>=250]#Jaccard系数筛选
        result={}
        for p in gram_list:
            result[p[0]]=0
        for line in dataset:
            for p in gram_list:
                if p[0] in line:
                    result[p[0]]+=1
        result_set=sorted(result.items(),key=lambda x:x[1],reverse=True)
        result_set_two = []
        for i in result_set:
            if i[1] > 400:
                result_set_two.append(i)
        association = {}
        for line in dataset:
            for i in range(len(result_set_two) - 1):
                for j in range(i + 1, len(result_set_two)):
                    pos = line.find(result_set_two[i][0])
                    pos1 = line.find(result_set_two[j][0])
                    if pos != -1 and pos1 != -1:
                        if pos > pos1:
                            try:
                                association[((result_set_two[j][0], result_set_two[i][0]), pos - pos1)] += 1
                            except:
                                association[((result_set_two[j][0], result_set_two[i][0]), pos - pos1)] = 1
                        elif pos < pos1:
                            try:
                                association[((result_set_two[i][0], result_set_two[j][0]), pos1 - pos)] += 1
                            except:
                                association[((result_set_two[i][0], result_set_two[j][0]), pos1 - pos)] = 1
        print [x for x in map(turn, sorted(association.items(), key=lambda x: x[1], reverse=True)) if x[1]>400]

