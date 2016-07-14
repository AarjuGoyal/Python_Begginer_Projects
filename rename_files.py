import os
def rename_files():
    #(1) find the files
    file_list = os.listdir('/Users/aarjugoyal/Documents/python_udacity_beg/prank')
    print(file_list)
    current_directory = os.getcwd()
    print(current_directory)
    os.chdir('/Users/aarjugoyal/Documents/python_udacity_beg/prank')
    print(os.getcwd())

     #(2) for each file, rename it
    for file_name in file_list:
          os.rename( file_name, file_name.translate(None, '1234567890') )
    os.chdir(current_directory)

rename_files()

        
