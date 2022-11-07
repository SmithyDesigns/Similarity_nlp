import spacy
import numpy as np

nlp = spacy.load("en")

# Creating an empty dictionary
d = {}

# Reading file
my_file = open("movies. txt").read()
my_file = my_file.split('\n')
my_file.pop()

# Saving contents of file in a dictionary
for i in my_file:
    d[i.split(":")[0]] = i.split(":")[1]

l1 = []
for i in d.values():
    sentence_to_compare = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth," 
                          "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the"
                          "Hulk can live in peace.",
                          "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as" 
                          "a gladiator."""

    model_sentences = nlp(sentence_to_compare)

    # Comparing each movie description with the given description to find the closest similarity
    similarity = nlp(i).similarity(model_sentences)
    print(i + "-" + str(similarity))
    l1.append(similarity)
movie_title = []
for i in d.keys():
    movie_title.append(i)

# Printing the movie title
print(movie_title[l1.index(max(l1))])
