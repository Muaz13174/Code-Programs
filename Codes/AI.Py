print("Hello! I am AI Bot. What's your name? :")
name = str(input())
print("Nice to meet you,",name + "!")
print("How do you feel today (good/bad)? :")
mood = str(input()).lower()
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes, it's hard to put feelings into words.")

print("It was nice chatting with you, " + name + ". Goodbye!")