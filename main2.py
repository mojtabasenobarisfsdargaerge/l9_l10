import os
path =r'C:\Users\Aref\Desktop\project'
#____________________#
def vogod_file(name, path):
    if name in os.listdir(path):
        print(f"{name} pyda shod")
        return True
    else:
        print(f"{name} pyda nashod")
        return False


vogod_file("main2.py", path)
vogod_file("users.txt", path)
vogod_file("data.csv", path)
vogod_file("report.pdf", path)
vogod_file("image.jpg", path)
#____________________#
r =os.listdir(path)
print(r)
#____________________#
def coant_file(path):
    coant =0
    for isfile in os.listdir(path):
        coant += 1
    return coant
print(coant_file(path))
#____________________#
def hagm_kb(b, path):
    r= os.path.getsize(b)
    r /= 1000    
    return (f"hagm file: {r} kb ast")
print(hagm_kb("main2.py", path))
print(hagm_kb("users.txt", path))
print(hagm_kb("data.csv", path))
print(hagm_kb("report.pdf", path))
print(hagm_kb("image.jpg", path))
#____________________#
def hagm_kb2(b, path):
    r= os.path.getsize(b)
    r /= 1000
    return (r)
r= [(hagm_kb2("main2.py", path)),
   (hagm_kb2("users.txt", path)),
   (hagm_kb2("data.csv", path)),
   (hagm_kb2("report.pdf", path)),
   (hagm_kb2("image.jpg", path)),
]
print(sum(r))
print(max(r))
print(min(r))
#_____________________#
import math
print(math.ceil(r[1]))
print(math.ceil(r[2]))
print(math.ceil(r[3]))
print(math.ceil(r[4]))
#_____________________#
def hagm_b(b, path):
    r= os.path.getsize(b) 
    return (f"hagm file: {r} b ast")
print(hagm_b("main2.py", path))
print(hagm_b("users.txt", path))
print(hagm_b("data.csv", path))
print(hagm_b("report.pdf", path))
print(hagm_b("image.jpg", path))
#_____________________#