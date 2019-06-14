
def main():
    x = factorial(5)
    print(x)

def factorial(x:int):
    if x==0:
        return 1
    if x<0:
        return -1
    res_rec = factorial(x-1)
    return x * res_rec

if __name__ == '__main__':
    main()