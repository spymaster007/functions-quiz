	
# TODO - write has_teen
def has_teen(a,b,c):
	if a <= 19 and a >= 13:
		return True
	elif b <= 19 and b >= 13:
		return True
	elif c <= 19 and c >= 13:
		return True
	else:
		return False
		
print has_teen(1,13,1)
print has_teen(1,1,1)
print has_teen(1,1,19)
print has_teen(13,1,1)
print has_teen(13,13,19)

# TODO - write not_string
def not_string(str):
	if str[:3] == "not":
		return str + " not"
	else:
		return "not " + str

print not_string("Tomato")
print not_string("not Tomato")

# TODO - write icy_hot
def icy_hot(t1,t2):
	if t1>100 or t2>100:
		if t1<0 or t2<0:
			return True
		else:
			return False
	else:
		return False

print icy_hot(-1,101)
print icy_hot(1,10)
print icy_hot(1,101)
print icy_hot(-1,10)
# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
