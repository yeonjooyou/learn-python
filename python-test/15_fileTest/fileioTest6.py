# =============== listdir  ===============
import os

files = os.listdir("c:\\Temp") # \, / 는 디렉토리 구분자
print(type(files))
for f in files:
    print(f)

# =============== listdir2  ===============
import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "\\" + f
        if os.path.isdir(fullpath):
            print("[" + fullpath + "]")
            dumpdir(fullpath)
        else:
            print("\t" + fullpath)

dumpdir("c:\\yyj\\PYTHONexam")
