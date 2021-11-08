import dropbox
import os
from dropbox.files import WriteMode

class TransferData(object):
    def __init__(self, access_token):
        self.accessToken = access_token


    def upload_file(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                path = os.path.join(root, filename)

                rePath = os.path.relpath(path, fileFrom)
                dropboxPath = os.path.join(fileTo, rePath)

                with open(path, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))



def main():
    accessToken = 'UJFQxNNueVcAAAAAAAAAAY-6E1rLZxFqEbpPgIxkjxehZzXWh7gFPdRskp-wwJ0I'
    fileFrom = input("Enter the file to transfer from : ")
    fileTo = input("enter the full path of where to upload : ")

    transferData = TransferData(accessToken)
    transferData.upload_file(fileFrom, fileTo)

main()