# Requests text from user.
# Alternating Letters splits the text so that each character in the text alternates between uppercase and lowercase. E.g. "HeLlO WoRlD"
# Alternating Words splits the text so that each word in the text alternates between lowercase and uppercase. E.g. "hello WORLD"

def main():

    text = input("Enter some text: ").strip()
    split_text = text.split()

    alternating_letters_text = alternating_letters(split_text)
    print(f"Alternating Letters: {alternating_letters_text}")

    alternating_words_text = alternating_words(split_text)
    print(f"Alternating Words: {alternating_words_text}")


def alternating_letters(split_text):

# Iterates through each word in text, then iterates through each character in each word
# If modulus with remainder = 0, converts character to uppercase, else converts character to lowercase
# split_text[0][0] represents the first character of the first word and so on
# Each new word is appended to a list, then printed using the join() method.
    
    alternating_letters_list = []

    for word in range(len(split_text)):
        new_text = ""
        for character in range(len(split_text[word])):

            if character % 2 == 0:
                new_text += (split_text[word][character].upper())
            else:
                new_text += (split_text[word][character].lower())
    
        alternating_letters_list.append(new_text)

    alternating_letters = " ".join(alternating_letters_list)

    return alternating_letters

def alternating_words(split_text):

# Iterates through each word in text
# If modulus with remainder = 0, converts word to lowercase, else converts word to uppercase
# Each new word is appended to a list, then printed using the join() method.

    alternating_words_list = []

    for word in range(len(split_text)):

        if word % 2 == 0:
            alternating_words_list.append(split_text[word].lower())
        else:
            alternating_words_list.append(split_text[word].upper())

    alternating_words = " ".join(alternating_words_list)

    return alternating_words

main()