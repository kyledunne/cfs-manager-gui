#I am still getting an error within manager.py while calling the below line
from cfs_manager.manager import Main_FS
from cfs_manager.help_functions import license, github, documentation

fs = Main_FS()


def download(filename, destination):
    pass


def get_default_download_destination():
    pass


def delete(filename):
    pass


#returns a list containing the names of the files that were uploaded
def upload_from(directory_name):
    pass


def upload_all():
    pass


#return list of names of folders being watched
def get_watched_folders():
    pass


def watch(directory_name):
    pass


def remove_from_watched(directory_name):
    pass


#gets list of files being managed by cfs_manager
def get_file_list():
    pass


#returns a dictionary containing various pieces of info about the file
#(or if it's easier to implement, a list of strings)
def get_file_info(filename):
    pass


def refresh_cloud():
    pass


def clear_cloud():
    pass


def open_docs():
    documentation(fs, [])


def open_github():
    github(fs, [])


def open_license():
    license(fs, [])


def get_total_space():
    return fs.file_system_info['total quota']/2**30


def get_space_used():
    return fs.cfs_size/2**30


def get_version_number():
    return '1.3.0'
