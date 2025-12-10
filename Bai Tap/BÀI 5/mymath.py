def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    if not values:  
        return None
    return sum(values) / len(values)
