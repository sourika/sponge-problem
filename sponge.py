def sponge_case(sentence):
    lst_words = sentence.split()
    new_lst = []

    for word in lst_words:
        new_lst.append(convert(word))

    return " ".join(new_lst)    


def convert(word):
    converted_lst =[]

    for i in range(len(word)):
        if i % 2 == 0:
            converted_lst.append(word[i].lower())
        else:
            converted_lst.append(word[i].upper())
    
    return "".join(converted_lst)            


# Test cases
assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")