# -*- coding=utf-8 -*-
# def shift_gramlist(gramlist):
#     total=sum([x[1] for x in gramlist])
#     result=[]
#     for i in gramlist:
#         result.append((i[0],round(float(i[1])/total),4))
#     return result

import matplotlib.pyplot as plt

def shift_list(numlist):
    return map(lambda x:float(x)/sum(numlist),numlist)


class Jaccard(object):
    def __init__(self,lista,listb):
        self.lista=lista
        self.listb=listb

    def get_Jaccard(self):
        resulta = []
        resultb = []
        length=min(len(self.lista),len(self.listb))
        while length>1:
            tmplista=[x[1] for x in self.lista][0:length]
            tmplistb = [x[1] for x in self.listb][0:length]
            # tmplista = shift_list(tmplista)
            # tmplistb = shift_list(tmplistb)
            tmpsum=0
            for k in range(length):
                tmpsum+=tmplista[k]*tmplistb[k]
            protocol_jaccard = float(tmpsum) / (
                        sum(map(lambda x: x * x, tmplista)) + sum(map(lambda x: x * x, tmplistb)) - tmpsum)
            resulta.append(min(tmplista[length-1],tmplistb[length-1]))
            resultb.append(protocol_jaccard)
            length-=1
        return resulta, resultb



if __name__=="__main__":
    with open("real_LOG_data", 'r') as filein:
        dataset=filein.readlines()
        length=len(dataset)
        dataseta=dataset[0:length/2]
        datasetb=dataset[length/2:]
    n=input("N-gram number:")
    # threshold=map(int,raw_input("please input the thresholds(spliter with space):").strip().split())
    gramdica={}
    gramdicb={}
    for line in dataseta:
        for i in range(len(line.strip())-n+1):
            gram=line.strip()[i:i+n]
            if gram in gramdica:
                gramdica[gram]+=1
            else:
                gramdica[gram]=1
    gram_lista = sorted(gramdica.items(), key=lambda x: x[1], reverse=True)
    for line in datasetb:
        for i in range(len(line.strip())-n+1):
            gram=line.strip()[i:i+n]
            if gram in gramdicb:
                gramdicb[gram]+=1
            else:
                gramdicb[gram]=1
    gram_listb = sorted(gramdicb.items(), key=lambda x: x[1], reverse=True)
    jaccard=Jaccard(gram_lista,gram_listb)
    X=jaccard.get_Jaccard()[0]
    Y=jaccard.get_Jaccard()[1]
    plt.title("LOG "+str(n/2)+"-gram")
    plt.xlabel('threshold')
    plt.ylabel('protocol_Jaccard')
    plt.plot(X,Y)
    plt.show()