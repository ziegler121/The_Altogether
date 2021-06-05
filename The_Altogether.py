"""
STANFORD CODE IN PLACE PROJECT SUBMISSION
Project by : Asiedu-brako Jeffrey
Description: This project puts most of the lessons taught in the code in place
course into a larger program with a little bit extra stuff.
'The Altogether' as I call it can perform the following tasks for its user:
1. Can perform some mathematical computations(act as a calculator)
2. Has a word dictionary function
3. Generate random passwords
4. Word Guessing(hangman game)
"""

import pyttsx3  #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

import json
from difflib import get_close_matches  #this function from the difflib helps to get close matches of a word when compared to other words
data = json.load(open("data.json"))

import random
import string

from tkinter import *
import parser   #Parser helps solve the mathematical computations that appear on the calculator

i = 0   #This variable keeps track of the position where the value needs to be inserted

# import random
# from tkinter import *
# import string

def speak(text):
    """
    This function pronounces the string which is passed to it
    """
    engine.say(text)
    engine.runAndWait()


def start_Samaritan():
    speak("...Initializing Samaritan...")
    speak("Hi, I am Samaritan, your voicebot. First and foremost, I would like to say a special thank you to the whole code in place community and Standford University on behalf of my Master Jeffrey")


def welcome_message():
    text = "Welcome to the Altogether. A program that combines some functionalities for the user. The program consists of a calculator, dictionary, hangman game, random password generator"
    print(text)
    speak(text)
    print()

def menu():
    # while True:
    print("---MAIN MENU---\n")
    items = ['Dictionary', 'Hangman', 'Calculator', 'Random Password Generator']
    i=1
    for item in items:
        print(str(i) + "-->" + item)
        i+=1
    speak("Enter 1 to use the dictionary, 2 to play Hangman, 3 for Calculator, 4 for Random Password Generator or 0 to quit the entire program")
    user_choice = int(input())
    if user_choice == 1:
        dictionary()
    elif user_choice == 2:
        hangman_game()
    elif user_choice == 3:
        calculator()
    elif user_choice == 4:
        rand_password_gen()
    else:
        # break
        speak("Goodbye, See you later.")

def find_meaning(word): #function for matching user's input to meanings in dictionary data file
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())[0]) > 1:
        close_match = get_close_matches(word, data.keys())[0]
        speak(f"Did you mean {close_match}?")
        response = input("Enter 'y' for yes or 'n' for no")
        if response == "y" or response=="Y":
            return data[close_match]
        elif response == "n" or response == "N":
            return "You have entered an invalid word."
    else:
        return "You have entered an invalid word."


def dictionary():
    print("")
    print("---***WELCOME TO GEO'S DICTIONARY***---")
    speak("Enter the word you want to search: ")
    word = input()
    do_again = "y"
    while do_again: #find the meaning of words until user enters 'No'
        output = find_meaning(word)
    #check if meaning of word is a list
        if type(output) == list:
            num=1
            for item in output:
                print(str(num)+". "+item)
                num+=1
        else:
            print(output)
        print("")
        speak("Do you want to search for another word? ")
        do_again = input("Enter y for yes or n for no: ")
        print("")
        if do_again == "y" or do_again == "Y":
            speak("Enter the word you want to search: ")
            word = input()
        else:
            break
    print("")
    speak("Thanks for using my dictionary!")
    go_back()

def hangman_game():
    user_name = input("Enter your name: ")
    text = "Welcome"+user_name
    speak(text)
    print("------------------------------")
    speak("Enjoy this Hangman game by trying to guess the word in less than 10 tries")
    print("")
    # play_again = 'y'
    # while play_again:
    hangman()
    speak("Do you want to play again?")
    user_response = input("Enter y for yes or n for no")
    if user_response == 'y' or user_response=='Y':
        # play_again = 'y'
        hangman()
    else:
        # break
        go_back()

