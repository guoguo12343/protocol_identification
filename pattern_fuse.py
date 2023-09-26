# -*- coding=utf-8 -*-
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
        gram_list=[x for x in gram_list if x[1]>=800]#Jaccard系数筛选
        result={}
        for p in gram_list:
            result[p[0]]=0
        for line in dataset:
            for p in gram_list:
                if p[0] in line:
                    result[p[0]]+=1
        result_set=sorted(result.items(),key=lambda x:x[1],reverse=True)
        print result_set