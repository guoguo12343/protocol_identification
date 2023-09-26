# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
def get_line_rt(line):
    patterns0={}
    patterns1={}
    tmp=[line[0]]
    for i in line[1:]:
        if i in tmp:
            tmp.append(i)
        else:
            pattern=''.join(tmp)
            if i=='0':
                if pattern in patterns1:
                    patterns1[pattern]+=1
                else:
                    patterns1[pattern]=1
            else:
                if pattern in patterns0:
                    patterns0[pattern]+=1
                else:
                    patterns0[pattern]=1
            tmp=[i]
    if tmp!=[]:
        pattern = ''.join(tmp)
        if i == '0':
            if pattern in patterns1:
                patterns1[pattern] += 1
            else:
                patterns1[pattern] = 1
        else:
            if pattern in patterns0:
                patterns0[pattern] += 1
            else:
                patterns0[pattern] = 1
    a=sum([len(x)*patterns1[x] for x in patterns1])
    b = sum([len(x) * patterns0[x] for x in patterns0])
    return round((float(a)-b)/(a+b),4)

if __name__=="__main__":
    with open("Bit_DARPA_2000_real_arp_data",'r') as filein:
        arp_rt_list=[]
        dataset=filein.readlines()
        for line in dataset:
            arp_rt_list.append(get_line_rt(line.strip()))

    with open("Bit_DARPA_2000_real_icmp_data",'r') as filein:
        icmp_rt_list=[]
        dataset=filein.readlines()
        for line in dataset:
            icmp_rt_list.append(get_line_rt(line.strip()))

    with open("Bit_DARPA_2000_real_http_data",'r') as filein:
        http_rt_list=[]
        dataset=filein.readlines()
        for line in dataset:
            http_rt_list.append(get_line_rt(line.strip()))

    plt.scatter(range(1, len(arp_rt_list) + 1), arp_rt_list, c='r', marker='x', label="arp")
    plt.scatter(range(1, len(icmp_rt_list) + 1), icmp_rt_list, c='b', marker='x', label="icmp")
    plt.scatter(range(1, len(http_rt_list) + 1), http_rt_list, c='g', marker='x', label="http")
    plt.title("arp-icmp-http-Run length")
    plt.ylabel('Run length value')
    plt.xlabel('Protocol frame number')
    plt.legend()
    plt.show()
