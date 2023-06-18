import os
import shutil

lib_path = './CCS_bak/'

db_path = './CCS_db124_SEQ36_160/'

lib_list = []
db_list  = []

for root, dirs, files in os.walk(lib_path):
    for file in files:
        lib_list.append(os.path.splitext(file)[0])

for root, dirs, files in os.walk(db_path):
    for file in files:
        print (os.path.splitext(file)[0])
        db_list.append(os.path.splitext(file)[0])

diff = set(lib_list).difference((set(db_list)))

for name in diff:
    shutil.copy(lib_path + '/' + name + '.lib', './CCS/')