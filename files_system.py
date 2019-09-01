def ReadOP(file):
    f = open(file, 'r')
    print("Your Content")
    print(f.read())
    f.close()


def WriteOP(file):
    f = open(file, 'w')
    print("Erase Your Content Previous Content \nEnter New Content\n")
    s = input()
    print("total Character Count ", f.write(s))
    f.close()


def AppendOP(file):
    f = open(file, 'a')
    print("Add Your New Content")
    s = input()
    print("total Character Count ", f.write(s), "total Line Count ", f.writable())
    f.close()


def CreateNewFile(file):
    f = open(file, 'x')
    s = input()
    print("total Character Count ", f.write(s), "total Line Count ", f.writable())
    f.close()


def main():
    #    file = "Text.txt"
    #    ReadOP(file)
    #    WriteOP(file)
    #    ReadOP(file)
    #    AppendOP(file)
    #    ReadOP(file)
    file = "data.txt"
    CreateNewFile(file)
    ReadOP(file)


if __name__ == "__main__":
    main()
