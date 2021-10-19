def recursive_sum(n):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    elif n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)

#Sammenligner de to første elementer i en liste, fjerner det største av disse og kaller på seg selv med oppdatert liste.
def find_smallest_element(numbers):
    if len(numbers) > 1:
        if numbers[0] > numbers[1]:
            numbers.pop(numbers.index(numbers[0]))
            return find_smallest_element(numbers)
        elif numbers[0] < numbers[1]:
            numbers.pop(numbers.index(numbers[1]))
            return find_smallest_element(numbers)
        else:
            numbers.pop(numbers.index(numbers[1]))
            return find_smallest_element(numbers)
    else:
        return numbers[0]

#Ser om element er midtpunkt. Hvis element > midtpunkt, rekurser med øvre halvdel. Omvendt i omvendt tilfelle.
def binary_search(numbers, element):
    halvlengde = len(numbers)//2
    if element == numbers[halvlengde]:
        return numbers.index(numbers[halvlengde])
    elif numbers[0] == numbers[-1]:
        return -float('inf')
    else:
        low_list = numbers[:halvlengde:]
        high_list = numbers[halvlengde::]
        if element > high_list[0]:
            return halvlengde + binary_search(high_list, element)
        elif element < high_list[0]:
            return halvlengde - (halvlengde - binary_search(low_list, element))


print(binary_search([1,5,8,9,10,11,18,21,34,35],35))
