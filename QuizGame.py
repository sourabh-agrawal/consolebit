"""
Written by sourabh agrawal
problem:-
    write a quiz game which is dynamic
    user can give how many categories he wants to have for the quiz and how many questions in each category
    after saving the questions of each category test can begin where user will choose the category and then give the answer of questions
"""
# !/usr/bin/python3
quiz = {}  # Here the complete quiz will get save all the categoy and their question-answer
catname = []  # This list is used for storing the name of the categories


# This method is for saving the questions and their answers in each category
def feeding():
    global quiz
    global catname
    categories = int(input("Enter the no of categories you have\t"))
    for i in range(categories):
        cat_name = input("\nEnter the name of the category\t")
        catname.append(cat_name)
        q = int(input("Enter the no of questions\t"))
        ca = {}
        for question in range(q):
            temp = {}
            ques = input("\nEnter question no %d\n" % (question + 1))
            ans = int(input("Enter the answer in 0/1 0=false 1=true\t"))
            temp[ques] = ans
            ca.update(temp)
        quiz[cat_name] = ca


# This method is for playing the game
def gaming():
    correct = 0
    questions = 0
    print("\nchoose one of the following categories to begin with\n")
    counter = 0
    for i in catname:
        print("{}. {}".format(counter, i))
        counter += 1
    n = int(input("\nEnter the number to choose the category\t"))
    for quest in quiz[catname[n]].keys():
        questions += 1
        print("Question {}. {}".format(questions, quest))
        st = int(input("Enter the answer in 0/1 o=false and 1=true\t"))
        if int(quiz[catname[n]][quest]) == st:
            correct += 1
    print("\nyour score = {} out of {}.".format(correct, questions))
    counter = int(input("\n\npress 0 if you want to play again"))
    if not counter:
        gaming()


def main():
    feeding()
    gaming()


if __name__ == '__main__': main()
