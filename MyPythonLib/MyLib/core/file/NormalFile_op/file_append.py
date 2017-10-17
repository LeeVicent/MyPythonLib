#coding = utf-8 

def file_append_str(file_name, append_str):
    if os.path.isfile(file_name):
        infile = open(file_name, 'a')  
        infile.write(append_str + "\n")
        print("str \""+ append_str + "\" append success!")
        infile.close

    else:
        print(file_name + "doesn't exit!")

