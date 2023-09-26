# -*- coding=utf-8 -*-
if __name__=="__main__":
    with open("real_LOG_data") as filein:
        with open("tmp_log",'w') as fileout:
            dataset=filein.readlines()
            for line in dataset:
                if line.startswith("323"):
                    fileout.write(line)
            for line in dataset:
                if line.startswith("504"):
                    fileout.write(line)
            for line in dataset:
                if line.startswith("313"):
                    fileout.write(line)
