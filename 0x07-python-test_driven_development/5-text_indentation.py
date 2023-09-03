#!/usr/bin/python3
def text_indentation(text):
    """Write a function that prints a text with 2 new lines
      after each of these characters: ., ? and :
      Args: Text (str) must be a string,
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        sentence = ""
        for char in text:
            sentence += char
            if char in ['.', ':', '?']:
                print(sentence.strip())
                print()
                sentence = ""
        if sentence:
            print(sentence.strip(), end="")
