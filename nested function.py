#nested function
# function within function that called nested function


def greater(a,b):
    if a > b:
        return a
    return b

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)

print(new_greatest(1000,200,30))
