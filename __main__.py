import os
from tkinter import *
from cfs_manager.manager import Main_FS
from cfs_manager.help_functions import license, github, documentation
fs = Main_FS()

image_dir = os.path.join('cfs-manager-gui', 'res', 'img')

def upload():
    pass


def upload_all():
    pass


def open_manage_watched_folders_window():
    pass


def refresh():
    pass


def clear_cloud():
    pass


def display_download_or_delete_tip():
    pass


def open_about_window():
    pass


def open_docs():
    documentation(fs, [])


def open_github():
    github(fs, [])


def open_license():
    license(fs, [])


def open_gui_overview():
    pass


def open_send_feedback_window():
    pass


def get_space_used():
    return fs.cfs_size/2**30


def get_total_space():
    return fs.file_system_info['total quota']/2**30


def open_storage_details_window():
    pass


def get_version_number():
    return '1.3.0'


def switch_to_list_layout():
    pass


def switch_to_grid_layout():
    pass


def open_inspect_file_panel(file):
    pass


def main():
    root = Tk()
    root.title('CFS Manager v' + get_version_number())
    root.option_add('*tearOff', False) #removes dashed line from top of all cascading menus
    main_menu = Menu(root)
    root.config(menu=main_menu)

    cloud_files_panel = Frame(root, width=400)
    file_inspect_panel = Frame(root)
    storage_space_bar = Frame(root, height=100)

    #initialize main_menu elements
    local_submenu = Menu(main_menu)
    main_menu.add_cascade(label='Local', menu=local_submenu)
    local_submenu.add_command(label='Upload...', command=upload)
    local_submenu.add_command(label='Upload All', command=upload_all)
    local_submenu.add_command(label='Manage Watched Folders...', command=open_manage_watched_folders_window)

    cloud_submenu = Menu(main_menu)
    main_menu.add_cascade(label='Cloud', menu=cloud_submenu)
    cloud_submenu.add_command(label='Refresh', command=refresh)
    cloud_submenu.add_command(label='Clear', command=clear_cloud)
    #cloud_submenu.add_separator()
    #cloud_submenu.add_command(label='Download...', command=display_download_or_delete_tip)
    #cloud_submenu.add_command(label='Delete...', command=display_download_or_delete_tip)

    about_submenu = Menu(main_menu)
    main_menu.add_cascade(label='About', menu=about_submenu)
    about_submenu.add_command(label='About...', command=open_about_window)
    about_submenu.add_command(label='Docs...', command=open_docs)
    about_submenu.add_command(label='Github...', command=open_github)
    about_submenu.add_command(label='License...', command=open_license)

    help_submenu = Menu(main_menu)
    main_menu.add_cascade(label='Help', menu=help_submenu)
    help_submenu.add_command(label='Send Question/Request to the Developers...', command=open_send_feedback_window)

    #initialize storage space bar
    storage_space_bar.pack(side=BOTTOM, anchor=SW, fill=X)

    ssg_width = 80
    ssg_height = 17
    storage_space_graphic = Canvas(storage_space_bar, width=ssg_width, height=ssg_height)
    storage_space_graphic.pack(side=LEFT)
    space_used = get_space_used()
    total_space = get_total_space()
    sur_width = ssg_width * (space_used / total_space)
    print(sur_width)
    border_rectangle = storage_space_graphic.create_rectangle(0, 0, ssg_width, ssg_height, fill='lightgrey')
    space_used_rectangle = storage_space_graphic.create_rectangle(0, 0, sur_width, ssg_height, fill='green', outline='')

    space_used_text = Label(storage_space_bar, text=str(space_used) + ' GB used out of ' + str(total_space))
    space_used_text.pack(side=LEFT)

    storage_details_button = Button(storage_space_bar, text="Storage Details...", command=open_storage_details_window)
    storage_details_button.pack(side=LEFT)

    #initialize cloud files panel
    cloud_files_panel.pack(side=LEFT, fill=BOTH)
    cfp_top_bar = Frame(cloud_files_panel, height=100)
    cfp_top_bar.pack(side=TOP, fill=X)

    my_cloud_label = Label(cfp_top_bar, text='My Cloud')
    my_cloud_label.pack(side=LEFT)

    list_layout_img = PhotoImage(file=os.path.join(image_dir, 'list_layout.png'))
    grid_layout_img = PhotoImage(file=os.path.join(image_dir, 'grid_layout.png'))

    list_layout_button = Button(cfp_top_bar, image=list_layout_img, command=switch_to_list_layout, width=20, height=20)
    grid_layout_button = Button(cfp_top_bar, image=grid_layout_img, command=switch_to_grid_layout, width=20, height=20)
    list_layout_button.pack(side=RIGHT)
    grid_layout_button.pack(side=RIGHT)

    files_grid_frame = Frame(cloud_files_panel)
    files_grid_frame.pack(fill=BOTH)
    folder_image = PhotoImage(file=os.path.join(image_dir, 'sample_folder_image.png'))

    sample_file_1 = Label(files_grid_frame, image=folder_image)
    sample_file_2 = Label(files_grid_frame, image=folder_image)
    sample_file_3 = Label(files_grid_frame, image=folder_image)
    sample_file_4 = Label(files_grid_frame, image=folder_image)
    sample_file_5 = Label(files_grid_frame, image=folder_image)
    sample_file_6 = Label(files_grid_frame, image=folder_image)
    sample_file_7 = Label(files_grid_frame, image=folder_image)
    sample_file_8 = Label(files_grid_frame, image=folder_image)
    sample_file_9 = Label(files_grid_frame, image=folder_image)

    sample_file_1.grid(row=0, column=0)
    sample_file_2.grid(row=0, column=1)
    sample_file_3.grid(row=0, column=2)
    sample_file_4.grid(row=1, column=0)
    sample_file_5.grid(row=1, column=1)
    sample_file_6.grid(row=1, column=2)
    sample_file_7.grid(row=2, column=0)
    sample_file_8.grid(row=2, column=1)
    sample_file_9.grid(row=2, column=2)

    #initialize file inspect panel
    file_inspect_panel.pack(side=RIGHT, fill=Y)

    sample_file_inspect_image = Label(file_inspect_panel, image=folder_image)
    sample_file_inspect_image.pack(side=TOP, anchor=N)
    label_1 = Label(file_inspect_panel, text='nameOfFile.txt')
    label_2 = Label(file_inspect_panel, text='(in the future, you will')
    label_3 = Label(file_inspect_panel, text='select a file from the left')
    label_4 = Label(file_inspect_panel, text='and it will display here.')
    label_5 = Label(file_inspect_panel, text='(and this text will be the')
    label_6 = Label(file_inspect_panel, text='(--file-inspect info))')
    label_1.pack(side=TOP)
    label_2.pack(side=TOP)
    label_3.pack(side=TOP)
    label_4.pack(side=TOP)
    label_5.pack(side=TOP)
    label_6.pack(side=TOP)
    download_default_button = Button(file_inspect_panel, text='Download (Default)')
    download_custom_button = Button(file_inspect_panel, text='Download (Custom)...')
    delete_button = Button(file_inspect_panel, text='Delete')
    download_default_button.pack(side=TOP)
    download_custom_button.pack(side=TOP)
    delete_button.pack(side=TOP)

    root.mainloop()


if __name__ == '__main__':
    main()
