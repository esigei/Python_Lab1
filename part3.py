python = ['Alex', 'Ahmed', 'Desai', 'Kumar', 'Vinay','Raju', 'Jeff', 'Harshini' ]
web_app = ['Desai', 'Kumar', 'Tasnin', 'Aihan', 'Trinh', 'Xie', 'Zubair']
# used a similiar list comprehension as used for part2
python_only = [i for i in python if not i in web_app]
print('Python Students:')
print(python,'\n')
print('Web App Students:')
print(web_app,'\n')
print('Python only students:')
print(python_only)