import os
import my_staff
from case import Case
from utils import local_files, check_dir, zip_check, write_to_list, remove_dir
from collections import namedtuple
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(astime)s - %(levelname)s - %(message)s')

def my_func(list_of_links):
    for link in list_of_links:
        case = Case(link)
        try:
            with case.get_connection() as sftp:
                print('Connection succesfully established ... ')
                lm_upload = sftp.stat(r'/upload')
                list_of_files_path = os.path.join(local_path, case.number, case.list_of_files)
                local_dic = local_files(list_of_files_path)

                if local_dic and lm_upload.st_mtime <= local_dic().get(r'/upload', 0):
                    continue
                directory_structure = sftp.walktree('/upload', case.store_files_name, case.store_dir_name,
                                                    case.store_other_file_types)
                if not case.file_names:
                    continue
                for file in case.file_names:
                    lm_file = sftp.stat(file)
                    remote_dic = {}
                    remote_dic[file] = lm_file.st_mtime
                    local_file_path = os.path.join(local_path, case.number, os.path.basename(file))

                    if file not in local_dic or local_dic[file] < lm_file.st_mtime:
                        print(f'Downloading an item: {local_file_path}')
                        check_dir(local_file_path)
                        sftp.get(file, local_file_path)
                        write_to_list(list_of_files_path, file, lm_file.st_mtime)
                        zip_check(local_file_path)
                        if case.file_names.index(file) == (len(case.file_names) - 1):
                            write_to_list(list_of_files_path, '/upload', lm_upload.st_mtime)
                print('Done')
        except Exception as e:
            print(logging.error(e))


local_path = '/Users/denis/Downloads'

sf=namedtuple('sf', ['list1', 'list2'])
sf_return=sf(*my_staff.my_query())
print(sf_return.list1)
print(sf_return.list2)

# list_of_links, list_of_cases_sf = my_staff.my_query()
list_of_links=['sftp://ftp04043462:6ndNG5pR@supportftp9.veeam.com/upload']
my_func(list_of_links)
# remove_dir(local_path, list_of_cases_sf)


