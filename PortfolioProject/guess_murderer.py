from info import evidence1, functions

# Guess The Murderer!
name = input("What is your name detective?: ")
print(" ======== Guess the Murderer: Act 1 ========", "\n")
print("Good evening detective", name,
      "Someone has been murdered. Bryan Johnson's body has been found in his bedroom. He's been stabbed 3 times.")
print(" Case: Find the Culprit in Bryan's Family")


e1 = evidence1.Evidence()
# Prompt the detective(user) where he wants to look first (Kitchen, under the bed, Basement)
while True:
    functions.choice()
    print("Collect all the evidence in all the following option(Make sure you collect from 1-3 before Proceeding!) ")
    option1 = input("Where do you want to check for evidence? ")
    if option1 == "1":
        kitchen1 = input(
            "What evidence did you see? Blood drop? Burger? Dishes?  ")
        e1.Kitchen(kitchen1)

    elif option1 == "2":
        bed1 = input("What evidence did you see? Books? Missing pillow case? ")
        e1.Bedroom(bed1)

    elif option1 == "3":
        basement1 = input(
            "What evidence did you see? Wedding ring? hair(blonde)")
        e1.Basement(basement1)

    elif option1 == "4":
        print("Let's go to the police station and let's interview the suspects", "\n")
        break
    else:
        print("You are not taking this case seriously huh? ")

# User will be given a "dictionary" of evidence
evidencelist = {}
evidencelist["Kitchen"] = kitchen1
evidencelist["Bedroom"] = bed1
evidencelist["Basement"] = basement1
for proof in evidencelist:
    print("[In the", proof, "you found", evidencelist[proof] + "]")

# Prompt the detective(user) which Suspect he wants to interview first?
while True:
    functions.choice2()
    option2 = input("Who do you want to interview? ")
    if option2 == "1":
        while True:
            print("\n1) Who are you? ")
            print("2) Where were you? ")
            print("3) Proceed to the next suspect\n")
            interview = input("What do you want to ask? ")
            if interview == "1":
                functions.Suspectwho(" the Wife")
            elif interview == "2":
                functions.Suspectwhere(
                    "Outside. I wasn't home because we had an argument. he had a \"MISTRESS\"")
            elif interview == "3":
                break
    elif option2 == "2":
        while True:
            print("\n1) Who are you? ")
            print("2) Where were you? ")
            print("3) Proceed to the next suspect\n")
            interview = input("What do you want to ask? ")
            if interview == "1":
                functions.Suspectwho(" his son")
            elif interview == "2":
                functions.Suspectwhere(
                    "in my bedroom hiding and reading books because I got scared. There was a fight between my dad and my uncle")
            elif interview == "3":
                break
    elif option2 == "3":
        while True:
            print("\n1) Who are you? ")
            print("2) Where were you? ")
            print("3) Proceed to the next suspect\n")
            interview = input("What do you want to ask? ")
            if interview == "1":
                functions.Suspectwho(" his brother")
            elif interview == "2":
                functions.Suspectwhere(
                    "at the store buying beer. This family is done for!")
            elif interview == "3":
                break
    elif option2 == "4":
        print("Proceeding to the next step!")
        break

    else:
        print("You are not taking this case seriously huh?")

while True:
    functions.choice3()
    option3 = input(
        "Who do you think is the murderer detective? (This Question is tricky): \n")
    if option3 == "1":
        print("The Wife is not the murderer! You might think she is because you found her wedding ring on the floor because she was done with the marriage. You are fired!")
        break
    elif option3 == "2":
        print("The Son is not the murderer! That kid is only 6 years old! You are fired!")
        break
    elif option3 == "3":
        print("The Brother is not the murderer! You might think he is because he got into a fight with him. He punched him because he found out that he cheated on his sister(Wife). You are fired!")
        break
    elif option3 == "4":
        option4 = input("Who do you think murdered bryan?: ").lower()
        if option4 == "mistress":
            functions.Murderer()
            break
        else:
            print("Wrong!", option4, "is not the culprit! You are now fired!")
            break
    else:
        print("Choose only 1-4")

print("Thank you for playing! Try again if you got it wrong!")
