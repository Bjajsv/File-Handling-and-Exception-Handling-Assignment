#open(filename, mode) 
f = open("example.txt", "r") # Opens the file in read mode
print(f.name)
print(f.mode)
print(f.read)


f.close()
#method 2
with open("example.txt", "r") as f:
    content_s = f.readline() 
    print(content_s, end="")


#method 3
with open('example.txt', 'w') as f:
    wordz = f.write()
    print(wordz, end='')

#method 4
with open('example.txt' , 'r') as f:
    for line in f
    print(line, end='')

#Error handling 

try:
    with open('example.txt', 'r') as f:
        print(f.mode)
except FileNotFoundError
print("File Not Found")
