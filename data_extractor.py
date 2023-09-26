# -*- coding=utf-8 -*-

import json

class Data_extractor(object):
    def __init__(self):
        pass

    def get_arp_data_from_json(self,src_filename,des_filename,type):
        with open(src_filename,'r') as file1:
            with open(des_filename,type) as file2:
                load_dic=json.load(file1)
                for item in load_dic:
                    arp_data=item[u'_source'][u'layers'][u'arp_raw'][0]
                    file2.write(arp_data)
                    file2.write("\n")

    def get_http_data_from_json(self,src_filename,des_filename,type):
        with open(src_filename,'r') as file1:
            with open(des_filename,type) as file2:
                load_dic=json.load(file1)
                count=0
                for item in load_dic:
                    http_data=item[u"_source"][u'layers'][u'http_raw'][0]
                    file2.write(http_data)
                    file2.write("\n")
                    count+=1
                    if count==1000:
                        break
    def get_icmp_data_from_json(self,src_filename,des_filename,type):
        with open(src_filename,'r') as file1:
            with open(des_filename,type) as file2:
                load_dic=json.load(file1)
                for item in load_dic:
                    icmp_data=item[u'_source'][u'layers'][u'icmp_raw'][0]
                    file2.write(icmp_data)
                    file2.write("\n")

    def get_tcp_data_from_json(self,src_filename,des_filename,type):
        with open(src_filename,'r') as file1:
            with open(des_filename,type) as file2:
                load_dic=json.load(file1)
                for item in load_dic:
                    try:
                        icmp_data=item[u'_source'][u'layers'][u'tcp'][u'tcp.payload_raw'][0]
                        file2.write(icmp_data)
                        file2.write("\n")
                    except:
                        pass

    def get_log_data_from_json(self,src_filename,des_filename,type):
        with open(src_filename,'r') as file1:
            with open(des_filename,type) as file2:
                load_dic=json.load(file1)
                for item in load_dic:
                    log_data=item[u'_source'][u'layers'][u'ftp_raw'][0]
                    if len(log_data)<40:
                        continue
                    file2.write(log_data)
                    file2.write("\n")




if __name__=="__main__":
    data_extracor=Data_extractor()
    # data_extracor.get_arp_data_from_json("DARPA_2000_outside_arp.json","DARPA_2000_real_arp_data",'w')
    # data_extracor.get_arp_data_from_json("DARPA_2000_inside_arp.json","DARPA_2000_real_arp_data",'a')
    # data_extracor.get_http_data_from_json("DARPA_2000_outside_http.json", "DARPA_2000_real_http_data", 'w')
    # data_extracor.get_icmp_data_from_json("DARPA_2000_outside_icmp.json", "DARPA_2000_real_icmp_data", 'w')
    # data_extracor.get_http_data_from_json("2019_06_03_http.json","2019_06_03_real_http_data",'w')
    # data_extracor.get_arp_data_from_json("2019_06_03_arp.json", "2019_06_03_real_arp_data", 'w')
    # data_extracor.get_tcp_data_from_json("zello_tcp.json", "zello_real_tcp_data", 'w')
    # data_extracor.get_tcp_data_from_json("zello_1_tcp.json", "zello_real_tcp_data", 'a')
    # data_extracor.get_tcp_data_from_json("zello_2_tcp.json", "zello_real_tcp_data", 'a')
    # data_extracor.get_log_data_from_json("LOG.json", "real_LOG_data", 'w')
    # data_extracor.get_log_data_from_json("LOG1.json", "real_LOG_data", 'a')
    data_extracor.get_http_data_from_json("hit.json", "hit_data", 'w')