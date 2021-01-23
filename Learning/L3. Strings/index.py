a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# Strings are array
variable_string = "Le Tang Co"

print(variable_string[0])
# Length strings
print(len(variable_string))
# Check argument is exists
print('Tang' not in variable_string)
# Or
if 'Tang' in variable_string:
    print("Yes, 'Tang' is exist")
else:
    print('No, not exists')


for x in variable_string:
    print(x)