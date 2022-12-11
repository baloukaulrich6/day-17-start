from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
"""Pour cree une liste de question """
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# pour que les questions se repete on vas cree une bouque while qui vas controler s'il y a encore une question dans la biblioteque
while quiz.still_has_question():
    quiz.next_question()

print("vous avez terminer le Quizz")
print(f"votre scorer final est: {quiz.score} / {quiz.question_number}")