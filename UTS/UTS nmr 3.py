def max_cap(text):
    maks = ""
    for char in text:
        if ((ord("A") <= ord(char) <= ord("Z"))and char > maks):
            maks = char
    if(maks!=""):
        return maks
print(max_cap("belAjaR PyThon DengaN geMBira"))
print(max_cap("belajar python dengan gembira"))
