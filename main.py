def main():
    word = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    word = file_contents.split()
    print(len(word))
main()
