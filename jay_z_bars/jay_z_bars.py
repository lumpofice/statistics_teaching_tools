import tkinter as tk
from tkinter import *
from tkinter import ttk
import random


a = ttk.Notebook()
frame1 = ttk.Frame(a)
#frame2 = ttk.Frame(a)
#frame3 = ttk.Frame(a)
#frame4 = ttk.Frame(a)
#frame5 = ttk.Frame(a)

def quiz(a):
    """This function chooses an item from the grown_bars list.
If that item comes from the other_bars list, then we call the not_jay_z
function with the chosen grown_bar as its argument. If that item
comes from the jay_z_bars list, then we call the jay_z function
with the chosen grown_bar as its argument."""
    grown_bars = [
        '1 million 2 million 3 million 4 '
        'in 18 months 80 million more',
        'if you grew up with holes in your zapatos '
        'youd celebrate the minute you was havin dough',
        'i lift every voice when i sing '
        'my ability '
        'make yours look like a exercise in futility',
        'who wanna bet us '
        'that we dont touch lettuce '
        'stack cheddars forever '
        'live treacherous '
        'all the et ceteras',
        'true this the streets school us to spend our money foolish',
        'lock my body cant trap my mind '
        'easily explain why we adapt to crime',
        'please dont be fooled by the quantity from these heathens '
        'when your head is full of air you can do a lot of leakin',
        'now everything is sophy '
        'thats philosophical for those who copy',
        'i was shootin dice in the lunchroom, skippin that class '
        'sellin Ziploc just to keep customers glad',
        'This is chess better check your board '
        'who gave the world more fire but less reward',
        'Envy keep your pockets empty so just focus on you '
        'if you broke and clownin a millionaire the joke is on you',
        'Id rather be happy being myself than sad trying to please everyone else',
        'Im the first Latin rapper to baffle your skull/Master the flow',
        '99 percent of aliens prefer earth '
        'so im here to rule the planet starting with your turf',
        'put up that paper and buy me some acres '
        'and start me a farm, you know im a cash cow',
        'hey should i get fresh or should i keep it humble? '
        'my closet like dover street used to be bummin '
        'some days im still bummin difference is now its by choice',
        'His palms are sweaty, knees weak, arms are heavy '
        'Theres vomit on his sweater already, moms spaghetti '
        'Hes nervous, but on the surface he looks calm and ready',
        'Give me the microphone first, so I can bust like a bubble '
        'Compton and Long Beach together Now you know youre in trouble',
        'shackling the masses with drastic rap tactics '
        'graphic displays melt the steel like blacksmiths',
        ]
    
    other_bars = [
        'now everything is sophy '
        'thats philosophical for those who copy',
        'This is chess better check your board '
        'who gave the world more fire but less reward',
        'Envy keep your pockets empty so just focus on you '
        'if you broke and clownin a millionaire the joke is on you',
        'Im the first Latin rapper to baffle your skull/Master the flow',
        'Id rather be happy being myself than sad trying to please everyone else',
        'got throw away bars that can go invade mars',
        'hey should i get fresh or should i keep it humble? '
        'my closet like dover street used to be bummin '
        'some days im still bummin difference is now its by choice',
        'His palms are sweaty, knees weak, arms are heavy '
        'Theres vomit on his sweater already, moms spaghetti '
        'Hes nervous, but on the surface he looks calm and ready',
        'Give me the microphone first, so I can bust like a bubble '
        'Compton and Long Beach together Now you know youre in trouble',
        'this place is my house ',
        'shackling the masses with drastic rap tactics '
        'graphic displays melt the steel like blacksmiths',
        'i might as well erase my face with whiteout '
        'cuz yall cant see me like maces eyebrows',
        'hospital, nah! '
        'growin up only doctor you knew '
        'was dr dre dr jay and maybe that doctor drew dude',
        'I just got a grip on our relationship '
        'We was ironing things out, started picking up steam '
        'And when we didnt need its when it all got heated '
        'And we both said some things that we probably didnt mean',
        'I steadily dream about cleanin these demons out '
        'In order to clean them out, you gotta scream and shout '
        'All of your secrets out loud ',
        'Now lets talk about how much I respect my Pop '
        'Hes been through so much in life, we aint never had a lot',
        'Ay, I got a question for you '
        'When you see another human being whos being treated worse than a disease '
        'On his knees, beggin please, for egg and cheese '
        'Or anything to eat, do you see his test as a lesson for you?',
        'Im PS4 in HD and the screen is plasma '
        'Youre Atari 2600 with a weak adapter'
        'Skeletons aint in my closet, thats my apartment '
        'And they like to hide behind thousand dollar fabrics and garments',
        'I just wanna make the simplest quotes intricate dope '
        'If its about the purest lyricist on the coast '
        'You listening to the GOAT',
        'do any sins go unforgiven? i hope not '
        'cuz most of mine were hunger-driven ',
        'this is bar raisin '
        'im raisin the bar so far '
        'tryin to look at its '
        'equivalent to star gazin',
        'im real '
        'straight from my mothers stomach '
        'aint enough cloth for all us '
        'to be cut from it',
        'What if I told you I wake up screamin and swingin '
        'Dreamin that Im fighting demons '
        'Dreamin Im swingin on heathens '
        'Competin and schemin to eat every piece '
        'of my peace when Im sleepin',
        'youre bluffin youre nothin youre stuffin on thanksgivin '
        'my tummy is hungry ill put you on a plate listen',
        'your style is like dying in my sleep '
        'i dont feel it',
        'please dont be fooled by the quantity from these heathens '
        'when your head is full of air you can do a lot of leakin',
        'im in tune with what the gutter loves '
        'i hop on beats and son you like a mother does',
        'haters wanna be like me but thatll just make em synonyms',
        'i was shootin dice in the lunchroom, skippin that class '
        'sellin Ziploc just to keep customers glad',
        'put up that paper and buy me some acres '
        'and start me a farm, you know im a cash cow',
        'no beef no malice '
        'i got no vendetta with yall '
        'i only want better for myself '
        'might even want better for yall',
        'I just got a grip on our relationship '
        'We was ironing things out, started picking up steam '
        'And when we didnt need its when it all got heated '
        'And we both said some things that we probably didnt mean',
        'the owners of them prisons are magicians thats a trick '
        'voila disappearin in the system thats a trick',
        'I steadily dream about cleanin these demons out '
        'In order to clean them out, you gotta scream and shout '
        'All of your secrets out loud ',
        'this place is my house '
        'i might as well erase my face with whiteout '
        'cuz yall cant see me like maces eyebrows',
        'its only fair to warn i was born with a set of horns '
        'and metaphors attached to my embilical cord',
        '99 percent of aliens prefer earth '
        'so im here to rule the planet starting with your turf',
        'Now lets talk about how much I respect my Pop '
        'Hes been through so much in life, we aint never had a lot',
        'hospital, nah! '
        'growin up only doctor you knew '
        'was dr dre dr jay and maybe that doctor drew dude',
        'no beef no malice '
        'i got no vendetta with yall '
        'i only want better for myself '
        'might even want better for yall',
        'its only fair to warn i was born with a set of horns '
        'and metaphors attached to my embilical cord',
        ]
    
    jay_z_bars = [
        'im supposed to be number one on everybodys list '
        'well see what happens when i no longer exist',
        'im not a biter im a writer for myself and others',
        'now im just scratchin the surface '
        'cause whats burried under there '
        'was a kid torn apart '
        'once his pop disappeared',
        'pound for pah pah pah pound '
        'the best around '
        'no way you can get up '
        'when i get down',
        'unless you was me '
        'how you judge me '
        'i was brought up in pain '
        'yall cant touch me',
        '1 million 2 million 3 million 4 '
        'in 18 months 80 million more',
        'if you grew up with holes in your zapatos '
        'youd celebrate the minute you was havin dough',
        'i lift every voice when i sing '
        'my ability '
        'make yours look like a exercise in futility',
        'who wanna bet us '
        'that we dont touch lettuce '
        'stack cheddars forever '
        'live treacherous '
        'all the et ceteras',
        'true this the streets school us to spend our money foolish',
        'lock my body cant trap my mind '
        'easily explain why we adapt to crime',
        ]
    
    a.add(frame1, text = "Q1")
    
    grown_choice = random.choice(grown_bars) #random choice from grown_bars set
    print(f'There are {len(grown_bars)} bars in grown_bars with P(j)=1/3 being Jay-Z bars')
    
    if grown_choice in other_bars: #other_bars = non_jay_z_bars
        not_jay_z(grown_choice)
        
    if grown_choice in jay_z_bars:
        jay_z(grown_choice)

