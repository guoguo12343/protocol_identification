# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
def count_1(stra):
    return float(sum(map(int,list(stra))))/len(stra)
if __name__=="__main__":
    with open("Bit_DARPA_2000_real_arp_data",'r') as filein:
        arp_bl_list=[]
        dataset=filein.readlines()
        for line in dataset:
            line=line.strip()
            tmplist=[]
            while len(line)>32:
                tmplist.append(line.strip()[0:32])
                line=line[32:]
            k_set=map(count_1,tmplist)
            k_mean=sum(k_set)/len(k_set)
            arp_bl_list.append(sum(map(lambda x:(x-k_mean)*(x-k_mean),k_set))/(len(k_set)*k_mean*k_mean))

        with open("Bit_DARPA_2000_real_icmp_data", 'r') as filein:
            icmp_bl_list = []
            dataset = filein.readlines()
            for line in dataset:
                line = line.strip()
                tmplist = []
                while len(line) > 32:
                    tmplist.append(line.strip()[0:32])
                    line = line[32:]
                k_set = map(count_1, tmplist)
                k_mean = sum(k_set) / len(k_set)
                icmp_bl_list.append(
                    sum(map(lambda x: (x - k_mean) * (x - k_mean), k_set)) / (len(k_set) * k_mean * k_mean))


        with open("Bit_DARPA_2000_real_http_data", 'r') as filein:
            http_bl_list = []
            dataset = filein.readlines()
            for line in dataset:
                line = line.strip()
                tmplist = []
                while len(line) > 32:
                    tmplist.append(line.strip()[0:32])
                    line = line[32:]
                k_set = map(count_1, tmplist)
                k_mean = sum(k_set) / len(k_set)
                http_bl_list.append(
                    sum(map(lambda x: (x - k_mean) * (x - k_mean), k_set)) / (len(k_set) * k_mean * k_mean))

        plt.scatter(range(1, len(arp_bl_list) + 1), arp_bl_list, c='r', marker='x', label="arp")
        plt.scatter(range(1, len(icmp_bl_list) + 1), icmp_bl_list, c='b', marker='x', label="icmp")
        plt.scatter(range(1, len(http_bl_list) + 1), http_bl_list, c='g', marker='x', label="http")
        plt.title("arp-icmp-http-Intra-block frequency")
        plt.ylabel('Intra-block frequency')
        plt.xlabel('Protocol frame number')
        plt.legend()
        plt.show()