def hangman():
    """This function contains a list of words that the user is going to guess
    It matches the user's guesses to the words in the list and displays whether the user
    was able to guess rightly or not
    """
    #list containing words for hangman game
    word_lst = ["chthonic", "squush", "kickshaw", "zugzwang", "ytterbium", "randkluft", "yclept", "diphthong", "squdgy", "besing"]
    valid_input = string.ascii_lowercase
    num_turns = 10
    user_guess = ""
    word = random.choice(word_lst)

    while len(word) > 0:
        word_developed = ""

        for letter in word:
            if letter in user_guess:
                word_developed = word_developed + letter
            else:
                word_developed = word_developed + "_" + " "

        if word_developed == word:
            print(word_developed)
            print("You win!!")
            break

        print("Guess the word: ", word_developed)
        guess = input()


        if guess in valid_input:
            user_guess = user_guess + guess
        else:
            print("Input invalid. Enter a lowercase character")
            guess = input()

        if guess not in word:
            num_turns-=1
            if num_turns == 9:
                print("You have 9 turns left")
                print("  --------  ")
            elif num_turns == 8:
                print("You have 8 turns left")
                print("  --------  ")
                print("     O      ")
            elif num_turns == 7:
                print("You have 7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            elif num_turns == 6:
                print("You have 6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            elif num_turns == 5:
                print("You have 5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            elif num_turns == 4:
                print("You have 4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            elif num_turns == 3:
                print("You have 3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            elif num_turns == 2:
                print("You have 2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            elif num_turns == 1:
                print("You have 1 turn left")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            else:
                speak("You lose")
                speak("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

def calculator():
    root = Tk()
    root.title("Calculator")

    #get the user input and place it in the textfield

    def get_variables(num):
        global i
        display.insert(i, num)
        i+=1

    #function that will get the text from the entire display and evaluate it
    def calculate():
        entire_string = display.get()
        try:
            a = parser.expr(entire_string).compile()
            result = eval(a)
            clear_all()
            display.insert(0, result)
        except Exception:
            clear_all()
            display.insert(0, "Error")

    #function that will handle how the operators work
    def get_operator(operator):
        global i
        length = len(operator)
        display.insert(i, operator)
        i+=length

    #Function that will delete all entries in the textfield
    def clear_all():
        display.delete(0, END)

    #Function that will help delete a single element
    def undo():
        entire_string = display.get()
        if len(entire_string):
            new_string = entire_string[:-1]
            clear_all()
            display.insert(0, new_string)
        else:
            clear_all()
            display.insert(0, "Error")

    #adding the input field- this is where when a number is pressed, it is going to appear
    display = Entry(root)
    display.grid(row=1, columnspan=6, sticky=W+E)

    #adding buttons to the calculator

    Button(root, text="1", command = lambda :get_variables(1)).grid(row=2, column=0)
    Button(root, text="2", command = lambda :get_variables(2)).grid(row=2, column=1)
    Button(root, text="3", command = lambda :get_variables(3)).grid(row=2, column=2)

    Button(root, text="4", command = lambda :get_variables(4)).grid(row=3, column=0)
    Button(root, text="5", command = lambda :get_variables(5)).grid(row=3, column=1)
    Button(root, text="6", command = lambda :get_variables(6)).grid(row=3, column=2)

    Button(root, text="7", command = lambda :get_variables(7)).grid(row=4, column=0)
    Button(root, text="8", command = lambda :get_variables(8)).grid(row=4, column=1)
    Button(root, text="9", command = lambda :get_variables(9)).grid(row=4, column=2)

    #adding other buttons to the calculator
    Button(root, text="AC", command = lambda :clear_all()).grid(row=5, column=0)
    Button(root, text="0", command = lambda :get_variables(0)).grid(row=5, column=1)
    Button(root, text="=", command = lambda :calculate()).grid(row=5, column=2)

    Button(root, text="+", command = lambda :get_operator("+")).grid(row=2, column=3)
    Button(root, text="-", command = lambda :get_operator("-")).grid(row=3, column=3)
    Button(root, text="*", command = lambda :get_operator("*")).grid(row=4, column=3)
    Button(root, text="/", command = lambda :get_operator("/")).grid(row=5, column=3)

    #adding new operations
    Button(root, text="pi", command = lambda :get_operator("*3.14")).grid(row=2, column=4)
    Button(root, text="%", command = lambda :get_operator("%")).grid(row=3, column=4)
    Button(root, text="(", command = lambda :get_operator("(")).grid(row=4, column=4)
    Button(root, text="exp", command = lambda :get_operator("**")).grid(row=5, column=4)

    Button(root, text="DEL", command = lambda :undo()).grid(row=2, column=5)
    Button(root, text="x!").grid(row=3, column=5)
    Button(root, text=")", command = lambda :get_operator(")")).grid(row=4, column=5)
    Button(root, text="^2", command = lambda :get_operator("**2")).grid(row=5, column=5)


    root.mainloop()
    go_back()

def rand_password_gen():
    root = Tk()

    root.geometry("450x250")
    root.title("Secure Password Generator (Produced by GeoTech)")

    #intro text
    intro_text = StringVar()
    label1 = Label(root, textvariable=intro_text).pack()
    intro_text.set("Password Strength:")


    def selection():
        selection = choice.get()

    choice = IntVar()
    radio_but1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
    radio_but2 = Radiobutton(root, text="MEDIUM", variable=choice, value=2, command=selection).pack(anchor=CENTER)
    radio_but3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection).pack(anchor=CENTER)

    Labelchoice = Label(root)
    Labelchoice.pack()

    lenlabel = StringVar()
    lenlabel.set("Password length")
    lentitle = Label(root, textvariable=lenlabel).pack()

    val = IntVar()
    spinlength = Spinbox(root, from_=8, to_=34, textvariable=val, width=20).pack()


    def callback():
        password_label.config(text=password_gen())

    generate_button = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3, padx=3)
    generate_button.pack()

    password = str(callback)

    password_label = Label(root, text="", font=("times", 15, "bold"), fg="blue")
    password_label.pack(side=BOTTOM)

    #Logic for creating various password types
    poor = string.ascii_uppercase + string.ascii_lowercase
    average = string.ascii_uppercase + string.ascii_lowercase + string.digits
    advanced = poor + average + string.punctuation

    def password_gen():
        if choice.get()==1:
            return "".join(random.sample(poor, val.get()))
        elif choice.get()==2:
            return "".join(random.sample(average, val.get()))
        elif choice.get()==3:
            return "".join(random.sample(advanced, val.get()))

    root.mainloop()
    go_back()

def go_back():
    print("")
    menu()



def main():
    start_Samaritan()
    welcome_message()
    menu()


if __name__ == '__main__':
    main()
