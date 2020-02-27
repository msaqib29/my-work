#strings and output

msg = 'you said "hi"'

print(msg)

#lists

pets = ["dog", "cat", "fish"]

thepet = pets[1]

print(thepet)

#length & types

size = len(pets)

msg = "there are " + str(size) + " pets"

print(msg)

#loops

for anml in pets:
    print("I wish I had a " + anml)
    
#user input

ans = input("What kind of pet do you have?")

print("you have a " + ans)


#booleans i.e. TRUE or FALSE

known = ans in pets
print (known)
print ("it is " + str(known) + " that I have seen a " + ans)


#branching

if known:
    msg = "My friend has a " + ans
else:
    msg = "I don't have anyone with a " + ans
print(msg)


#dictionary

feels = {"cat":"selfish", "dog":"loyal", "fish":"wet"}
if known:
    pre = "e" if ans == "fish" else ""
    msg = ans + pre + "s are very " + feels.get(ans)
else:
    msg = "I don't know anyone with a " + ans

print(msg)
