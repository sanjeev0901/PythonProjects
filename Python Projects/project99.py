#Program to delete files older than x days.
import datetime, os, shutil


print("Hi, ", os.environ.get('USERNAME'))

mypath =input("Enter the path to delete files: ")
days = int(input("Enter the number of days to delete files: "))
today = datetime.datetime.today() 
total_files = 0
total_folder = 0  

def delFilesAndFolders(mypath,days):
    if  os.path.exists(mypath):
        for root, directories, files in os.walk(mypath):
            for fname in files:
                fullname = os.path.join(root, fname)
                my_fn_delete(fullname, days)

            for fname in directories:
                fullname = os.path.join(root, fname)
                my_fn_delete(fullname, days)
            print(f"Total number  of files removed are: {total_files}. \n"
          f"Total number of folders removed are: {total_folder}")
    else:
        print("Path does not exist")
        
def my_fn_delete(objname, days):
        # returns file created time in seconds
        time_modified = os.stat(objname).st_ctime  
        # convert seconds to date time format
        file_created_time = datetime.datetime.fromtimestamp(time_modified)
        # check the age of the file from creation date till today
        file_age = (file_created_time - today).days
        # checking if file is more than x days old
        # or not if yes then remove them
        if file_age <= -days:
            if os.path.isfile(objname):
                os.remove(objname)
                total_files += 1
            elif os.path.isdir(objname):
                shutil.rmtree(objname)
                total_folder += 1

    
delFilesAndFolders(mypath,days)