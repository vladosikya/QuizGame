from question_model import Question
from data import question_data
from quiz_brain import Brain

game = Brain()
questions = []
MAIN_GAME = True

for ques in question_data:
    questions.append(Question(ques['text'], ques['answer']))

while MAIN_GAME:
    sc = 1
    print('If you want to stop, just write "stop".')
    for ques in questions:
        if game.take_answer(question_date=ques, num=sc):
            sc+=1
        else:
            break

    if len(questions) < sc:
        print("Questions are over.")

    if game.play_again():
        pass
    else:
        MAIN_GAME = False


