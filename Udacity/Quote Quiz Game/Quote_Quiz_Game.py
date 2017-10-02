#!/usr/bin/env python2.7
def main():
    """ Main function makes the program run by initiating the other functions
    """
    mychoice = choice()
    diff_level = difficultyLevel(mychoice)
    startGame(diff_level)


def choice():
    """ Prompts the user for the difficulty level desired
        Returns: the user's dificulty choice
    """
    print("Please select a game difficulty by typing it in! \n" +
          "Possible choices include easy, medium, and hard.")
    valid_responses = ("easy", "medium", "hard", "1", "2", "3")
    user_answer = raw_input().lower()

    while(user_answer not in valid_responses):
        print("That's not an option")
        print("Please select a game difficulty by typing it in! \n" +
              "Possible choices include easy, medium, and hard.")
        user_answer = raw_input().lower()
    return user_answer


def difficultyLevel(mychoice):
    """ Assigns the difficulty level and answers
        Args:
            param1 (str): the user's difficulty choice
        Returns: the user's dificulty choice in word form
    """
    if(mychoice == "easy" or mychoice == '1'):
        return "easy"
    elif(mychoice == "medium" or mychoice == '2'):
        return "medium"
    else:
        return "hard"


def startGame(diff_level):
    """ Quizzes the player
        Args:
            param1 (str):  Assigns the prompt and number of blanks,
                dependent on difficulty level
    """
    prompt_dict = {"easy": "If you love __1__ don't waste __2__ for time is " +
                   "what __3__ is __4__ up of",
                   "medium": "If you __1__ too much time __2__ " +
                   "about a __3__ , you'll __4__ get it done.",
                   "hard": "Anyone who __1__ learning is __2__ , " +
                   "whether at __3__ or __4__ . Anyone who keeps" +
                   " __5__ stays __6__ . The __7__ thing in life " +
                   "is to keep your __8__ young."}
    blanks_dict = {
        "easy": ["__1__", "__2__", "__3__", "__4__"],
        "medium": ["__1__", "__2__", "__3__", "__4__"],
        "hard": ["__1__", "__2__", "__3__", "__4__", "__5__",
            "__6__", "__7__", "__8__"]}

    newString = prompt_dict[diff_level]
    print(newString)
    answer_index = 0
    for blank_item in blanks_dict[diff_level]:
        newString = verifyUsersAnswer(diff_level, newString,
                                      answer_index, blank_item)
        prompt_dict[diff_level] = newString
        answer_index = answer_index + 1
        print(prompt_dict[diff_level])


def verifyUsersAnswer(diff_level, prompt, answer_index, blank_item):
    """ Verifies the users entry against the correct answer
        Args:
            param1 (): the user's selected difficulty level
            param2 (): the prompt associated to the difficulty level
            param3 (): the answers to the associated difficulty level
            param4 (): the blanks associated to the difficulty level
    """
    num_of_tries = 3
    print("You get " + str(num_of_tries) + " guesses per problem")
    answers = {"easy": ["life", "time", "life", "made"],
               "medium": ["spend", "thinking", "thing", "never"],
               "hard": ["stops", "old", "twenty", "eighty",
               "learning", "young", "greatest", "mind"]}

    for num_try in range(num_of_tries):
        print(prompt)
        user_answer = raw_input("What should be in for " + blank_item + " ? ")
        if(user_answer == answers[diff_level][answer_index]):
            print("Congratulations!")
            new_prompt = prompt.replace(blank_item, user_answer)
            return new_prompt
        else:
            num_of_tries = num_of_tries - 1
            print("Nope try again " + str(num_of_tries) + " chances left")
main()
