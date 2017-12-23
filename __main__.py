import os
from tkinter import *
from tkinter import filedialog, messagebox
image_dir = os.path.join(os.getcwd(), 'res', 'img')
import integration
watched_folders = integration.get_watched_folders()
managed_files = integration.get_file_list()
default_download_destination = integration.get_default_download_destination()

def open_manage_watched_folders_window():
    ManageWatchedFoldersWindow()


class ManageWatchedFoldersWindow:

    def __init__(self):
        self.window = Toplevel()
        self.window.title('Manage Watched Folders')
        self.listbox_frame = Frame(self.window)
        self.listbox_frame.pack(side=LEFT, fill=Y)
        self.current_inspected_folder = None
        self.scrollbar = Scrollbar(self.listbox_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.folders_listbox = Listbox(self.listbox_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.folders_listbox.yview)
        self.folders_listbox.pack(side=LEFT)
        width = 20
        for folder in watched_folders:
            width = max(width, len(folder))
            self.folders_listbox.insert(END, folder)
        self.folders_listbox.config(width=min(50, width+3))
        self.folders_listbox.bind('<ButtonRelease-1>', self.find_and_inspect_folder)

        self.right_side_frame = Frame(self.window)
        self.right_side_frame.pack(side=RIGHT, fill=Y)
        self.add_button = Button(self.right_side_frame, text='Add...', command=self.add)
        self.add_button.pack(side=TOP)
        self.remove_button = Button(self.right_side_frame, text='Stop Watching', command=self.remove)
        self.remove_button.pack(side=BOTTOM)
        self.remove_button.config(state=DISABLED)
        self.inspected_folder_name_label = Label(self.right_side_frame, text='')
        self.inspected_folder_name_label.pack(side=BOTTOM)
        Label(self.right_side_frame, text='--------------------').pack(side=BOTTOM)
        self.window.grab_set()
        self.window.focus_set()

    def find_and_inspect_folder(self, event_data):
        self.current_inspected_folder = self.folders_listbox.get(self.folders_listbox.curselection()[0])
        self.inspected_folder_name_label.config(text=self.current_inspected_folder)
        # self.remove_button.config(state=NORMAL)

    def add(self):
        folder_to_add = filedialog.askdirectory()
        if folder_to_add:
            integration.watch(folder_to_add)
            watched_folders.append(folder_to_add)
            self.folders_listbox.insert(END, folder_to_add)

    def remove(self):
        integration.remove_from_watched(self.current_inspected_folder)
        folders_listbox_index = watched_folders.index(self.current_inspected_folder)
        watched_folders.remove(self.current_inspected_folder)
        self.folders_listbox.delete(folders_listbox_index)
        self.inspected_folder_name_label.config(text='')
        self.remove_button.config(state=DISABLED)


def open_about_window():
    pass


def open_send_feedback_window():
    pass


def inspect_file(file):
    print(file)


def main():
    MainWindow()


class MainWindow:

    def __init__(self):
        #initialize constants
        self.file_listbox_max_width = 50
        self.file_inspect_panel_width = 33



        #initialize window
        self.current_inspected_file = None
        self.manage_watched_folders_window = None

        self.root = Tk()
        self.root.title('CFS Manager v' + integration.get_version_number())
        self.root.option_add('*tearOff', False)  # removes dashed line from top of all cascading menus
        main_menu = Menu(self.root)
        self.root.config(menu=main_menu)

        cloud_files_panel = Frame(self.root, width=400)
        file_inspect_panel = Frame(self.root)
        self.storage_space_bar = Frame(self.root, height=100)

        # initialize main_menu elements
        local_submenu = Menu(main_menu)
        main_menu.add_cascade(label='Local', menu=local_submenu)
        local_submenu.add_command(label='Upload...', command=self.upload)
        local_submenu.add_command(label='Upload All', command=self.upload_all)
        local_submenu.add_command(label='Manage Watched Folders...', command=open_manage_watched_folders_window)

        cloud_submenu = Menu(main_menu)
        main_menu.add_cascade(label='Cloud', menu=cloud_submenu)
        cloud_submenu.add_command(label='Refresh', command=self.refresh)
        cloud_submenu.add_command(label='Clear', command=self.clear_cloud)

        about_submenu = Menu(main_menu)
        main_menu.add_cascade(label='About', menu=about_submenu)
        about_submenu.add_command(label='About...', command=integration.open_docs)
        about_submenu.add_command(label='Github...', command=integration.open_github)
        about_submenu.add_command(label='License...', command=integration.open_license)

#       help_submenu = Menu(main_menu)
#       main_menu.add_cascade(label='Help', menu=help_submenu)
#       help_submenu.add_command(label='Send Question/Request to the Developers...', command=open_send_feedback_window)

        # initialize storage space bar
        self.storage_space_bar.pack(side=BOTTOM, anchor=SW, fill=X)

        self.ssg_width = 80
        self.ssg_height = 17
        self.storage_space_graphic = Canvas(self.storage_space_bar, width=self.ssg_width, height=self.ssg_height)
        self.storage_space_graphic.pack(side=LEFT)
        space_used = integration.get_space_used()
        total_space = integration.get_total_space()
        self.sur_width = self.ssg_width * (space_used / total_space)
        self.storage_space_graphic.create_rectangle(0, 0, self.ssg_width, self.ssg_height, fill='lightgrey')
        self.storage_space_graphic.create_rectangle(0, 0, self.sur_width, self.ssg_height, fill='green', outline='')

        space_used_text = Label(self.storage_space_bar, text=str('%.2f' % space_used) + ' GB used out of '
                                + str('%.2f' % total_space) + ' |')
        space_used_text.pack(side=LEFT)

        self.status_label = Label(self.storage_space_bar, text='')
        self.status_label.pack(side=RIGHT)

        # initialize cloud files panel
        cloud_files_panel.pack(side=LEFT, fill=BOTH)
        cfp_top_bar = Frame(cloud_files_panel, height=100)
        cfp_top_bar.pack(side=TOP, fill=X)

        my_cloud_label = Label(cfp_top_bar, text='My Cloud')
        my_cloud_label.pack(side=LEFT)

        scrollbar = Scrollbar(cloud_files_panel)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.file_listbox = Listbox(cloud_files_panel, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_listbox.yview)
        self.file_listbox.pack(side=LEFT, fill=BOTH)

        width = 20
        for file in managed_files:
            width = max(width, len(file))
            self.file_listbox.insert(END, file)
        self.file_listbox.config(width=min(self.file_listbox_max_width, width + 3))

        self.file_listbox.bind('<ButtonRelease-1>', self.find_and_inspect_file)

        # initialize file inspect panel
        file_inspect_panel.pack(side=RIGHT, fill=Y)

        self.no_file_selected_100x100_image = PhotoImage(file=os.path.join(image_dir, 'no_file_selected_100x100.png'))
        self.folder_100x100_image = PhotoImage(file=os.path.join(image_dir, 'folder_100x100.png'))
        self.document_100x100_image = PhotoImage(file=os.path.join(image_dir, 'document_100x100.png'))
        self.image_100x100_image = PhotoImage(file=os.path.join(image_dir, 'image_100x100.png'))

        self.file_inspect_image_label = Label(file_inspect_panel, image=self.no_file_selected_100x100_image)
        self.file_inspect_image_label.pack(side=TOP, anchor=N)
        self.file_name_label = Label(file_inspect_panel, text='Name: ')
        self.file_size_label = Label(file_inspect_panel, text='Size: ')
        self.date_uploaded_label = Label(file_inspect_panel, text='Uploaded: ')
        self.storage_provider_label = Label(file_inspect_panel, text='System type: ')
        self.file_name_label.pack(side=TOP)
        self.file_size_label.pack(side=TOP)
        self.date_uploaded_label.pack(side=TOP)
        self.storage_provider_label.pack(side=TOP)
        Label(file_inspect_panel, text='- - - - - - - - - - - - - - - - - - - - - - - - -').pack(side=TOP)
        self.choose_download_folder_label = Label(file_inspect_panel, text='Choose destination:')
        self.choose_download_folder_label.pack(side=TOP)
        download_destination_frame = Frame(file_inspect_panel)
        download_destination_frame.pack(side=TOP)
        self.download_destination_entry = Entry(download_destination_frame)
        self.download_destination_entry.insert(0, default_download_destination)
        self.download_destination_entry.config(width=self.file_inspect_panel_width-5)
        self.download_destination_entry.config(state=DISABLED)
        self.download_destination_entry.pack(side=LEFT, fill=X)
        self.choose_download_destination_button = Button(download_destination_frame, text='...',
                                                         command=self.choose_download_destination)
        self.choose_download_destination_button.config(state=DISABLED)
        self.choose_download_destination_button.pack(side=RIGHT)
        self.download_button = Button(file_inspect_panel, text='Download', command=self.download)
        self.download_button.config(state=DISABLED)
        self.download_button.pack(side=TOP)
        Label(file_inspect_panel, text='- - - - - - - - - - - - - - - - - - - - - - - - -').pack(side=TOP)
        self.delete_button = Button(file_inspect_panel, text='Delete', command=self.delete)
        self.delete_button.config(state=DISABLED)
        self.delete_button.pack(side=TOP)

        self.root.mainloop()

    def find_and_inspect_file(self, event_data):
        self.current_inspected_file = self.file_listbox.get(self.file_listbox.curselection()[0])
        self.set_file_inspect_panel()
        self.status_label.config(text='')

    def choose_download_destination(self):
        replacement_filepath = filedialog.askdirectory()
        if replacement_filepath:
            self.download_destination_entry.delete(0, END)
            self.download_destination_entry.insert(0, replacement_filepath)

    def download(self):
        filepath = self.download_destination_entry.get()
        viable = self.check_filepath_viability(filepath)
        if viable:
            integration.download(self.current_inspected_file, filepath)
            self.status_label.config(text=self.current_inspected_file + ' downloaded')
        else:
            print('invalid filepath error')
            exit()

    def delete(self):
        integration.delete(self.current_inspected_file)
        index_in_file_listbox = managed_files.index(self.current_inspected_file)
        managed_files.remove(self.current_inspected_file)
        self.status_label.config(text=self.current_inspected_file + ' deleted')
        self.file_listbox.delete(index_in_file_listbox)
        self.current_inspected_file = None
        self.set_file_inspect_panel()

    def set_file_inspect_panel(self):
        file = self.current_inspected_file
        if not file:
            self.file_inspect_image_label.config(image=self.no_file_selected_100x100_image)
            self.file_name_label.config(text='Name: ')
            self.file_size_label.config(text='Size: ')
            self.date_uploaded_label.config(text='Uploaded: ')
            self.storage_provider_label.config(text='Storage provider: ')
            self.choose_download_destination_button.config(state=DISABLED)
            self.download_button.config(state=DISABLED)
            self.delete_button.config(state=DISABLED)
            self.download_destination_entry.config(state=DISABLED)
        else:
            file_ext = file[-4:-1] + file[-1]
            if '.' not in file:
                self.file_inspect_image_label.config(image=self.folder_100x100_image)
            elif file_ext in ['.jpg', '.png', '.gif']:
                self.file_inspect_image_label.config(image=self.image_100x100_image)
            else:
                self.file_inspect_image_label.config(image=self.document_100x100_image)
            file_info = integration.get_file_info(file)
            file_name = file_info['filename']
            file_name = file_name[0:len(file_name)-4]
            self.file_name_label.config(text='Name: ' + file_name)
            self.file_size_label.config(text='Size: ' + str(file_info['size']) + ' bytes')
            self.date_uploaded_label.config(text='Uploaded: ' + file_info['date'])
            self.storage_provider_label.config(text='Storage provider: ' + file_info['system type'])
            self.choose_download_destination_button.config(state=NORMAL)
            self.download_button.config(state=NORMAL)
            self.delete_button.config(state=NORMAL)
            self.download_destination_entry.config(state=NORMAL)

    def check_filepath_viability(self, filepath):
        return True

    def upload(self):
        directory_to_upload_from = filedialog.askdirectory()
        if directory_to_upload_from:
            files = integration.upload_from(directory_to_upload_from)
            message_string = ''
            for file in files:
                managed_files.append(file)
                self.file_listbox.insert(END, file)
                message_string += file + '\n'
            messagebox.showinfo(str(len(files)) + ' Files Uploaded', message_string)
            self.status_label.config(text='')
        else:
            self.status_label.config(text='')

    def upload_all(self):
        files = integration.upload_all()
        message_string = ''
        for file in files:
            managed_files.append(file)
            self.file_listbox.insert(END, file)
            message_string += file + '\n'
        messagebox.showinfo(str(len(files)) + ' Files Uploaded', message_string)
        self.status_label.config(text='')

    def refresh(self):
        integration.refresh_cloud()
        managed_files.clear()
        for file in integration.get_file_list():
            managed_files.append(file)
        self.file_listbox.delete(0, END)
        for file in managed_files:
            self.file_listbox.insert(END, file)
        self.current_inspected_file = None
        self.set_file_inspect_panel()
        self.status_label.config(text='File system refreshed')

    def clear_cloud(self):
        confirmation = messagebox.askyesno('Clear Cloud', 'This will delete all files in CFSManager\'s cloud.'
                                           + '\nAre you SURE you want to do this?')
        if confirmation:
            self.status_label.config(text='Clearing file system...')
            integration.clear_cloud()
            self.status_label.config(text='File system cleared')
            managed_files.clear()
            self.file_listbox.delete(0, END)
            self.current_inspected_file = None
            self.set_file_inspect_panel()
        else:
            self.status_label.config(text='Operation cancelled')


if __name__ == '__main__':
    main()
