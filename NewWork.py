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

# More stuff  10-8

print("Mary had a little lamb")
print("It's fleece was white as %s" % 'snow')
print("And every where that mary went.")
print("." * 10)

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
print(formatter %(1,2,3,4))
print(formatter % ("one", "two", "three" , "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))

# Why did I use %r instead of %s
("%r displays the contents that the variables represent while %s converts coding to a string.")

#Time foe some strange stuff in the world of printin...

days= "Mon Tue Wed Thu Fri Sat Sun"
months="Jan\Feb\Mar\Apr\May\Jun\Jul\Aug\Sep\Oct\Nov\Dec"

print("Here are the days" , days)
print("here are the months" ,months)



