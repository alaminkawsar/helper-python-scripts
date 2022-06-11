# https://stackoverflow.com/a/61174372/17957276

'''Run this code on google colab'''

'''
Date: 11 June,20202
Code by Al Amin Kawsar
'''

'''Run this snipet on first colab's cell'''
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
my_drive = GoogleDrive(gauth)



'''Run this code snipet on second cell on colab'''
files_in_trash = my_drive.ListFile({'q': "trashed = true"}).GetList()
print(len(files_in_trash)," file to delete")
# print("total to delte ",len(files_in_trash))
for a_file in files_in_trash:
    # print the name of the file being deleted.
    print(f"the file {a_file['title']}, is about to get deleted permanently.")
    # delete the file permanently.
    a_file.Delete()