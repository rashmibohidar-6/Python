cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
    
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))