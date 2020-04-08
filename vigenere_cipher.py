alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decoder(text, keyword):
    pointer = 0
    new_keyword = ""
    decoded_text = ""
    for i in (range(len(text))):
        if text[i] == " ":
            new_keyword += " "
            decoded_text += " "
        else:
            new_keyword += keyword[pointer]
            pointer = (pointer+1)%len(keyword)
            key = alphabet.find(text[i]) - alphabet.find(new_keyword[i])
            decoded_text += alphabet[key%26]
    return decoded_text


def coder(text, keyword):
    pointer = 0
    new_keyword = ""
    coded_text = ""

    for i in (range(len(text))):
        if text[i] == " ":
            new_keyword += " "
            coded_text += " "
        else:
            new_keyword += keyword[pointer]
            pointer = (pointer+1)%len(keyword)
            key = alphabet.find(text[i]) + alphabet.find(new_keyword[i])
            coded_text += alphabet[key%26]
    return coded_text

print(coder("THIS IS MY KEY", "KEY"))
print(decoder("DLGC MQ WC IOC", "KEY"))
