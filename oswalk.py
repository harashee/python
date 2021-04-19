'''
OS walk helps in traversing child directories and 
returns top directory, current directory and list of files in the current directory

'''

import os
files = []
def walk(top, topdown=True, onerror=None, followlinks=False):
    f = []
    d = []
    content = os.listdir(top)
    for item in content:
        if os.path.isfile(top + '/'+ item):
            f.append(item)
        else:
            d.append(top+'/'+item)
            walk(top+'/'+ item)
    print(top,d,f)

if __name__ == "__main__":
    walk("/home/hrasheed/test/")
