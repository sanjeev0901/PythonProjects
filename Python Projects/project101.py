import dropbox,os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relativePath = os.path.relpath(local_path, file_from)
                dbxPath=os.path.join(file_to,relativePath)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dbxPath, mode=WriteMode.overwrite)
        print('Your files and folders has been uploaded to Dropbox')
        
def main():
    access_token = 'sl.BGRsSB7l01HW1e0LiNkBub0aVz8thYjg_VwDgztrgp_nUwsD_-UpwK_6kohUjQJbvCVQbVA8rJO1-BRQv5-hGZ7YopRP7faZMHtQFZv-gu1aDNmWQIl3mFevMwpCsvegLi6dHrtzxyXv'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to upload: ')
    file_to = input('Enter the full path of folder or file in dropbox: ')

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
