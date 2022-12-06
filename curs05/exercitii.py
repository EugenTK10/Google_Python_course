num_calls = 0

def exercitiu(x):
    global num_calls
    num_calls = 3
    num_calls +=1
    return x*x

print(exercitiu(4))