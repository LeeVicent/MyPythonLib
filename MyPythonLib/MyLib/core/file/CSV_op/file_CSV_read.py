#coding  = utf-8

#return list of list  #返回二维数组
def file_CSV_read_list(file_name):
    if os.path.isfile(file_name):
        fin = open(file_name)                  
        temp_lsit = [x.rstrip().split(',') for x in fin]   #temp_list is an list of str(field)
        return temp_lsit
    else:
        print(file_name + "doesn't exit!")