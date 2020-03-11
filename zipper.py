import os


def main():
    f = open("new_file.txt","w")
    f.write("'Hello There'\n'General Kenobi!'")
    f.close()

    with open("new_file_2.txt", "w") as f:
    # f = open("new_file_2.txt", "w")
        f.write("OH HELLO THERE!!!")

    f = open('new_file.txt')
    print(f.read())
    f.close()

    # os.startfile('new_file.txt')











if __name__ == "__main__":
    main()
