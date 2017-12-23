#I am still getting an error within manager.py while calling the below line
from cfs_manager.cli import download_directory
from cfs_manager.manager import Main_FS
from cfs_manager.file_systems import dirs
from cfs_manager.help_functions import license, github, documentation
from cfs_manager.cfs_watcher import main
import __main__

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
    new_files_list = get_file_list()
    len_difference = len(new_files_list) - len(__main__.managed_files)
    if len_difference == 0:
        return []
    elif len_difference == 1:
        return [new_files_list[0]]
    else:
        new_list = new_files_list[0:len_difference]
        new_list.reverse()
        return new_list


def upload_all():
    fs.upload_all()
    new_files_list = get_file_list()
    len_difference = len(new_files_list) - len(__main__.managed_files)
    if len_difference == 0:
        return []
    elif len_difference == 1:
        return [new_files_list[0]]
    else:
        new_list = new_files_list[0:len_difference]
        new_list.reverse()
        return new_list


#return list of names of folders being watched
def get_watched_folders():
    return dirs


def watch(directory_name):
    main(directory_name)
    dirs.append(directory_name)


def remove_from_watched(directory_name):
    # TODO
    pass


#gets list of files being managed by cfs_manager
def get_file_list():
    names = []
    for file in fs.files:
        name_to_add = file['filename']
        names.append(name_to_add[0:len(name_to_add)-4])
    return names


#returns a dictionary containing various pieces of info about the file
#(or if it's easier to implement, a list of strings)
def get_file_info(filename):
    return fs.inspect_file(filename, return_dict=True)


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
