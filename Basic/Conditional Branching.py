def main():
    a = 1
    b = 2
    boolvar = a == b
    c = a == b
    d = a != b

    """
    if a == b:
    if a != b:

    if a > b:
    if a >= b:

    if a < b:
    if a <= b:

    if c or d:
    if c and d:
    if c ^ d:
    if not c:

        if not (c and d):
        if not (c or d):
    """

    if a == b and a <= b:
        print(a)
    elif a < b:
        print(b)
    else:
        print(b)

    match a:
        case 1:
            print(a)
        case 2:
            print(b)
        case 3:
            print(b)
        case _:
            print("default")

    print(b)


if __name__ == "__main__":
    main()
