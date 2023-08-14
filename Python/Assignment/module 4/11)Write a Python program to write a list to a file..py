# Write a Python program to write a list to a file.

sub = ['Python', 'Java', 'React Js', 'Node Js', 'Andriod', 'Html']
with open("tops.txt", "a") as myfile:
        for i in sub:
                myfile.write("\n"+i)

content = open("tops.txt")
print(content.read())