# Creating strings
greeting = "Hello, World!"
name = 'Alice'


# Changing case
print(greeting.upper())  # "HELLO, WORLD!"
print(greeting.lower())  # "hello, world!"
print(greeting.title())  # "Hello, World!"

# Removing whitespace
text = "   Hello, Python!   "
print(text.strip())  # "Hello, Python!"

# Replacing substrings
modified_text = greeting.replace("World", "Alice")
print(modified_text)  # "Hello, Alice!"


# Counting occurrences
count_o = greeting.count("o")  # 2