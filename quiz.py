	
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

print has_teen(1,13,1) #True
print has_teen(1,1,1) #False
print has_teen(1,1,19) #True
print has_teen(13,1,1) #True
print has_teen(13,13,19) #True

# TODO - write not_string

def not_string(str):
	if str[:3] == "not":
		return str + "not"
	else:
		return "not" + str

print not_string("Tomato") #not Tomato
print not_string("not Tomato") #not Tomato not

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

def closer_to(g,i1,i2):
	if i1 == i2:
		return 0
	elif abs(g-i1) < abs(g-i2):
		return i1
	elif abs(g-i1) > abs(g-i2):
		return i2

print closer_to(1,2,3)
print closer_to(1,2,2)
print closer_to(1,3,2)
# TODO - write two_as_one

def two_as_one(v1,v2,v3):
	if v1+v2==v3 or v3+v2==v1 or v1+v3==v2:
		return True
	else:
		return False

print two_as_one(1,2,3)
print two_as_one(1,2,1)
print two_as_one(1,2,5)
print two_as_one(5,2,3)