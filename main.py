book_path = "books/frankenstein.txt"
with open(book_path) as f:
    file_contents = f.read()
book_words = file_contents.split()
book_letters = [l for l in file_contents]


def word_countinator(words: str=book_words) -> int:
    counter = 0
    for word in words:
        counter += 1
    return counter

def get_letter_dict_count(file_contents: str=file_contents) -> dict:
    letters = [l for l in file_contents]
    letter_list = []
    letter_dict= {}
    for letter in letters:
        if letter.lower() in letter_dict.keys():
            letter_dict[letter.lower()] += 1
        else:
            letter_dict[letter.lower()] = 1
    return letter_dict

def get_letter_list(file_contents: str = file_contents) -> list:
    letter_list = []
    letter_dict = get_letter_dict_count()
    for k,v in letter_dict.items():
        letter_list.append({"letter":k, "count":v})
    return letter_list


def sort_on(dict) -> list:
    return dict["count"]

def print_reportinator(file_contents: str = file_contents) -> str:
    letter_list = get_letter_list(file_contents)
    letter_list.sort(key=sort_on, reverse=True)
    report = ""
    report += f"--- Begin report of {book_path} ---\n"
    report += f"{word_countinator()} words found in the document\n\n"
    for l in letter_list:
        if l['letter'].isalpha():
            report += f"The '{l['letter']} character was found {l['count']} times\n"
    report += "--- End report ---"
    print(report)
    return report

if __name__ == "__main__":
    print_reportinator()
    pass

