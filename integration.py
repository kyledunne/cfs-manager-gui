#I am still getting an error within manager.py while calling the below line
from cfs_manager.cli import download_directory
from cfs_manager.manager import Main_FS
from cfs_manager.file_systems import dirs
from cfs_manager.help_functions import license, github, documentation
from cfs_manager import manager

fs = Main_FS()


def download(filename, destination):
    return fs.download_file(filename, destination)


def get_default_download_destination():
    return download_directory


def delete(filename):
    fs.remove_file(filename)


#returns a list containing the names of the files that were uploaded
def upload_from(directory_name):
    fs.upload_archives(directory_name)
    # TODO needs to return a list of the names of the files that were uploaded
    return ['uploadedFile1.txt', 'uploadedFile2.txt', 'uploadedZip666comma666comma666.zip']


def upload_all():
    fs.upload_all()
    # TODO needs to return a list of the names of files that were uploaded
    return ['ALL', 'WILL BE', 'UPLOADED']


#return list of names of folders being watched
def get_watched_folders():
    return dirs


def watch(directory_name):
    # TODO
    return True


def remove_from_watched(directory_name):
    # TODO
    return True


#gets list of files being managed by cfs_manager
def get_file_list():
    names = []
    for file in fs.files:
        names.append(file['filename'])
    return names


#returns a dictionary containing various pieces of info about the file
#(or if it's easier to implement, a list of strings)
def get_file_info(filename):
    return fs.inspect_file(filename)


def refresh_cloud():
    fs.refresh_files()


def clear_cloud():
    fs.remove_all()


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
