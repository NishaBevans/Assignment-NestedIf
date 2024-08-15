#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" 
print ("large hall") if attendees > 100 else print("conference room")

#Task 2: Venue Selection: Based on the code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

audio_system = input("Would you like an audio system? yes/no: ")
projector = input("Would you like a projector? yes/no: ")
if attendees > 100:   
    if audio_system == "yes" and projector == "no":
        print("We will have the audio system ready for you!")
    if audio_system == "yes" and projector == "yes":
        print("We will have both set up for your event.")
elif attendees < 100:
    if projector == "yes" and audio_system == "no":
        print("We will have the projector set up for you.")
    if projector == "yes" and audio_system == "yes":
        print("We will have both set up for your event.")




#Task 3: Catering Choices: Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

vegetarian = input("Would you like vegetarian food? yes/no: ")

if vegetarian == "yes":
    print("We recommend Veggie Delight Caterers!")
else:
    print("We recomment Gourmet Meals Caterers!")


