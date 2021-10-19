print("\n\noppg a\n\n")

def check_equal(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

str1 = 'hei'
str2 = 'hello'
str3 = 'hello'
print(check_equal(str1, str2))
print(check_equal(str3, str2))

print("\n\noppg b\n\n")

def reversed_word(str):
    temp_liste_reversed = []
    for i in str:
        temp_liste_reversed.insert(0,i)
    return ''.join(temp_liste_reversed)
#return str[::-1]

str = 'Morna Jens'
print(reversed_word(str))

print("\n\noppg c\n\n")

def check_palindrome(str):
    a = str
    b = reversed_word(str)
    return check_equal(a,b)

str1 = 'agnes i senga'
str2 = 'hello'
print(check_palindrome(str1))
print(check_palindrome(str2))

print("\n\noppg d\n\n")

def contains_string(str1, str2):
    return str1.find(str2)

str1 = 'pepperkake'
str2 = 'per'
str3 = 'ola'
print(contains_string(str1, str2))
print(contains_string(str1, str3))
