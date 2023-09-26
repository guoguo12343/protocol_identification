# -*- coding=utf-8 -*-
if __name__=="__main__":
    gramdic={}
    with open("DARPA_2000_real_http_data", 'r') as filein:
        dataset=filein.readlines()
        tmp1=[]
        tmp2=[]
        with open("tmp_http1",'w') as fileout:
            with open("tmp_http2",'w') as fileout2:
                for i in range(len(dataset)):
                    if i%2==0:
                        fileout.write(dataset[i])
                    else:
                        fileout2.write(dataset[i])