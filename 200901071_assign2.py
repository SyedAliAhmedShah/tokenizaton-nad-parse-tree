import ast
import re
string = input("Expression: ")
print("Original string : " + str(string))
token = re.split('', string)
print("After spliting string: " + str(token))
code = ast.parse(string)
print(ast.dump(code, indent=4))