from random import shuffle

answer = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def ask(question, right_answer, wrong_1, wrong_2, wrong_3):
    shuffle(answer)
    answer[0].setText(right_answer)
    answer[1].setText(wrong_1)
    answer[2].setText(wrong_2)
    answer[3].setText(wrong_3)
    lb_question.setText(question)
    correct.setText(right_answer)
    show_question()


def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Павильно')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неправильно!')
