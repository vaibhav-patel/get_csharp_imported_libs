import os
dir1 = 'rc-test-execution-reviewer/'
def get_all_the_files(path):
    files = os.listdir(path)
    nf = []
    for file in files:
        nf.append(path + file)
    return nf

files = get_all_the_files(dir1)
q = files
visited = {}
libs = {}
def processLines(lines):
    for line in lines:
        if line != '':
            splits = line.split('using ')
            if len(splits) == 2:
                lib = splits[1]
                if lib[-2:] == ';\n':
                    lib = lib[:-2]
                if lib not in libs:
                    libs[lib] = 0
                libs[lib] += 1
    
while(len(q) > 0):
    nq = []
    for file in q:
        if file in visited:
            continue
        visited[file] = 1
        if os.path.isdir(file):
            file = file + '/'
            if file not in visited:
                visited[file] = 1
                nq += get_all_the_files(file)
        else:
            try:
                if file[-3:] == '.cs':
                    with open(file, 'r') as f:
                        lines = f.readlines()
                    processLines(lines)
            except:
                print('failed--', file)
                pass
    q = nq

removal = 'TE.'
external_libs = []
packages = {}
for lib in libs:
    if '=' not in lib:
        package = lib.split('.')[0]
        packages[package] = 1
        if lib[:len(removal)] != removal:
            external_libs.append(lib)
external_libs, packages
