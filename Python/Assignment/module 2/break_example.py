"""
break : break is a statement which is used to execute at looping tine.

using of break statement we can break the statement.

syntax :


for i in range(1,6):
    if condition:
        break
"""

for i in range(1,6):
    marks = int(input("Enter your marks : "))
    if marks>=35:
        print("pass")
    else:
        print("Fail")
        break
    