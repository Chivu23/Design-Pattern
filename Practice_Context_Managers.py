
# INTERACTION WITH FILES

f = open("Practice_Text_File.txt", "r")
print(f.read())
f.close()

# What happens if errors occur before we close the file??
# f = open('Practice_Text_File.txt', 'r')
# if aaaaaa:
#     print("doing something")
# f.close()
# an error occurs in the code before the file is closed -> the file will NOT be closed NEVER !!!
# -> we consume resources + data remains vulnerable/exposed!

# How can we improve the code above?

# VAR 1:
# - we use block try except + finally
# f = open('Practice_Text_File.txt', 'r')
# try:
#     print(f.read())
#     if aaaaa:
#         print("doing something")
# except Exception:
#     print("this is exception")
# finally:
#     print("close the file ___ FORCE")
#     f.close()

# VAR 2 the way to do
# USE de CONTEXT MANAGERS -> with statement

with open('Practice_Text_File.txt', 'r') as f:
    # variable f represents the result of the expression called in
    # the "with" block and is available inside the "with" block
    print("we are in the 'with' block")
    print(f.read())
print("we are outside of 'with' block")
# print(f.read())
# -> ERROR,
# when we left the block "with", the file is no longer open!


class File:

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with File('Practice_Text_File.txt', 'r') as file:
    print(file.read())

print("here")