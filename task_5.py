def factorial(n):
    if n==0:
        return 1
    else:
        a=1
        for i in range(1,n):
            a=a*(i+1)
    return a

def report():
    digit=1
    for i in range(101):
        print(f"{i}! is {len(str(digit))} digits long")
        digit=digit*(i+1)
