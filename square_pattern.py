

def square_pattern(size, ch):
    for i in range(size):
        for j in range(size):
            print(ch, end=" ")
        print()
square_pattern(5,"*")
