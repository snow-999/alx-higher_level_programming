#!/usr/bin/python3
"""sperated function"""


def text_indentation(text):
    """text indentation function
    args:
        text: that will be sperated by each delmeter
    raise:
    type error if text is not string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delm in ".?:":
        text = (delm + "\n\n").join(
            [line.strip(" ") for line in text.split(delm)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctset.testfile("tests/5-text_indentation.txt")
