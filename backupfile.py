import os
import shutil
import time
def main():
    deletedfoldercount=0
    deletedfilescount=0
    path="C:\\Users\\91706\\Desktop\\atmproject\\example"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for routefolder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(routefolder):
                remove_folder(routefolder)
                deletedfoldercount+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(routefolder,folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedfoldercount+=1
                for file in files:
                    file_path=os.path.join(routefolder,file)
                    if seconds >= get_file_or_folder_age (file_path):
                        remove_file(file_path)
                        deletedfilescount+=1
        else:
                if seconds >= get_file_or_folder_age(path):
                    remove_file(path)
                    deletedfilescount+=1
    else:
        print(f'"{path}"is not found')
        deletedfilescount+=1
    print(f"total folders deleted: {deletedfoldercount}")
    print(f"total files deleted: {deletedfilescount}")
def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed succesfully")
    else:
        print("enable to delete the path"+path)
def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime
if __name__=="__main__":
    main()

