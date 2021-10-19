def number_of_lines(filename):
    f = open(filename, 'r')
    linje = f.readline()
    teller = 0
    while linje:
        linje = f.readline()
        teller += 1
    f.close()
    return teller

a = number_of_lines('numbers.txt')
print("lines: ",a,"\n")

def number_frequency(filename):
    num_freq = {}
    f = open(filename, 'r')
    linje = f.readline()
    while linje:
        if int(linje.strip()) in num_freq:
            num_freq[int(linje.strip())] += 1
        else:   num_freq[int(linje.strip())] = 1
        linje = f.readline()
    f.close()
    return num_freq

def print_fint(dictionarius):
    for key,value in dictionarius.items():
        print(key," ::: ", value)

c = number_frequency('numbers.txt')
print_fint(c)


