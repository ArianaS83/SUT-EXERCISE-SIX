def sort_and_print_first_char(txt):
    words = txt.split(' ')
    sorted_words = sorted(words, key=lambda x: int(x[1:]))
    
    for word in sorted_words:
        print(word[0], end='')

def main():
    user_input = str(input("Enter space-separated words: "))
    sort_and_print_first_char(user_input)

if __name__ == "__main__":
    main()