def not_jay_z(c):
    """This function takes in the chosen grown_bar and displays it, along
with two buttons, one labeled Jay-Z and the other labeled Not Jay-Z, for the user.
The user presses one of these two buttons, as a response to the question
of who wrote the chosen grown_bar. Since this is the not_jay_z function,
users pressing the Not Jay-Z button as a response receive the feedback:
Correct,whereas users pressing the Jay-Z button as a response receive the
feedback: Incorrect. Feedback is generated by the corresponding command function
embedded within the Button arguments."""
    Label(
        frame1,
        text = f"'{c}'",
        wraplength = 1200,
        font = ("Arial", 30, "bold")
        ).grid(row = 2, column = 1)
    Button(
        frame1,
        text = "Not Jay-Z",
        font = ("Arial", 40, "bold"),
        bg = "light yellow",
        command = frame1_correct
        ).grid(row = 3, column = 1)
    Button(
        frame1,
        text = "Jay-Z",
        font = ("Arial", 40, "bold"),
        bg = "light blue",
        command = frame1_incorrect
        ).grid(row = 4, column = 1)

def jay_z(c):
    """This function takes in the chosen grown_bar and displays it, along
with two buttons, one labeled Jay-Z and the other labeled Not Jay-Z, for the user.
The user presses one of these two buttons, as a response to the question
of who wrote the chosen grown_bar. Since this is the jay_z function,
users pressing the Not Jay-Z button as a response receive the feedback:
Incorrect,whereas users pressing the Jay-Z button as a response receive the
feedback: Correct. Feedback is generated by the corresponding command function
embedded within the Button arguments."""
    Label(
        frame1,
        text = f"'{c}'",
        wraplength = 1200,
        font = ("Arial", 30, "bold")
        ).grid(row = 2, column = 1)
    Button(
        frame1,
        text = "Not Jay-Z",
        font = ("Arial", 40, "bold"),
        bg = "light yellow",
        command = frame1_incorrect
        ).grid(row = 3, column = 1)
    Button(
        frame1,
        text = "Jay-Z",
        font = ("Arial", 40, "bold"),
        bg = "light blue",
        command = frame1_correct
        ).grid(row = 4, column = 1)
    
def frame1_correct():
    """This function is called in response to the user pressing the
correct button."""
    Label(
        frame1,
        text = "Correct",
        font = ("Arial", 40, "bold"),
        bg = "green",
        fg = "yellow"
        ).grid(row = 1, column = 1)
    
def frame1_incorrect():
    """This function is called in response to the user pressing the
incorrect button."""
    Label(
        frame1,
        text = "Incorrect",
        font = ("Arial", 40, "bold"),
        bg = "red",
        fg = "yellow"
        ).grid(row = 1, column = 1)
    
quiz(a)
a.pack()
a.mainloop()