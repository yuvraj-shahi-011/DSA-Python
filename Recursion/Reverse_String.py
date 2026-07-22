def reverse(text):
    if len(text) == 0:
        return ""
    return reverse(text[1:]) + text[0]
text = input("Enter a string: ")
print("Reversed:", reverse(text))