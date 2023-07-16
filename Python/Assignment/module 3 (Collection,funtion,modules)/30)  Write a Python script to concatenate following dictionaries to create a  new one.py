#  Write a Python script to concatenate following dictionaries to create a new one.

dict1 = {'python': 85, 'marks': 60, 'name': 'avinash', 'tops': 5   }
dict2 = {'java': 100, 'cpp': 78, 'php': 'jay'}
dict3 = {'nord.js': 78, '.net': 80, 'city': 'somnath'}

concate_dic = {}

for i in (dict1,dict2,dict3):
    concate_dic.update(i)

print(concate_dic)
