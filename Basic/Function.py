import math


def PlayerUpdate():
    Move()


def Move():
    a = 1


def Vector2Length(x, y):
    return math.sqrt(x**2 + y**2)


def Vector2Add(a: int, b: int):
    return a + b, a - b


def PrintVector(a):
    x = 1
    y = 3
    print(a(x, y))


def Foo(i):
    if i < 10:
        i += 1
        print(i)
        Foo(i)


def main():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]
    sum_result, diff_result = Vector2Add(5, 3)
    print(f"Sum: {sum_result}, Difference: {diff_result}")

    z = 3
    w = 4
    length = Vector2Length(z, w)

    A = lambda x, y: math.sqrt(x**2 + y**2)

    leng = A(z, w)

    l = "Hello, World!"

    # PrintVector(Vector2Add)

    Foo(0)


if __name__ == "__main__":
    main()
