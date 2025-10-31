def display_chars(file_path, num_chars):
    with open(file_path) as file:
        content=file.read(num_chars)
        print(f"The first {num_chars} characters are:")
        print(content)

def display_line(file_path):
    with open(file_path) as file:
        content=file.readline()
        print(f"The first line is:")
        print(content)





def display_text(file_path):
    with open(file_path) as file:
        content=file.read()
        print("The full text is:")
        print(content)




def runtask2():
    display_text('library.txt')
    display_line('library.txt')
    display_chars('library.txt', num_chars=8)

if __name__ == '__main__':
    runtask2()











