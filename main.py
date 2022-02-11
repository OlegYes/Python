f = open('print_text.py', 'r')

print(eval(f.readlines()))
f.close()

# with open('print_text.py', 'r') as f:
#     lines = f.readlines()
#     commands = ""
#     for line in lines:
#         commands = commands + line.replace("\n", "; ")
#     print(commands)
#     eval(commands)
