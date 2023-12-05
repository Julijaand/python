file_name = input("Enter file name: ")

def read_file(file_name):
    try:
        with open(file_name, 'r') as o_f:
            content = o_f.read()
            return content
    except FileNotFoundError:
        return "File not found"
print (read_file(file_name))