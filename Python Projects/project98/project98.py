import sys  
file1=input("Enter the name of the first file: ")
file2=input("Enter the name of the second file: ")

#swap the files data
def swapFileData(filename1,filename2):
    with open(sys. path[0]+'/'+filename1, 'r') as f1:
        data_a=f1.read()
    with open(sys. path[0]+'/'+filename2, 'r') as f2:
        data_b=f2.read()
    with open(sys. path[0]+'/'+filename1, 'w') as a:
        a.write(data_b)
    with  open(sys. path[0]+'/'+filename2, 'w') as b:
        b.write(data_a)
        
swapFileData(file1,file2); 
    