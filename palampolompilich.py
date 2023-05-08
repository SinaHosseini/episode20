import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

app = QApplication(sys.argv)
loder = QUiLoader()
main_window = loder.load("ui_mainwindow.ui")
main_window.show()
l_r = ["l","r"]
a = 0

def play(l_r1):
    global a

    c_1 = random.choice(l_r)
    c_2 = random.choice(l_r)
    if l_r1 == "l":
        main_window.you.setText("✋")
    else:
        main_window.you.setText("👋")
    if c_1 == "l":
        main_window.c_1.setText("✋")
    else:
        main_window.c_1.setText("👋")
    if c_2 == "l":
        main_window.c_2.setText("✋")
    else:
        main_window.c_2.setText("👋")
    a += 1

    if main_window.c_1.text() == main_window.c_2.text() and  main_window.c_2.text() == main_window.you.text():
        main_window.text.setText("draw!")
    elif main_window.c_1.text() == main_window.c_2.text():
        main_window.y_s.setText(str(int(main_window.y_s.text())+1))
        main_window.text.setText("you win!")
    elif main_window.c_1.text() == main_window.you.text():
        main_window.c2_s.setText(str(int(main_window.c2_s.text())+1))
        main_window.text.setText("c_2 win!")
    else:
        main_window.c1_s.setText(str(int(main_window.c1_s.text())+1))
        main_window.text.setText("c_1 win!")
    
    if a == 5:
        if int(main_window.c1_s.text()) > int(main_window.c2_s.text()) and int(main_window.c1_s.text()) > int(main_window.y_s.text()):
            main_window.text.setText("c_1 win 👑")
        elif int(main_window.c2_s.text()) > int(main_window.c1_s.text()) and int(main_window.c2_s.text()) > int(main_window.y_s.text()):
            main_window.text.setText("c_2 win 👑")
        elif int(main_window.y_s.text()) > int(main_window.c2_s.text()) and int(main_window.y_s.text()) > int(main_window.c1_s.text()):
            main_window.text.setText("you win 👑")
        else:
            main_window.text.setText("darw 😐")

main_window.l.clicked.connect(partial(play,"l"))
main_window.r.clicked.connect(partial(play,"r"))

app.exec()