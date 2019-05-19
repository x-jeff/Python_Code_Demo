#f=open("temp.txt","w")
#f.write("hello world")
#f.close
#with open("temp.txt","w") as f:
#    f.write("hello\nworld")
#with open("temp.txt","r") as f:
    #print(f.read())
    #print(f.read(0))
    #print(f.read(1))
    #print(f.read(6))
    #print(f.read(7))
    #print(f.read(15))
#with open("temp.txt","r") as f:
#    for n in f.read():
#        print(n)
#with open("temp.txt","r") as f:
    #print(f.readline())
    #print(f.readline(0))
    #print(f.readline(1))
    #print(f.readline(6))
    #print(f.readline(7))
#with open("temp.txt","r") as f:
#    for n in f.readline():
#        print(n)
#with open("temp.txt","r") as f:
    #print(f.readlines())
    #print(f.readlines(0))
    #print(f.readlines(1))
    #print(f.readlines(5))
    #print(f.readlines(6))
with open("temp.txt","r") as f:
    for n in f.readlines():#for n in f: 也可以
        #print(n)
        print(n.strip())