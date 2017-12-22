import os
from tkinter import *
from tkinter import filedialog
import integration

image_dir = os.path.join('res', 'img')
watched_folders = integration.get_watched_folders()
managed_files = integration.get_file_list()
default_download_destination = integration.get_default_download_destination()


def upload():
    pass


def upload_all():
    pass


def open_manage_watched_folders_window():
    ManageWatchedFoldersWindow()


class ManageWatchedFoldersWindow:

    def __init__(self):
        window = Toplevel()
        window.title('Manage Watched Folders')
        self.listbox_frame = Frame(window)
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

        self.right_side_frame = Frame(window)
        self.right_side_frame.pack(side=RIGHT, fill=Y)
        self.add_button = Button(self.right_side_frame, text='Add...', command=self.add)
        self.add_button.pack(side=TOP)
        self.remove_button = Button(self.right_side_frame, text='Stop Watching', command=self.remove)
        self.remove_button.pack(side=BOTTOM)
        self.remove_button.config(state=DISABLED)
        self.inspected_folder_name_label = Label(self.right_side_frame, text='')
        self.inspected_folder_name_label.pack(side=BOTTOM)
        Label(self.right_side_frame, text='--------------------').pack(side=BOTTOM)

    def find_and_inspect_folder(self, event_data):
        self.current_inspected_folder = self.folders_listbox.get(self.folders_listbox.curselection()[0])
        self.inspected_folder_name_label.config(text=self.current_inspected_folder)
        self.remove_button.config(state=NORMAL)

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


def refresh():
    pass


def clear_cloud():
    pass


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
        self.current_inspected_file = None
        self.manage_watched_folders_window = None

        root = Tk()
        root.title('CFS Manager v' + integration.get_version_number())
        root.option_add('*tearOff', False)  # removes dashed line from top of all cascading menus
        main_menu = Menu(root)
        root.config(menu=main_menu)

        cloud_files_panel = Frame(root, width=400)
        file_inspect_panel = Frame(root)
        storage_space_bar = Frame(root, height=100)

        # initialize main_menu elements
        local_submenu = Menu(main_menu)
        main_menu.add_cascade(label='Local', menu=local_submenu)
        local_submenu.add_command(label='Upload...', command=upload)
        local_submenu.add_command(label='Upload All', command=upload_all)
        local_submenu.add_command(label='Manage Watched Folders...', command=open_manage_watched_folders_window)

        cloud_submenu = Menu(main_menu)
        main_menu.add_cascade(label='Cloud', menu=cloud_submenu)
        cloud_submenu.add_command(label='Refresh', command=refresh)
        cloud_submenu.add_command(label='Clear', command=clear_cloud)

        about_submenu = Menu(main_menu)
        main_menu.add_cascade(label='About', menu=about_submenu)
        about_submenu.add_command(label='About...', command=open_about_window)
        about_submenu.add_command(label='Docs...', command=integration.open_docs)
        about_submenu.add_command(label='Github...', command=integration.open_github)
        about_submenu.add_command(label='License...', command=integration.open_license)

        help_submenu = Menu(main_menu)
        main_menu.add_cascade(label='Help', menu=help_submenu)
        help_submenu.add_command(label='Send Question/Request to the Developers...', command=open_send_feedback_window)

        # initialize storage space bar
        storage_space_bar.pack(side=BOTTOM, anchor=SW, fill=X)

        ssg_width = 80
        ssg_height = 17
        storage_space_graphic = Canvas(storage_space_bar, width=ssg_width, height=ssg_height)
        storage_space_graphic.pack(side=LEFT)
        space_used = integration.get_space_used()
        total_space = integration.get_total_space()
        sur_width = ssg_width * (space_used / total_space)
        print(sur_width)
        storage_space_graphic.create_rectangle(0, 0, ssg_width, ssg_height, fill='lightgrey')
        storage_space_graphic.create_rectangle(0, 0, sur_width, ssg_height, fill='green', outline='')

        space_used_text = Label(storage_space_bar, text=str(space_used) + ' GB used out of ' + str(total_space))
        space_used_text.pack(side=LEFT)

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
        self.file_listbox.config(width=min(50, width + 3))

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
        Label(file_inspect_panel, text='- - - - - - - - - - - - - - - - - - - - - - - -').pack(side=TOP)
        self.choose_download_folder_label = Label(file_inspect_panel, text='Choose destination:')
        self.choose_download_folder_label.pack(side=TOP)
        download_destination_frame = Frame(file_inspect_panel)
        download_destination_frame.pack(side=TOP)
        self.download_destination_entry = Entry(download_destination_frame)
        self.download_destination_entry.insert(0, default_download_destination)
        self.download_destination_entry.config(width=len(default_download_destination))
        self.download_destination_entry.config(state=DISABLED)
        self.download_destination_entry.pack(side=LEFT, fill=X)
        self.choose_download_destination_button = Button(download_destination_frame, text='...',
                                                         command=self.choose_download_destination)
        self.choose_download_destination_button.config(state=DISABLED)
        self.choose_download_destination_button.pack(side=RIGHT)
        self.download_button = Button(file_inspect_panel, text='Download', command=self.download)
        self.download_button.config(state=DISABLED)
        self.download_button.pack(side=TOP)
        Label(file_inspect_panel, text='- - - - - - - - - - - - - - - - - - - - - - - -').pack(side=TOP)
        self.delete_button = Button(file_inspect_panel, text='Delete', command=self.delete)
        self.delete_button.config(state=DISABLED)
        self.delete_button.pack(side=TOP)

        root.mainloop()

    def find_and_inspect_file(self, event_data):
        self.current_inspected_file = self.file_listbox.get(self.file_listbox.curselection()[0])
        self.set_file_inspect_panel()

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
            print('downloaded')
        else:
            print('invalid filepath error')
            exit()

    def delete(self):
        integration.delete(self.current_inspected_file)
        index_in_file_listbox = managed_files.index(self.current_inspected_file)
        managed_files.remove(self.current_inspected_file)
        self.file_listbox.delete(index_in_file_listbox)
        self.current_inspected_file = None
        self.set_file_inspect_panel()
        print('deleted')

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
            if file_ext == '.zip':
                self.file_inspect_image_label.config(image=self.folder_100x100_image)
            elif file_ext in ['.jpg', 'jpeg', '.png', '.gif']:
                self.file_inspect_image_label.config(image=self.image_100x100_image)
            else:
                self.file_inspect_image_label.config(image=self.document_100x100_image)
            file_info = integration.get_file_info(file)
            self.file_name_label.config(text='Name: ' + file_info['filename'])
            self.file_size_label.config(text='Size: ' + file_info['size'] + ' bytes')
            self.date_uploaded_label.config(text='Uploaded: ' + file_info['date'])
            self.storage_provider_label.config(text='Storage provider: ' + file_info['system type'])
            self.choose_download_destination_button.config(state=NORMAL)
            self.download_button.config(state=NORMAL)
            self.delete_button.config(state=NORMAL)
            self.download_destination_entry.config(state=NORMAL)

    def check_filepath_viability(self, filepath):
        return True


if __name__ == '__main__':
    main()
