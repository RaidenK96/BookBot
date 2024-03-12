def main():
    file_directory = "books/frankenstein.txt"
    with open(file_directory) as f:
        file_contents = f.read()
        print(f"---| Initializing report of {file_directory} |---")
        print("")
        print(f">Words found in the document: {count_words(file_contents)}")
        dict_counter_letter = count_letters_each(file_contents)
        dict_counter_letter_organized = organize_list(dict_counter_letter)
        print("")
        print(f">The {dict_counter_letter_organized[0]["letter"]} character was found {dict_counter_letter_organized[0]["num"]} times")
        print(f">The {dict_counter_letter_organized[1]["letter"]} character was found {dict_counter_letter_organized[1]["num"]} times")
        print(f">The {dict_counter_letter_organized[2]["letter"]} character was found {dict_counter_letter_organized[2]["num"]} times")
        print(f">The {dict_counter_letter_organized[3]["letter"]} character was found {dict_counter_letter_organized[3]["num"]} times")
        print(f">The {dict_counter_letter_organized[4]["letter"]} character was found {dict_counter_letter_organized[4]["num"]} times")
        print(f">The {dict_counter_letter_organized[5]["letter"]} character was found {dict_counter_letter_organized[5]["num"]} times")
        print(f">The {dict_counter_letter_organized[6]["letter"]} character was found {dict_counter_letter_organized[6]["num"]} times")
        print(f">The {dict_counter_letter_organized[7]["letter"]} character was found {dict_counter_letter_organized[7]["num"]} times")
        print(f">The {dict_counter_letter_organized[8]["letter"]} character was found {dict_counter_letter_organized[8]["num"]} times")
        print(f">The {dict_counter_letter_organized[9]["letter"]} character was found {dict_counter_letter_organized[9]["num"]} times")
        print(f">The {dict_counter_letter_organized[10]["letter"]} character was found {dict_counter_letter_organized[10]["num"]} times")
        print(f">The {dict_counter_letter_organized[11]["letter"]} character was found {dict_counter_letter_organized[11]["num"]} times")
        print(f">The {dict_counter_letter_organized[12]["letter"]} character was found {dict_counter_letter_organized[12]["num"]} times")
        print(f">The {dict_counter_letter_organized[13]["letter"]} character was found {dict_counter_letter_organized[13]["num"]} times")
        print(f">The {dict_counter_letter_organized[14]["letter"]} character was found {dict_counter_letter_organized[14]["num"]} times")
        print(f">The {dict_counter_letter_organized[15]["letter"]} character was found {dict_counter_letter_organized[15]["num"]} times")
        print(f">The {dict_counter_letter_organized[16]["letter"]} character was found {dict_counter_letter_organized[16]["num"]} times")
        print(f">The {dict_counter_letter_organized[17]["letter"]} character was found {dict_counter_letter_organized[17]["num"]} times")
        print(f">The {dict_counter_letter_organized[18]["letter"]} character was found {dict_counter_letter_organized[18]["num"]} times")
        print(f">The {dict_counter_letter_organized[19]["letter"]} character was found {dict_counter_letter_organized[19]["num"]} times")
        print(f">The {dict_counter_letter_organized[20]["letter"]} character was found {dict_counter_letter_organized[20]["num"]} times")
        print(f">The {dict_counter_letter_organized[21]["letter"]} character was found {dict_counter_letter_organized[21]["num"]} times")
        print(f">The {dict_counter_letter_organized[22]["letter"]} character was found {dict_counter_letter_organized[22]["num"]} times")
        print(f">The {dict_counter_letter_organized[23]["letter"]} character was found {dict_counter_letter_organized[23]["num"]} times")
        print(f">The {dict_counter_letter_organized[24]["letter"]} character was found {dict_counter_letter_organized[24]["num"]} times")
        print(f">The {dict_counter_letter_organized[25]["letter"]} character was found {dict_counter_letter_organized[25]["num"]} times")
        print("")
        print("---| End report |---")

def count_words(book):
        words = book.split()
        return len(words)

def count_letters_each(book):
    letters_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    book_lowered = book.lower()
    for word in book_lowered:
        if word == "a":
            letters_count["a"] += 1
        elif word == "b":
            letters_count["b"] += 1
        elif word == "c":
            letters_count["c"] += 1
        elif word == "d":
            letters_count["d"] += 1
        elif word == "e":
            letters_count["e"] += 1    
        elif word == "f":
            letters_count["f"] += 1
        elif word == "g":
            letters_count["g"] += 1
        elif word == "h":
            letters_count["h"] += 1
        elif word == "i":
            letters_count["i"] += 1
        elif word == "j":
            letters_count["j"] += 1
        elif word == "k":
            letters_count["k"] += 1
        elif word == "l":
            letters_count["l"] += 1
        elif word == "m":
            letters_count["m"] += 1
        elif word == "n":
            letters_count["n"] += 1
        elif word == "o":
            letters_count["o"] += 1
        elif word == "p":
            letters_count["p"] += 1
        elif word == "q":
            letters_count["q"] += 1
        elif word == "r":
            letters_count["r"] += 1
        elif word == "s":
            letters_count["s"] += 1
        elif word == "t":
            letters_count["t"] += 1
        elif word == "u":
            letters_count["u"] += 1
        elif word == "v":
            letters_count["v"] += 1
        elif word == "w":
            letters_count["w"] += 1
        elif word == "x":
            letters_count["x"] += 1
        elif word == "y":
            letters_count["y"] += 1
        elif word == "z":
            letters_count["z"] += 1

    return letters_count

def sort_on(letters_count):
    return letters_count["num"]

def organize_list(letters_count):
    letters_organized = [
        {"letter": "a", "num": letters_count.get("a", 0)},
        {"letter": "b", "num": letters_count.get("b", 0)},
        {"letter": "c", "num": letters_count.get("c", 0)},
        {"letter": "d", "num": letters_count.get("d", 0)},
        {"letter": "e", "num": letters_count.get("e", 0)},
        {"letter": "f", "num": letters_count.get("f", 0)},
        {"letter": "g", "num": letters_count.get("g", 0)},
        {"letter": "h", "num": letters_count.get("h", 0)},
        {"letter": "i", "num": letters_count.get("i", 0)},
        {"letter": "j", "num": letters_count.get("j", 0)},
        {"letter": "k", "num": letters_count.get("k", 0)},
        {"letter": "l", "num": letters_count.get("l", 0)},
        {"letter": "m", "num": letters_count.get("m", 0)},
        {"letter": "n", "num": letters_count.get("n", 0)},
        {"letter": "o", "num": letters_count.get("o", 0)},
        {"letter": "p", "num": letters_count.get("p", 0)},
        {"letter": "q", "num": letters_count.get("q", 0)},
        {"letter": "r", "num": letters_count.get("r", 0)},
        {"letter": "s", "num": letters_count.get("s", 0)},
        {"letter": "t", "num": letters_count.get("t", 0)},
        {"letter": "u", "num": letters_count.get("u", 0)},
        {"letter": "v", "num": letters_count.get("v", 0)},
        {"letter": "w", "num": letters_count.get("w", 0)},
        {"letter": "x", "num": letters_count.get("x", 0)},
        {"letter": "y", "num": letters_count.get("y", 0)},
        {"letter": "z", "num": letters_count.get("z", 0)},
    ]
    letters_organized.sort(reverse=True, key=sort_on)
    return letters_organized


main()