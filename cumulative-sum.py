# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt

if __name__=="__main__":
    with open("Bit_DARPA_2000_real_arp_data",'r') as filein:
        arp_cs_list=[]
        dataset=filein.readlines()
        for line in dataset:
            line=line.strip()
            length=len(line)
            tmplist1=[]
            tmplist2=[]
            sum1=0
            sum2=0
            for i in range(length):
                if line[i]=='0':
                    sum1+=-1
                else:
                    sum1+=1
                if line[length-i-1]=='0':
                    sum2+=-1
                else:
                    sum2+=1
                tmplist1.append(sum1)
                tmplist2.append(sum2)
            t1=float(sum(tmplist1))/len(tmplist1)
            t2=float(sum(tmplist2))/len(tmplist2)
            arp_cs_list.append(round((t2-t1)/(t1+t2),4))

    with open("Bit_DARPA_2000_real_icmp_data",'r') as filein:
        icmp_cs_list=[]
        dataset=filein.readlines()
        for line in dataset:
            line=line.strip()
            length=len(line)
            tmplist1=[]
            tmplist2=[]
            sum1=0
            sum2=0
            for i in range(length):
                if line[i]=='0':
                    sum1+=-1
                else:
                    sum1+=1
                if line[length-i-1]=='0':
                    sum2+=-1
                else:
                    sum2+=1
                tmplist1.append(sum1)
                tmplist2.append(sum2)
            t1=float(sum(tmplist1))/len(tmplist1)
            t2=float(sum(tmplist2))/len(tmplist2)
            icmp_cs_list.append(round((t2-t1)/(t1+t2),4))


    with open("Bit_DARPA_2000_real_http_data",'r') as filein:
        http_cs_list=[]
        dataset=filein.readlines()
        for line in dataset:
            line=line.strip()
            length=len(line)
            tmplist1=[]
            tmplist2=[]
            sum1=0
            sum2=0
            for i in range(length):
                if line[i]=='0':
                    sum1+=-1
                else:
                    sum1+=1
                if line[length-i-1]=='0':
                    sum2+=-1
                else:
                    sum2+=1
                tmplist1.append(sum1)
                tmplist2.append(sum2)
            t1=float(sum(tmplist1))/len(tmplist1)
            t2=float(sum(tmplist2))/len(tmplist2)
            http_cs_list.append(round((t2-t1)/(t1+t2),4))

    plt.scatter(range(1, len(arp_cs_list) + 1), arp_cs_list, c='r', marker='x', label="arp")
    plt.scatter(range(1, len(icmp_cs_list) + 1), icmp_cs_list, c='b', marker='x', label="icmp")
    plt.scatter(range(1, len(http_cs_list) + 1), http_cs_list, c='g', marker='x', label="http")
    plt.title("arp-icmp-http-Cumulative sum")
    plt.ylabel('Cumulative sum')
    plt.xlabel('Protocol frame number')
    plt.legend()
    plt.show()
