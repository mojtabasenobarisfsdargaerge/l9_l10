danesh_amozan =["ali","reza","sara"]
nomre =[18,19.25,16]

r =zip(danesh_amozan, nomre)
path =danesh_amozan =["ali","reza","sara"]
nomre =[18,19.25]

r =zip(danesh_amozan, nomre)

def meyangen(n):
    if not n:
        return None
    return sum(n) / len(n)
def add_grade():
    path ='C:Users\Aref\Desktop\grades.txt'
    with open(path,'w')as grades:
        grades.writelines(r)
def read_grade():
    path ='C:Users\Aref\Desktop\grades.txt'
    with open(path,'r')as grades:
        grades.read()
def calculate_average(n):
   return(meyangen(n))
def find_top_student(t):
    r =max(t.key)
    return(r)