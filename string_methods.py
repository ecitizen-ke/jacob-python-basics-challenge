'''
String Methods:
- Create a string variable containing a sentence with multiple words.
- Use string methods to count the number of occurrences of the letter 'a' in the sentence.
- Replace all occurrences of the letter 'a' with 'z' and print the modified sentence.
'''

string_sentence = "My name is Jacob Gimachombe Mwita. I am learning python programming language."
letter_count = string_sentence.count("a")

print(letter_count)

replace_letter = string_sentence.replace("a", "z")
print(replace_letter)
