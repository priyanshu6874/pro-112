import os;
import shutil;

from_dir="C:/Users/user/Downloads"
to_dir="C:/Users/user/Documents/Document_Files"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    root,ext=os.path.splitext(file)

    if ext =="":
        continue
    if ext in [".txt",".doc",".docx",".pdf"]:
        path1=from_dir+"/"+file
        path2=to_dir+"/"+"pdf"
        path3=to_dir+"/"+"pdf"+"/"+file

        if os.path.exists(path2):
            print("moving "+file+"....")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving "+file+"....")
            shutil.move(path1,path3)