import random
noun_list = ["dog", "cat", "giraffe", "computer", "donut", "water", "Phone", "Laptop", "Train", "Airplane", "House"]
verb_list = ["run", "jump", "swim", "play", "watch", "kill", "cry", "make", "fall", "dive"]
adjectives_list = ["beautiful", "scary", "red", "ugly", "brave", "calm", "faithful", "happy", "sad", "smart"]
adverb_list = ["lazily", "quickly", "happily", "gleefully", "sadly", "energetically", "crazily", "skillfully", "wisely", "dejectdly"]
preposition_list = ["on", "over", "under", "behind", "next to", "between", "over"]
article_list = ["a", "the"]

#make myself a function for generating noun phrases
def noun_phrase():
    return random.choice(article_list) + " " + random.choice(adjectives_list) + " " + random.choice(noun_list)



#try out noun phrase generator a few times
print(noun_phrase())
print(noun_phrase())
print(noun_phrase())


def verb_phrase():
    return random.choice(adverb_list) + " " + random.choice(verb_list)
print(verb_phrase())
print(verb_phrase())
print(verb_phrase())

def preposition_phrase():
    return random.choice(preposition_list) + " " + noun_phrase()
print(preposition_phrase())
print(preposition_phrase())
print(preposition_phrase())

def sentence():
    return noun_phrase() + " " + verb_phrase() + " " + preposition_phrase()
print (sentence())
print (sentence())
