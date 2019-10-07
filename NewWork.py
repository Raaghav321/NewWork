# making a joke using variables.

x= "There are %d types of people" %10
binary="binary"
doNot = "don't"
y = "Those who know %s and those who %s" % (binary, doNot)

# Actually making the joke.

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s ." % y)

hilarious = False
joke_evalution = "isn't that funny?! %r"
print(joke_evalution % hilarious)

# making a sentence using variables and plugging them in.

w="This is the left side of..."
e="a string with a right side"

print(w+e)
