import os 
os.chdir('new')

u = 0 
def get():
    global u
    u += 1 
    return f"a{u}"

x = 0 
def get_name():
    global x 
    x += 1 
    return f"{x+223}.jpg"

for i in os.listdir():
    if not i.split('.')[0].isnumeric():
        os.rename(i,get_name())

# for i in os.listdir():
#     os.rename(i,get_name())
