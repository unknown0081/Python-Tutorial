def main():
    list = [1, 2, 3, 4, 5]
    tuple = (1, 2, 3, 4, 5)
    dictionary = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}

    print(list[0])
    list[0] = "1asdf"
    print(list[0])

    print(list)
    list.append(6)
    print(list)
    list.remove(6)
    print(list)

    # tuple[0] = 1
    print(tuple)

    list += list
    print(list)

    tuple += tuple

    o = tuple + tuple
    print(tuple)

    print(dictionary["one"])


if __name__ == "__main__":
    main()
