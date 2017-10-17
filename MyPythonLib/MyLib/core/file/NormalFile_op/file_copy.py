#coding = utf-8 
import os

def file_copy(infile_name, outfile_name):
    if os.path.isfile(infile_name):
        infile = open(infile_name, 'r')
        outfile = open(outfile_name, 'w')

        outfile.writelines([x for x in infile])   #测试

        infile.close()
        outfile.close()

    else:
        print(infile_name + "doesn't exist!")