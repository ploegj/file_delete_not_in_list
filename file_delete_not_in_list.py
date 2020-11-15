import os
set_device = set()

str_path = 'data'
with open("files_to_keep.txt", "r") as fh:
    line = fh.readline()
    while line != '':
        # add first 6 characters of devicename to set
        set_device.add(line.strip()[:6])
        # print(line.strip())
        line = fh.readline()

for filename in os.listdir('data'):
    if filename[:6] not in set_device:
        print(str_path + '\\' + filename)
        os.unlink(str_path + '\\' + filename)


sys.exit()
