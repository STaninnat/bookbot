
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    unique = get_txt_unique(text)
    count_unique = get_count_unique(text, unique)
    sorted_unique = sorted(count_unique.items(), key=get_sort_on, reverse=True)
    #unique_sentense = get_sentense(sorted_unique)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for nam in sorted_unique:
        print (f"The {nam[0]} character was found {nam[1]} times")
    print("--- End report ---")
    
      
def get_num_words(text):
    words = text.split()
    return len(words)

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

def get_sort_on(item):
    return item[1]

main()
