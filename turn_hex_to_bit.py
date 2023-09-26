# -*-coding=utf-8 -*-

def decode_hex(stra):
    DECODE_LIST=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    if stra in "0123456789":
        return DECODE_LIST[int(stra)]
    elif stra in "abcdef":
        return DECODE_LIST[ord(stra)-87]
def decode_line(line):
    tmp=[]
    for i in line:
        tmp.append(decode_hex(i))
    return ''.join(tmp)

if __name__=="__main__":
    with open("DARPA_2000_real_arp_data",'r') as filein:
        with open("Bit_DARPA_2000_real_arp_data",'w') as fileout:
            for line in filein.readlines():
                fileout.write(decode_line(line.strip()))
                fileout.write('\n')
