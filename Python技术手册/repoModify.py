import string, os, sys, hashlib

def list_files(path):
    list = os.listdir(PATH)
    return list

def modifyFile(oldfile, newfile):
    fh = open(oldfile)
    sh = open(newfile, 'w+')
    for line in fh.readlines():
        if re.match(r'#baseurl', line):
            new_line = re.sub('#baseurl', 'baseurl', line)
            sh.write(new_line)
        elif re.match(r'^mirrorlist', line):
            new_line = re.sub(r'mirrorlist', "#mirrorlist", line)
            #print new_line
            sh.write(new_line)
        else:
            sh.write(line)

def md5sum(filename):
    '''
    对文件的内容进行MD5才是正确的
    '''
    fd = open(filename,"r")
    fcont = fd.read()
    fd.close()
    fmd5 = hashlib.md5(fcont)
    return fmd5

PATH = "/etc/yum.repos.d/"
#PATH = "/etc/yum.repos.d/"
FILELIST = list_files(PATH)
for filename in FILELIST:
    oldfile = PATH + filename
    oldfileMD5 = md5sum(oldfile)
    newfileName = "/tmp/" + filename + ".swap"
    modifyFile(oldfile, newfileName)
    newfileMD5 = md5sum(newfileName)
    if oldfileMD5 != newfileMD5:
        shutil.copy(newfileName, oldfile)
