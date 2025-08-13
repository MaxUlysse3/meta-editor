import music_tag as mtag
import os

def menu():
    print("\n" * 2)
    print("Welcome to meta-editor !")
    print("\n")
    while True:
        res = input("What do yout want to do ? (type 'help' for help) : ")
        if res == "ex":
            print("Goodbye!")
            exit()
        elif res == "help":
            help_menu()
            continue
        elif res == "bk":
            path = input("Path to the folder to edit ? : ")
            bulk_edit(path)
        else:
            print("Not a command")
            continue


def help_menu():
    print("List of commands : ")
    print("ex -- Exit the program")
    print("bk -- Edit the metadatas of a whole folder")

def bulk_edit(path):
    print("Type 'exit' to exit")
    files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    print(files)
    while (res := "") != "exit":
        res = input("Enter the name of the metadata you want to edit : ")
        if res == "exit":
            break
        else: 
            val = input("The value of the metadata : ")
            for f in files:
                edit_one(f, res, val)

def edit_one(path, field, val):
    f = mtag.load_file(path)
    f[field] = val
    print(field)
    print(val)
    f.save()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        exit()
