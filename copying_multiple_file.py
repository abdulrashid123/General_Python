import os
import shutil


def copy_file(source,destination,n=1):
    print()
    print("copying....")
    if os.path.exists(source) and os.path.exists(destination):
        
        print("path_exists")
        try:
            for i in range(n):
                temp_destination = os.path.join(destination,"ball"+str(i)+".jpg")
                print(temp_destination)
                shutil.copy(source,temp_destination)
        
        # For other errors 
        except: 
            print("Error occurred while copying file.")

source_path = "<source_path>"
destination_path = "<destination_path>"

copy_file(source_path,destination_path,10)
