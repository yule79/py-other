a = [1,2,3,4,5,6]

def b():
    c=0
    for i in a:
        if a[c]%2==0:
            print(a[c])
            c+=1
        else:
            c+=1
#
d=("aca")

def e():
    if d[::-1]==d:
        print("回文です")
    else:
        print("回文ではありません")
#
def g():
    for f in range(1,10):
        if f%2==0 and f%3==0:
            print("FizzBuzz")
        elif f%2==0:
            print("Fizz")
        elif f%3==0:
            print("Buzz")
        else:
            print(f)
#
b()
e()
g()