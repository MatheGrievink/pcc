filename = 'chapter10/TRY/10.1_learning_python/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in file_object:
    print(line.strip())