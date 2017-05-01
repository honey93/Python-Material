import os

filelist = os.listdir(r"F:\Photos\Kodinar Pics")
print(filelist)
saved_path = os.getcwd()
os.chdir(r"F:\Photos\Kodinar Pics")
for file_name in filelist:
        os.rename(file_name,file_name.translate(None,"W"))
#print(filelist)
os.chdir(saved_path)        

    
