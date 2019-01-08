#learning python the hard way
#ex5.py
'''
Ex5: More Variables and Printing
- using a "format string"
- learning how to make strings that have variables embedded in them.
	-- this is done by using spec format sequences and then putting the variable
		at the end with special syntax, telling python this is a format string.
'''


my_name = 'Eric J. Knickmeyer'
my_age = 23 #Jordan year
my_height = 72 # inches...more or less
my_weight = 160 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_hair

#tricky line of code... I made a mistake.
print "if I add %d, %d, and %d I get %d." % (# <-- before this was where my mistake was!!!!
my_age, my_height, my_weight, my_age + my_height + my_weight)

# ---------------------------------------------------------------------------

name = 'Eric J. Knickmeyer'
age = 23
height = 72
weight = 160
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


