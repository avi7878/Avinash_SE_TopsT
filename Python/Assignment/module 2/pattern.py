m = int(input("Enter the start number: "))
# k = int(input("Enter the end number: "))

# while i <= k:
#     b = 1
#     while b <= k - i:
#         print(" ", end=" ")
#         b += 1

#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     j+=2
#     print()
#     i += 1

for i in range(m):
    for j in range(i,m):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
