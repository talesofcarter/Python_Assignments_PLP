# Simple program to read a file and write a modified version to another file

# 1. First create the file
file = open('input.txt', 'w')
file.write('Hello world')
file.close()

print('input file created successfully!')

# 2. Open the file and read it
file = open('input.txt', 'r')
content = file.read()
file.close()

# 3. Modify the content 
modified_file = content.upper()

# 4. Modified content to a new file
output_file = open('output.txt', 'w')
output_file.write(modified_file)
output_file.close()

print("Completed successfully🎉")