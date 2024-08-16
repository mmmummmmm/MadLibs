import random


# List of story templates with placeholders. 
# New templates can be added to this list to increase variety.
template_reportoire = ["It was about (a number) (a measure of time) ago when I arrived at the hospital in a (a mode of Transportation)." 
                          "The hospital was a/an (an adjective) place, there were a lot of (an adjective) (a plural noun) there. There were nurses who had (a color) (a part of the body)."
                             "If someone wanted to come into my room I told them that they had to (a verb) first. I’ve decorated my room with (a number) (a noun)."
                               " Today I talked to a doctor and they were wearing a (a noun) on their (a part of body). I heard that all doctors (a verb) (a noun) every day for breakfast."
                                   " The most (an adjective) thing about being in the hospital is the (a silly word) (a noun)!",
                       "This weekend I am going camping with (a person’s name). I packed my lantern, sleeping bag, and (a noun). I am so (an adjective describing a feeling)"
                        " to (a verb without 'to') in a tent. I am (an adjective describing a feeling) we might see a/an (an animal), I hear they’re kind of dangerous. While we’re camping"
                            ", we are going to hike, fish, and (a verb without 'to'). I have heard that the (a color) lake is great for ( a verb enging in -ing). Then we will (an adverb ending in -ly)"
                                 " hike through the forest for (a number) (a measure of time). If I see a/an (a color) (an animal) while hiking, I am going to bring it home as a pet! At night we will tell"
                                     " (a number) (a silly word) stories and roast (a noun) around the campfire!",
                       "Dear (a person’s name ), I am writing to you from a/an (an adjective) castle in an enchanted forest. I found myself here one day after"
                         " going for a ride on a (a color) (an animal) in (a place). There are (an adjective) (a magical Creature in plural form) and (an adjective)"
                             " (a magical creature in Plural from) here! In the (a room in a house) there is a pool full of (a noun). I fall asleep each night on a (a noun) of (a plural noun)"
                                 " and dream of (an adjective) (a plural noun). It feels as though I have lived here for (a number) (a measure of time). I hope one day you can visit, although"
                                     " the only way to get here now is (a verb ending in -ing) on a (an Adjective) (a noun)!"  "Once upon a time there was a man called (a name)"]

"Display message to players."
input ('''
       Welcome adventurer! You are about to help us make a history here. 
       Here's how it works:
       You give us a little bit of detail and Shahrzad the story teller will tell you a story based on your input. Be careful what words you choose!
       To continue press ENTER . . . ''')

#While loop to make sure the user picks a number 
while True:
    try:
        selected_template = input ('''
       Please choose a template to proceed:
       1- A hospital visit
       2- A camping trip
       3- A letter to a friend
       0- Let the game choose one for you. ^ - ^
                           
        Your choice: ''')
        if selected_template == '0':
            selected_template = random.choice(template_reportoire)
        else:
            selected_template = template_reportoire[int(selected_template)-1]
    except Exception as e:
        print ("You must enter a valid number between 0 and 3. Try again!")
        continue
    break



#Challenge: How to extract the words in the parantheses so that the program can automatically collect all the keywords and ask for users' input.
# Replacing ')' with '(' simplifies the process of extracting placeholders from the template.
template_splits = selected_template.replace(')','(').split('(')  

#Split into two alternating lists. Again, helps with automating the code.
template_words, key_words = template_splits[0::2], template_splits[1::2]


#User's inputs
answers =[]

#Collect keywords from the user. 
# Use the try/except concept to validate numbers. Smart, huh? Thank you Stackoverflow. 
# A *for loop* might make more sense as it can put a limit for the number of retries.
for keyword in (key_words):
   # user_input = input (f'Please enter a/an {i} ')
    if keyword == 'a number':
        while True: 
            try:    
                user_input = input (f'Please enter {keyword}: ')
                user_input_int = int(user_input)
            except ValueError:
                print (f'Dude! Really? {user_input}?  TRY AGAIN!')
                continue
            break
    else:
        user_input = input (f'Please enter {keyword}: ')
    answers.append(user_input)

#recreate the story
story = [None]*(len(template_words)+(len(answers)))
story[::2] = template_words
story[1::2] = answers
story = ''.join(story)
print (story)
