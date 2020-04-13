import pysftp
import os
import my_staff
import zipfile
import shutil
from urllib.parse import urlparse
import traceback

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

file_names = []
dir_names = []
un_name = []


def store_files_name(fname):
    file_names.append(fname)


def store_dir_name(dirname):
    dir_names.append(dirname)


def store_other_file_types(name):
    un_name.append(name)


def clear_files_dir_other():
    file_names.clear()
    dir_names.clear()
    un_name.clear()


def download_ftp(list_of_links):
    try:
        for i in list_of_links:
            clear_files_dir_other()
            sftp_link = urlparse(i)
            with pysftp.Connection(host=sftp_link.hostname, username=sftp_link.username, password=sftp_link.password,
                                   cnopts=cnopts) as sftp:
                print('Connection succesfully established ... ')
                sftp.cwd(r'/upload')
                directory_structure = sftp.walktree('.', store_files_name, store_dir_name, store_other_file_types)

                for item in file_names:
                    case_number = sftp_link.username.lstrip(('ftp'))
                    list_of_files = 'list_of_files.txt'
                    list_of_files_path = os.path.join('.', case_number, list_of_files)

                    attr = sftp.stat(item)
                    dic_remote = {}
                    dic_remote[item] = attr.st_mtime
                    print(attr.st_mtime, item)

                    local_path = ('.' + '/' + case_number + '/' + item)
                    dir_name = os.path.dirname(local_path)

                    dic_local = {}

                    if os.path.exists(list_of_files_path):
                        with open(list_of_files_path, 'r') as file:
                            lines = file.readlines()
                            list_lines = []
                            for i in range(len(lines)):
                                list_lines.append(lines[i].strip('\n').split('\t'))

                            for i in range(len(list_lines)):
                                dic_local[list_lines[i][0]] = int(list_lines[i][1])

                    if not os.path.exists(dir_name):
                        os.makedirs(dir_name)

                    if item not in dic_local or dic_local[item] < attr.st_mtime:
                        print(f'downloading item {item}')
                        sftp.get(item, local_path)
                        with open(list_of_files_path, 'a') as file:
                            file.write(f'{item}\t{attr.st_mtime}\n')

                    # if item.endswith('.zip'):
                    #     with zipfile.ZipFile(local_path, 'r') as zip_ref:
                    #         zip_ref.extractall(local_path.rstrip('.zip'))
                    #     os.remove(local_path)

                    if item.endswith('.zip'):
                        file_unzip(local_path)
                print('Done')
    except Exception as e:
        print(e.__doc__)
        print(e.message, e)
        # excepName = type(e).__name__
        # print(excepName)
        # print(traceback.print_exc())
        # print('An exception occurred: {}'.format(e))


def file_unzip(local_path):
    with zipfile.ZipFile(local_path, 'r') as zip_ref:
        unziped_local_path = local_path.rstrip('.zip')
        zip_ref.extractall(unziped_local_path)
        os.remove(local_path)


def dyrectory_list(path):
    """List directory"""
    list_of_cases_local = []
    for folderNmae in os.listdir(path):
        if folderNmae.isdigit() and os.path.isdir(folderNmae):
            list_of_cases_local.append(folderNmae)
    return list_of_cases_local


def dyrectory_remove(list_of_cases_sf, list_of_cases_local):
    for i in range(len(list_of_cases_local)):
        if list_of_cases_local[i] is not None and list_of_cases_local[i] not in list_of_cases_sf:
            # print('.' + '/' + list_of_cases_local[i])
            shutil.rmtree('.' + '/' + list_of_cases_local[i])


# list_of_links, list_of_cases_sf = my_staff.my_query()

# list_of_cases_local = dyrectory_list('.')
list_of_links=['sftp://ftp04043462:6ndNG5pR@supportftp9.veeam.com/upload']
download_ftp(list_of_links)
#
# dyrectory_remove(list_of_cases_sf, list_of_cases_local)
