b =(
["Ali,ali@gmail.com,active"]
["Sara,sara@gmail.com,blocked"]
["Reza,reza@gmail.com,active"])




def add_user(y):
    b =input("shakhs ro vared kon:")
    if "@gmail.com" in b and "active" in b:
        b.append(y)
    else:
        print("vared nashod")
def find_user(y):
    b =input("shakhs ro vared kon:")
    if b in y:
        print("shakhs peyda shod")
    else:
        print("peyda nashod")
def delete_user(y):
    b =input("asm vared kon")
    if b in y:
        y.remove(b)
def update_user(y):
    b =input("asm vared kon:")
    if b in y:
        l =input("asm vared kon:")
    if "@gmail.com" in l:
        y.remove(b)
        l.append(y)
    else:
        print("vared nashod")
def list_user(y):
    print(y)

            
        