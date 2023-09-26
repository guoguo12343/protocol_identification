# -*-coding=utf-8 -*-
import matplotlib.pyplot as plt
if __name__=="__main__":
    with open("Bit_DARPA_2000_real_arp_data",'r') as filein:
        arp_ft_list=[]
        dataset=filein.readlines()
        for line in dataset:
            sum=0.0
            for i in line:
                if i=='0':
                    sum+=-1
                else:
                    sum+=1
            arp_ft_list.append(round(sum/len(dataset),4))

    with open("Bit_DARPA_2000_real_icmp_data",'r') as filein:
        icmp_ft_list=[]
        dataset=filein.readlines()
        for line in dataset:
            sum=0.0
            for i in line:
                if i=='0':
                    sum+=-1
                else:
                    sum+=1
            icmp_ft_list.append(round(sum/len(dataset),4))

    with open("Bit_DARPA_2000_real_http_data",'r') as filein:
        http_ft_list=[]
        dataset=filein.readlines()
        for line in dataset:
            sum=0.0
            for i in line:
                if i=='0':
                    sum+=-1
                else:
                    sum+=1
            http_ft_list.append(round(sum/len(dataset),4))
    plt.scatter(range(1,len(arp_ft_list)+1),arp_ft_list,c='r',marker='x',label="arp")
    plt.scatter(range(1,len(icmp_ft_list)+1),icmp_ft_list,c='b',marker='o',label="icmp")
    plt.scatter(range(1,len(http_ft_list)+1),http_ft_list,c='g',marker='s',label="http")
    plt.title("arp-icmp-http-Symbol frequency")
    plt.ylabel('Symbol frequency value')
    plt.xlabel('Protocol frame number')
    plt.legend()
    plt.show()