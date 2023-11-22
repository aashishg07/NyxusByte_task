sentence = input("Enter the sentence: ")

sentence = sentence.lower()

vowel_count = 0

for char in sentence:
    if char in "aeiou":
        vowel_count += 1

print(f"The vowel in the sentence are: {vowel_count}")