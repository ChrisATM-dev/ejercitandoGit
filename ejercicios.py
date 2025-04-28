## FizzBuzz

def fizzbuzz(n):

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def printSphereASCII(radius):
    """
    Print a sphere in ASCII art with the given radius.
    """
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if x**2 + y**2 <= radius**2:
                print("o", end="")
            else:
                print(" ", end="")
        print()