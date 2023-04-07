sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

#Replace the ! in sentence with a space
sentence_replace = sentence.replace("!", " ")
#Remove the space between dog and .
sentence_replace = sentence_replace.replace("dog .", "dog.")
print(f"sentence.replace('!', ' '): {sentence_replace}")

# Convert sentence_replace to uppercase
sentence_upper = sentence_replace.upper()
print(f"sentence.upper(): {sentence_upper}")

# Print sentence_upper in reverse
sentence_upper_reverse = sentence_upper[::-1]
print(f"sentence reversed[::-1]: {sentence_upper_reverse}")