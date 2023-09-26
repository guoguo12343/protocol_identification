# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import math
import pandas as pd
import numpy as np
from scipy import stats
def get_r2_scipy(x, y):
    _, _, r_value, _, _ = stats.linregress(x, y)
    return r_value**2

n=input("please input a number for the ngram:")
print "ARP协议拟合优度："
legends = []
for num in range(2,n+1,2):
    gramdic = {}
    with open("DARPA_2000_real_arp_data", 'r') as filein:
        for line in filein.readlines():
            for i in range(len(line.strip())-num+1):
                gram=line.strip()[i:i+num]
                if gram in gramdic:
                    gramdic[gram]+=1
                else:
                    gramdic[gram]=1
        gram_list=sorted(gramdic.items(),key=lambda x:x[1],reverse=True)
        X=map(math.log,[item for item in range(1,len(gram_list)+1)])
        Y=map(math.log,[x[1] for x in gram_list])
        legends.append(str(num/2)+"-gram")
        plt.plot(X,Y)
        plt.title("LOG N-gram")
        plt.xlabel('Number of occurrences(log)')
        plt.ylabel('Rank number(log)')
        print num/2,"gram R2:",round(get_r2_scipy(X,Y),4)
        # gx=pd.Series(X)
        # gy=pd.Series(Y)
        # corr_gust=round(gx.corr(gy),4)
        # print num,"gram:",corr_gust
        # plt.scatter(X,Y)
plt.legend(legends)
plt.show()
