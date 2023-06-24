# Write a Python program to count the occurrences of each word in a given sentence 

def count (str): #decler a function(count is function) and  pass one perameter, str in name of parameter 

    counts = {} #create a  dictnory it is a empty 
    sentence = str.split() # 

    for i in sentence:# loop is execute and check the condition / sentence store in i variable.
        if i in counts:# loop is is execute and check the condition 
            counts[i] += 1 # count a word and store in counts variable
        else:
            counts[i] = 1# word store in counts variable
    return counts # return in counts

# function calling
sentence = input("Enter your sentence : ")# crete variable and accept value from user.
print(count(sentence))# print and count sentence
