def outer(x):
    def inner(y):
        return x+y
    return inner
add_five = outer(5)
res = add_five(6)
print(res)

#function as an aurgument
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 10, 5)
print(result)

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

fun = greeting("Ram")
message = greet_john()
print(message)
