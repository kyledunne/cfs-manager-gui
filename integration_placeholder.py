#I am still getting an error within manager.py while calling the below line
#from cfs_manager.manager import Main_FS
#from cfs_manager.help_functions import license, github, documentation

#fs = Main_FS()


def download(filename, destination):
    return True


def get_default_download_destination():
    return 'C:\\Users\\AlisonRocks\\Downloads'


def delete(filename):
    return True


#returns a list containing the names of the files that were uploaded
def upload_from(directory_name):
    return ['uploadedFile1.txt', 'uploadedFile2.txt', 'uploadedZip666comma666comma666.zip']


def upload_all():
    return ['ALL', 'WILL BE', 'UPLOADED']


#return list of names of folders being watched
def get_watched_folders():
    return ['OWLS', 'NEWTS', 'SALAMANDERS', 'C:\\Users\\Whaaaaaaat????????', 'a', 'b', 'c', 'd', 'e', '1', '2', '3']


def watch(directory_name):
    return True


def remove_from_watched(directory_name):
    return True


#gets list of files being managed by cfs_manager
def get_file_list():
    return ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt', 'file7.txt', 'file8.txt'
            , 'file12.txt', 'file22.txt', 'file32.txt', 'file42.txt', 'file52.txt', 'file62.txt', 'file72.txt'
            , 'file82.txt', 'file122.txt', 'file222.txt', 'file332.txt', 'file442.txt', 'file552.txt', 'file662.txt'
            , 'file772.txt', 'file882.png', 'file2.zip', 'file3.zip', 'file4.zip', 'file5.zip', 'file6.zip', 'file7.zip'
            , 'file8.zip', 'file666commma666comma666.zip']


#returns a dictionary containing various pieces of info about the file
#(or if it's easier to implement, a list of strings)
def get_file_info(filename):
    return {'filename': filename, 'size': '666', 'system type': 'Google Drive', 'date': '6/6/66 6:06'}


def refresh_cloud():
    return True


def clear_cloud():
    return True


def open_docs():
    #documentation(fs, [])
    pass


def open_github():
    #github(fs, [])
    pass


def open_license():
    #license(fs, [])
    pass


def get_total_space():
    #return fs.file_system_info['total quota']/2**30
    return 15.0


def get_space_used():
    #return fs.cfs_size/2**30
    return 3.0


def get_version_number():
    return '1.3.0'
