
# There are a number of things I'd like to improve:
# Replace fixed values for BLANKS and allow it to vary by quiz
# Incorporate ascii characters as part of output

# The following includes my process for solvng the "Code Your Own Quiz" challenge.
# Step 1: Build out the content of the QUIZZES and ANSWERS

# ------ Define the EASY Quiz -----
quiz_easy = '''
__________________________________________________

You chose the EASY Quiz. You will get 5 guesses per problem. Let's get started. HINT: Remember to CAPITALIZE capitals :)

Americans are notoriously bad at geography. To help us improve our basic understanding of Europe, memorize and name the following European capitals. ___1___ is the capital of the Emerald Isle, Ireland. Kelly Pickler infamously missed this next question on a U.S game show: The capital of France is ___2___ , otherwise known as la Ville des Lumieres. ___3___ is the capital of the Netherlands. ___4___ is the capital of Spain. The following country and capital have the same name. To help you out a bit, this country is known for Grand Prix, casinos and Princess Grace Kelly. ___5___ is the capital of ___5___.

__________________________________________________
'''
# ------ Define the MEDIUM Quiz -----
quiz_medium = '''
__________________________________________________

You chose the MEDIUM Quiz. Time to break a little sweat. You will get 4 guesses per problem. Let's get started.

Name the seven taxonomic ranks for life forms in order: ___1___, ___2___, ___3___, ___4___, ___5___, ___6___, ___7___.

__________________________________________________
'''

# ------ Define the ZOIKS Quiz -----
quiz_zoiks = '''
__________________________________________________

You chose the ZOIKS Quiz. You will get 3 guesses per problem. Let's get started.

Rocks are for more than just throwing at your friends. Rocks classified as ___1___ undergo a physical change due to extreme heat and pressure (hint: think Metamorphin' Power Rocks). Rocks classified as ___2___, form when particles from other rocks or the remains of plants and animals are pressed and cemented together (Hint: kind of like your sedentary uncle). Rocks classified as ___3___ are formed from the cooling of molten rock at or below the surface. A ___4___ is the lucky scientist who gets to study rocks in the hot sun.

__________________________________________________
'''

# Define ANSWERS for each quiz
answers_easy = ["Dublin", "Paris", "Amsterdam", "Madrid", "Monaco"]
answers_medium = ["kingdom", "phylum", "class", "order", "family", "genus", "species"]
answers_zoiks = ["metamorphic", "sedimentary", "igneous", "geologist"]

# Define number of ATTEMPTS by DIFFICULTY of quiz
attempts_easy = 5
attempts_medium = 4
attempts_zoiks = 5

# Define BLANKS for each quiz. This doesn't seem very elegant.
blanks = ["___1___", "___2___","___3___","___4___","___5___","___6___","___7___"]

# STEP 2: To START the game, prompt player to select DIFFICULTY level and return the appropriate QUIZ
def start():
    print " "
    print "||/////////////////////////////////////////////////||"
    print "||                                                 ||"
    print "||               Welcome to the                    ||"
    print "||              * QUIZ of PERIL *                  ||"
    print "||            Enter at your own risk               ||"
    print "||                                                 ||"
    print "||/////////////////////////////////////////////////||"
    user_difficulty = raw_input("\nSelect the difficulty of your quiz: \n \n 1-Easy \n 2-Medium \n 3-Zoiks \n \n ")
    user_difficulty = user_difficulty.lower()
    if user_difficulty == "1" or user_difficulty == "1-easy" or user_difficulty == "easy":
        return quiz_game(quiz_easy, answers_easy, attempts_easy)
    elif user_difficulty == "2" or user_difficulty == "2-medium" or user_difficulty == "medium":
        return quiz_game(quiz_medium, answers_medium, attempts_medium)
    elif user_difficulty == "3" or user_difficulty == "3-zoiks" or user_difficulty == "zoiks":
        return quiz_game(quiz_zoiks, answers_zoiks, attempts_zoiks)
    else:
        print "Sorry that is not an option! \nPlease select a game difficulty by typing in one of the following choices: \n 1-Easy or 2-Medium or 3-Zoiks"

# Start QUIZ
# provide number of remaining attempts
# prompt user to answer questions
# if user input = correct answer, replace BLANKS in QUIZ with user input
# if no more attempts, end game
# if user input != correct answer, increment -1 on attempts

def quiz_game(quiz, answers, attempts):
    print quiz
    index = 0
    while index < len(answers):
        print "\n" + "> You have [ " + str(attempts) + " ] remaining attempts! \n"
        user_input = raw_input("Please provide the correct response for " + str(blanks[index]) + " above" + "\n")
        if user_input == answers[index]:
            quiz = quiz.replace(blanks[index], answers[index])
            index = index + 1
            if index == len(answers):
                print quiz
                return "\n ========================================== \n *** Well Done! You are a Quiz Master! *** \n ========================================== \n"
            else:
                print quiz
                print "\n ------------------------------------------------------ \n Nice job. You answered correctly. Keep going and answer the next question. \n ------------------------------------------------------ \n"
        else:
            if attempts == 1:
                return "\n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n GAME OVER! Sorry, but you have no more attempts. \n Keep studying and better luck next time. \n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   \n"
            else:
                attempts = int(attempts) - 1
                print "\n ------------------------------------------------------ \n Doh! Incorrect Response! But, don't give up hope. You still have " + str(attempts) + " remaining attempts. \n ------------------------------------------------------ \n"


print start()

