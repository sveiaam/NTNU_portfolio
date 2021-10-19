my_family = {}


def add_family_member(role, name):
    if role not in my_family:
        my_family[role] = [name]
    else:
        my_family[role].append(name)

def print_fint():
    for key,value in my_family.items():
        print(key," ::: ", value)

def main():
    while True:
        rel = input("\nRelasjon: ")
        if rel == '':
            break
        navn = input("Navn: ")
        add_family_member(rel, navn)
    print_fint()



main()
