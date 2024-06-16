def add(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(add(a, b))
