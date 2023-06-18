import os

in_path = './CCS_SEQ/'
out_path = './test/'
files = os.listdir(in_path)

flag = 0
for file in files:
    with open(out_path + file, 'w') as out:
        with open(in_path + file) as f:
            for line in f:
                if line.startswith('  cell (ICG'):
                    flag = 1
                if flag == 1:
                    if line.startswith('  cell ('):
                        if line.startswith('  cell (ICG') == 0:
                            flag = 0
                if flag:
                    out.write('/*' + line[0:-1] + '\t*/' + '\n')
                else: out.write(line)

out.close()

