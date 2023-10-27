apple = 100
print(globals())
def sample():
    global apple
    print(apple)
sample()