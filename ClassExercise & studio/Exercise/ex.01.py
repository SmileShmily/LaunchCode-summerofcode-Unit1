''' Write a program that asks the user for a sentence in English and then
    translates that sentence to Pirate.'''


def pirate():
    """Write a program that asks the user for a sentence in English and then
    translates that sentence to Pirate."""

    from random import choice
    d = {
        "sir": "matey", "hotel": "fleabag inn", "student": "swabbie",
        "boy": "matey", "girl": "wench", "professor": "foul blaggart",
        "restaurant": "galley", "your": "ye", "excuse": "arr", "you": "ye",
        "students": "swabbies", "are": "be", "lawyer": "foul blaggart",
        "the": "th'", "restroom": "head", "my": "me", "hello": "avast",
        "is": "be", "man": "scurvy dog", "hey": "avast", "pirate": "scurvy pirate",
        "idiot": "flunder", "young": "ye", "the": "t'", "suck": "blow down",
        "fall": "hade", "happens": "be happening", "death": "Davy Jones' treasure chest",
        "always": "ever", "you're": "ye're", "girlfriend": "Lassie-Lucy",
        "with": "wit'", "everyone": "evr'un"
    }
    # ~ sentence = raw_input("What be yer sentence, ye old landlubber? ")
    sentences = ["If the world didn't suck we'd all fall off",
                 "What happens if you get scared half to death twice?",
                 "Save water and shower with your girlfriend",
                 "Always remember you're unique, just like everyone else"]

    start = ["Yarr, ", "Yarr! ", "Yarr-ha-harr! ", "Skuttle me Skippers! ",
             "Shiver me timbers! ", "Ahoy, me hearties! ", "Dogs ahoy! ",
             "Hoist the mizzen!!! ", "Hoist the colors!! "]
    end = [". ARRRGHHHH!", ". Avast ye varmint!", ". Yarr?",
           ". Savvyy?", ". Yarr!", ". Aye!",
           ", ye bilge rat!", ", ye mangy dog!", ", ye scallywag!"]

    s = choice(sentences)
    print(s)
    print(
    choice(start) + \
    ' '.join([d[i] if i in d else i for i in s.lower().split()]).capitalize() \
    + choice(end))
#if __name__ == "__main__":
s = "i like pie, it's very nice, yes indeed, it is. banana"
'''print(count_all(s))
create_bar(s)
counted_table(s)
makeitwork()
alice_in_wonderland()
pirate()'''