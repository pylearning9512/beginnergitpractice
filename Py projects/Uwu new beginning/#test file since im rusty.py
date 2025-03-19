def reverse():
    """"
    this is a function that mirrors the strings when the user calls
    it by entering "mirror". otherwise it will print the regular strings combined

    """
    
    mirror = combined_lists[::-1]
    user_input= hewwo_input
    if user_input == ("mirror"):
        print(mirror)
    else:
        print(combined_lists)

""""
this defines the user inputs for the function to work with, 
it specifies if it should mirror it or not, and then asks for the text to be displayed

"""

hewwo_input= input("whacha want?  ")

a= input("enter first word: ")
b= input("enter second word: ")
combined_lists= str(a+" "+b)


#calling the function once all inputs have been define
reverse()