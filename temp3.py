# import os
# import string
# import my_sftp_part
# import shutil
# import zipfile
# import gzip
# import py7zr


# import zipfile
#
# with zipfile.ZipFile('./04038031/2020-03-02T164832_VeeamBackupLogs.zip', 'r') as zip_ref:
#     zip_ref.extractall('./04038031/2020-03-02T164832_VeeamBackupLogs')
#
# os.remove('./04038031/2020-03-02T164832_VeeamBackupLogs.zip')


# def dyrectory_list(path):
#     list_of_cases_local = []
#     for folderNmae in os.listdir(path):
#         if folderNmae.isdigit() and os.path.isdir(folderNmae):
#             list_of_cases_local.append(folderNmae)
#     return list_of_cases_local
#
#
# def dyrectory_remove(list_of_cases_sf, list_of_cases_local):
#     for i in range(len(list_of_cases_local)):
#         if list_of_cases_local[i] not in list_of_cases_sf:
#             print(i)
#             # shutil.rmtree('.' + '/' + i)

# def file_extract(path):
#     l1=os.listdir()
#     for i in l1:
#         if i.endswith('filepart'):
#             with py7zr.SevenZipFile('i', mode='r') as z:
#                 z.extractall(i.rstrip('.filepart'))
#             # with gzip.open('i', 'rb') as f_in:
#             #     with open(i.rstrip('.filepart'), 'wb') as f_out:
#             #         shutil.copyfileobj(f_in, f_out)
#             # with zipfile.ZipFile(i, 'r') as zip_ref:
#             #     zip_ref.extractall(i.rstrip('.zip'))
#             # # os.remove(local_path)
#
#
#
# file_extract('.')


# def validate(value, validator):
#     try:
#         return validator(value)
#     except Exception as e:
#         raise ValueError('Invalid value: %s' % value) from e
#
#
# def validator(value):
#     if len(value) > 10:
#         raise ValueError("Value can't exceed 10 characters")
#
#
# try:
#     validate(False, validator)
# except Exception as e:
#     print(type(e))


# import os
# for folderName, subfolders, filenames in os.walk('.'):
#     print('The current folder is ' + folderName)
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)
#     print('')

# import os
# for folderName, subfolders, filenames in os.walk('.'):
#     # print('The current folder is ' + folderName)
#     # for subfolder in subfolders:
#     #     pass
#         # print(folderName + '/' + subfolder)
#     for filename in filenames:
#         print(folderName + '/'+ filename)
#     # print('')


def func():
    pass

print(func)