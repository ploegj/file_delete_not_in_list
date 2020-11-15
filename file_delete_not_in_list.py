import os
# this script will delete all files which are not listed in str_files_to_keep from str_path

set_device = set()

# path containing files to delete/keep
str_path = 'data'
str_files_to_keep = 'files_to_keep.txt'

# read files to keep into set_device set, reading them into a set keeps them unique
with open(str_files_to_keep, "r") as fh:
    line = fh.readline()
    while line != '':
        # add first 6 characters of devicename to set
        set_device.add(line.strip()[:6])
        # print(line.strip())
        line = fh.readline()

# loop through all files in str_path and delete the filenames that cannot be found in set_device
for filename in os.listdir(str_path):
    if filename[:6] not in set_device:
        print(str_path + '\\' + filename)
        os.unlink(str_path + '\\' + filename)


sys.exit()
