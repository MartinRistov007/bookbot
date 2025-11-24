def count_words(contents):
    words = contents.split()
    counter = 0
    for word in words:
        counter += 1

    return counter

def count_characters(contents):
    character_dictionary = {}

    for character in contents:
        try:
            character_dictionary[character.lower()] += 1
        except KeyError:
            character_dictionary[character.lower()] = 1

    return character_dictionary 

def get_book_text(path_to_file):
    try:
        with open(path_to_file) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File not found. Make sure path is correct! You inputted: {path_to_file}")
        return None
    except PermissionError:
        print("Error: You do not have permission to open this file.")
        return None
    except IOError as e:
        print(f"An general I/O error has occurred: {e}")
        return None
    
    return file_contents

def sort_on(count):
    return count["num"]

def sort_dictionary(character_dictionary):
    dictionary_list = []


    for key, value in character_dictionary.items():
        specific_dictionary = {"char" : key, "num" : value}

        dictionary_list.append(specific_dictionary)

    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list


