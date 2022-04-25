import time,cv2,random,dropbox
startTime=time.time()

def takeSnapshot():
    number=random.randint(0,1000)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    videoCaptureObject.release()
    return imageName

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
            
        print('Your file has been uploaded to Dropbox')   

def main():
    access_token = 'sl.BGb_TPvCSp2J7g-v7OIIOtzzHJdSQ89cQd8_4UEshLx16iDBClIBD3ZJhmRuSP0FApX57iBY0Au2MLV6_NHmH-4-4d1dTznpCnGHloG1Lge4LEO94IY35oISVAt4qHFJTYMRuXKjf7CW'
    transferData = TransferData(access_token)

    file_from = takeSnapshot()
    file_to = input('Enter the folder name where you want to upload your images: ')
    file_to = '/'+file_to+'/'+file_from

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()