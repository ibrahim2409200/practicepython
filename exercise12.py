#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.
def list_ends(a_lists):
    return [a_lists[0],a_lists[len(a_lists)-1]]
a_lists=[5,10,15,20,25]
print(list_ends(a_lists))