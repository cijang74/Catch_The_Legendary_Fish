a = False

def test():
    global a
    a = True
test()

def test2():
    global a
    if a == True:
        print("정상입니다")

test2()