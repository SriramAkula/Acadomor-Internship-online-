#Write a program that takes a list of elements and counts how many times each element occurs using a dictionary.
def count_occurrences(elements):
    counts = {}
    for element in elements:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    
    return counts

user_input = input("Enter elements separated by spaces: ").split()
elements = [element for element in user_input if element]
result = count_occurrences(user_input)

print(result)
