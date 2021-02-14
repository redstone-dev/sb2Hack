print("""
sb2Hack v1.00
© 2021 redstone-scratch

sb2Hack is a Python program that allows you to hack .sb2 files.
For more information, see the official GitHub repo:
""")

if(input("Are you ready to hack? ").lower() in ["yes","y","yeah"]):
    print("Great!")
elif input("Really? ").lower() in ["no","n","nope"]:
    print("Okay.")
else:
    print("I'm pretty sure you typed gibberish.")
