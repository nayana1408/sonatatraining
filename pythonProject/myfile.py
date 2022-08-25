def myfile():
    try:
        c=open("nayana.txt", "r")
        print(c.read())
    except(FileNotFoundError):
        return ('not exists')
ani=myfile()
print(ani)