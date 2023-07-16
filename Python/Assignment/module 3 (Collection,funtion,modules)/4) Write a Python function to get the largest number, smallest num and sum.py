#  Write a Python function to get the largest number, smallest num and sum of all from a list. 
l1 = [12,23,54,66,55,99,90,200,100,345,56,78,34]

def smallest(l1):
    largest = min(l1)
    return largest
def largest(l1):
    largest = max(l1)
    return largest
def sum_all(l1):
    largest = sum(l1)
    return largest

print("smallest number of all from a list : ",smallest(l1))
print("largest number of all from a list : ",largest(l1))
print("sum number of all from a list : ",sum_all(l1))


