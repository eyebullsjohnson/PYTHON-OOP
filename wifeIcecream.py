#ICE CREAM PLS
def ask_for_ice_cream():
    while True:
        response = input("Should I get my wife some ice cream? (SAY YES) ").strip().lower()
        if response == 'yes':
            print("Okay, stopping.")
            break
        else:
            print(" >=[ I'll ask again...")

# Run the function to start asking
ask_for_ice_cream()
#PASTE python3 wifeIcecream.py