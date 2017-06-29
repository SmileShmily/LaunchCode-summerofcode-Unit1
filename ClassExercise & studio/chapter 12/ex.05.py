'''Here’s a table of English to Pirate translations
English
Pirate
sir
matey
hotel
fleabag inn
student
swabbie
boy
matey
madam
proud beauty
professor
foul blaggart
restaurant
galley
your
yer
excuse
arr
students
swabbies
are
be
lawyer
foul blaggart
the
th’
restroom
head
my
me
hello
avast
is
be
man
matey
Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.'''

'''
pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['restaurant'] = 'galley'
#and so on

sentence = input("Please enter a sentence in English")

psentence = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print((" ").join(psentence))
'''
'''
def main():

	input_sentence = raw_input("What would you like to translate? ")
	word_list = []


	def piratize(input_sentence):

		input_sentence.split()
		for i in range(0,):
			if input_sentence[i] == "sir":
				input_sentence[i] = "matey"
			if input_sentence[i] == "hotel":
				input_sentence[i] = "fleabag inn"
			if input_sentence[i] == "student":
				input_sentence[i] = "swabbie"
			if input_sentence[i] == "boy":
				input_sentence[i] = "matey"
			if input_sentence[i] == "madam":
				input_sentence[i] = "porud beauty"
			if input_sentence[i] == "professor":
				input_sentence[i] = "foul braggart"
			if input_sentence[i] == "retaurant":
				input_sentence[i] = "galley"
			if input_sentence[i] == "your":
				input_sentence[i] = "yer"
			if input_sentence[i] == "are":
				input_sentence[i] = "be"
			if input_sentence[i] == "the":
				input_sentence[i] = "th'"
			if input_sentence[i] == "my":
				input_sentence[i] = "me"
			if input_sentence[i] == "is":
				input_sentence[i] = "be"

		print( input_sentence)
		return input_sentence
	translation = piratize(input_sentence)
	print (translation)

if __name__ == "__main__":
              main()
              '''


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
    print(choice(start) + \
          ' '.join([d[i] if i in d else i for i in s.lower().split()]).capitalize() \
          + choice(end))


if __name__ == "__main__":
# ~ s = "i like pie, it's very nice, yes indeed, it is. banana"
# ~ print count_all(s)
# ~ create_bar(s)
# ~ counted_table(s)
# ~ makeitwork()
# ~ alice_in_wonderland()
    pirate()


'''from test import testEqual

def translate(text):
        # your code here!
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
                 "hello my man, please excuse your professor to the restroom!",
                 "Always remember you're unique, just like everyone else"]

    start = ["Yarr, ", "Yarr! ", "Yarr-ha-harr! ", "Skuttle me Skippers! ",
             "Shiver me timbers! ", "Ahoy, me hearties! ", "Dogs ahoy! ",
             "Hoist the mizzen!!! ", "Hoist the colors!! "]
    end = [". ARRRGHHHH!", ". Avast ye varmint!", ". Yarr?",
           ". Savvyy?", ". Yarr!", ". Aye!",
           ", ye bilge rat!", ", ye mangy dog!", ", ye scallywag!"]

    s = choice(sentences)
    print(s)
    print(choice(start) + \
          ' '.join([d[i] if i in d else i for i in s.lower().split()]).capitalize() \
          + choice(end))


#if __name__ == "__main__":
# ~ s = "i like pie, it's very nice, yes indeed, it is. banana"
# ~ print count_all(s)
# ~ create_bar(s)
# ~ counted_table(s)
# ~ makeitwork()
# ~ alice_in_wonderland()
   # translate(text)

text = "hello my man, please excuse your professor to the restroom!"
testEqual(translate(text), "avast me matey, please arr your foul blaggart to the head!")
'''
