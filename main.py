from question_model import Question
from data import question_data
from quiz_brain import QuizBrain  # Fixed typo in class name
from art import logo
print(logo)
question_bank = []
for question in question_data:
    quest_text = question["text"]
    quest_answer = question["answer"]
    new_question = Question(quest_text, quest_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)  # Fixed typo and added missing parenthesis
while quiz.still_has_questions():
    quiz.next_question()