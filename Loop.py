def main():
    for i in range(0, 10, 2):
        print(str(i) + "> Hello, World!")
    print("End\n")

    i = 0
    while i < 10:
        i += 1
        if i < 5:
            continue
        print(str(i) + ">Hello, World!")

        if i == 8:
            break
    print("End\n")

    while True:
        if a == 10:
            break


if __name__ == "__main__":
    main()
