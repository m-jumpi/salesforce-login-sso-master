import os
import re
import zipfile
import shutil


def local_files(list_of_files_path):
    local_dic = {}
    if os.path.exists(list_of_files_path):
        with open(list_of_files_path, 'r') as file:
            lines = file.readlines()
            list_lines = []
            for i in range(len(lines)):
                list_lines.append(lines[i].strip('\n').split('\t'))
            for i in range(len(list_lines)):
                local_dic[list_lines[i][0]] = int(list_lines[i][1])
    return local_dic


def check_dir(local_file_path):
    local_dir = os.path.dirname(local_file_path)
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)


def zip_check(local_file_path):
    logRegex = re.compile(r'\S*\d{4}-\d{2}-\d{2}T\d{6}_VeeamBackupLogs\S*.zip')
    if local_file_path.endswith('.zip'):
        with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
            zip_ref.extractall(local_file_path.rstrip('.zip'))
        os.remove(local_file_path)
        if logRegex.search(local_file_path):
            pass
        else:
            walk_folder(local_file_path.rstrip('.zip'))


def walk_folder(local_file_path):
    for folder, subfolder, filenames in os.walk(local_file_path):
        for filename in filenames:
            zip_check(os.path.join(folder, filename))


def write_to_list(list_of_files_path, key, value):
    with open(list_of_files_path, 'a') as list_of_files:
        list_of_files.write(f'{key}\t{value}\n')


def remove_dir(local_path, list_of_cases_sf):
    for folder in os.listdir(local_path):
        if folder.isdigit() and os.path.isdir(os.path.join(local_path, folder)) and folder not in list_of_cases_sf:
            shutil.rmtree(os.path.join(local_path, folder))
