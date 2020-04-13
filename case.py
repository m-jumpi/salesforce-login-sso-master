from urllib.parse import urlparse
import pysftp
import logging


class Case:
    def __init__(self, sftp_link):
        self.sftp_link = sftp_link
        link = urlparse(sftp_link)
        self.hostname = link.hostname
        self.username = link.username
        self.password = link.password
        self.number = self.username.lstrip('ftp')
        self.list_of_files = f'list_files_{self.number}.txt'

    def store_files_name(self, fname):
        self.file_names = []
        self.file_names.append(fname)

    def store_dir_name(self, dirname):
        self.dir_names = []
        self.dir_names.append(dirname)

    def store_other_file_types(self, name):
        self.un_name = []
        self.un_name.append(name)

    def get_connection(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        try:
            self.conn = pysftp.Connection(host=self.hostname, username=self.username, password=self.password,
                                          cnopts=cnopts)
            return self.conn
        except Exception as e:
            # print(e.__doc__)
            print(e.message, e)
            # print(logging.error(e))

    def __str__(self):
        return f'{self.hostname} / {self.username} / {self.number} / {self.password}'


c1 = Case('sftp://ftp04043462:6ndNG5pR@supportftp5.veeam.com/upload')

with c1.get_connection() as sftp:
    sftp.cwd(r'/upload')
    print(sftp.pwd)
    print('success')
    # sftp.get('./TENANT_2020-03-26T091301_VeeamBackupLogs.zip', './TENANT_2020-03-26T091301_VeeamBackupLogs.zip')
