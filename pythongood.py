def myfunc():
    x = 300
    print(x)

myfunc()


def myfunc1():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc1()

x = 300

def myfunc2():
    print(x)

myfunc2()

print(x)

x = 300

def myfunc3():
    x = 200
    print(x)

myfunc()

print(x)

def myfunc4():
    global x
    x = 300

myfunc4()

print(x)

print("f")

x = 300

def myfunc5():
    global x
    x = 200

myfunc5()

print(x)