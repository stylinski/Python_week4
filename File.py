#creating a new file
file = open("newfile.pdf", "w")
file.write("Hello, this is week 4 assignment.")

#Reading the file
file = open("newfile.pdf", "r")
data = file.readline()
print(data)

#writing a modified version  to a new file
file = open("output.txt", "w")
file.write(data.upper())

#Ask the user for a filename
filename = input("Please enter a filename: ")

#handle errors if it doesn’t exist or can’t be read.
try:
    file = open(filename, "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You don’t have permission to read this file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File Operation Complete.")
