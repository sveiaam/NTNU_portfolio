def write_to_file(data):
    f = open('my_file.txt','a')
    f.write(data)
    f.write("\n")
    f.close()

def read_from_file(filename):
    f = open(filename,'r')
    print(f.read())
    f.close()

def reset_file():
    f = open('my_file.txt','w')
    f.close()

def main():
    reset_file()
    svar = 'readwrite'
    while svar != 'done':
        svar = input("Do you want to read or write? ::: ")
        if svar == 'write':
            skriving = input("What do you want to write? ::: ")
            write_to_file(skriving)
            print(skriving,"::: has been written to file.\n")
        if svar == 'read':
            print()
            read_from_file('my_file.txt')
            print()
    print("\n:::::::::\nYou are done.\n:::::::::\n")

main()

