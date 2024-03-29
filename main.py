
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    #####################################################
    unique = get_txt_unique(text)
    count_unique = get_count_unique(text, unique)
    print(count_unique)
       
def get_num_words(text):
    words = text.split()
    return words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_txt_unique(text):
    unique = set()  
    lower_txt = text.lower()
    for char in text:
        for i in range(97,123):
            if char == chr(i):
                unique.add(char)
    return unique
    
def get_count_unique(text, unique):
    output = {}
    lower_txt = text.lower()
    for char in unique:
        count = 0
        count = lower_txt.count(char)
        output[char] = count
    return output

main()
