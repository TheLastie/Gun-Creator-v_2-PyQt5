from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


from Images import Images
from factors import *


class Window(QMainWindow):
    def __init__(self):
        def btn_clc(element):
            if self.ent.text():
                level = self.ent.text()
            else:
                level = "1"
            ndsaa = NameDmgSpeedAccuracyAmmo(element, level)
            o = Images(element, ndsaa.w_type, ndsaa.bonus)
            image = QPixmap(o)
            dmg = ndsaa.dmg()
            elemental_dmg = ndsaa.element_damage()
            speed = ndsaa.speed()
            accuracy = ndsaa.accuracy()
            ammo = ndsaa.ammo()
            name = ndsaa.name()
            if 20 > len(name) > 16:
                self.l_2.setFont(self.font2)
                self.l_2.move(145, 0)
            elif 30 > len(name) > 25:
                self.l_2.setFont(self.font3)
                self.l_2.move(135, 0)
            elif len(name) > 29:
                self.l_2.setFont(self.font3)
                self.l_2.move(125, 0)
            else:
                self.l_2.setFont(self.font1)
                self.l_2.move(160, 0)
            self.l_2.setText(name)
            self.l_3.setText('Урон:' + str(dmg))
            if element != 'none':
                self.l_9.setText('Стихийный урон:' + str(elemental_dmg))
            else:
                self.l_9.setText('')
            self.l_4.setText('патрон/сек:' + str(speed))
            self.l_5.setText('Меткость:' + str(accuracy))
            self.l_6.setText('Ёмкость магазина:' + str(ammo))

            self.l_2.adjustSize()
            self.l_3.adjustSize()
            self.l_4.adjustSize()
            self.l_5.adjustSize()
            self.l_6.adjustSize()
            self.l_8.setPixmap(image)
            self.l_8.adjustSize()
            self.l_9.adjustSize()

        class TS:
            def t1(self):
                btn_clc('none')

            def t2(self):
                btn_clc('fire')

            def t3(self):
                btn_clc('cold')

            def t4(self):
                btn_clc('elctr')

            def t5(self):
                btn_clc('tox')

            def t6(self):
                btn_clc('rad')

        super(Window, self).__init__()
        self.TS = TS
        self.setWindowTitle('Gun Generator')
        self.setGeometry(1420, 30, 500, 300)
        self.font = QFont()
        self.font.setFamily('Eternal Ancient')
        self.font.setPointSize(10)
        self.font1 = QFont()
        self.int = QIntValidator()
        self.font1.setFamily('Eternal Ancient')
        self.font1.setPointSize(10)
        self.font2 = QFont()
        self.font2.setFamily('Eternal Ancient')
        self.font2.setPointSize(9)
        self.font3 = QFont()
        self.font3.setFamily('Eternal Ancient')
        self.font3.setPointSize(8)

        self.l_1 = QLabel(self)
        self.l_2 = QLabel(self)
        self.l_3 = QLabel(self)
        self.l_4 = QLabel(self)
        self.l_5 = QLabel(self)
        self.l_9 = QLabel(self)
        self.l_10 = QLabel(self)
        self.l_6 = QLabel(self)
        self.l_7 = QLabel(self)
        self.l_8 = QLabel(self)

        self.l_1.setText('Стихия')
        self.l_1.move(15, 0)
        self.l_1.setFont(self.font1)
        self.l_2.setFont(self.font)
        self.l_9.move(290, 30)
        self.l_2.move(150, 5)
        self.l_9.setFont(self.font3)
        self.l_3.setFont(self.font)
        self.l_3.move(150, 30)
        self.l_4.setFont(self.font)
        self.l_4.move(150, 55)
        self.l_5.setFont(self.font)
        self.l_5.move(150, 80)
        self.l_6.setFont(self.font)
        self.l_6.move(150, 105)
        self.l_7.setText('level')
        self.l_7.setFont(self.font1)
        self.l_7.move(10, 205)
        self.l_8.move(160, 150)

        self.l_1.setStyleSheet("QLabel { color: white}")
        self.l_2.setStyleSheet("QLabel { color: white}")
        self.l_3.setStyleSheet("QLabel { color: white}")
        self.l_4.setStyleSheet("QLabel { color: white}")
        self.l_5.setStyleSheet("QLabel { color: white}")
        self.l_6.setStyleSheet("QLabel { color: white}")
        self.l_7.setStyleSheet("QLabel { color: white}")
        self.l_8.setStyleSheet("QLabel { color: white}")
        self.l_9.setStyleSheet("QLabel { color: white}")

        self.ent = QLineEdit(self)
        self.ent.move(35, 230)
        self.ent.resize(20, 20)
        self.ent.setValidator(self.int)
        self.ent.setMaxLength(2)

        self.btn_1 = QPushButton(self)
        self.btn_1.setText("Нет")
        self.btn_1.move(10, 30)
        self.btn_1.adjustSize()
        self.btn_1.setStyleSheet("QPushButton { color: #326696}")
        self.btn_1.clicked.connect(self.TS.t1)

        self.btn_2 = QPushButton(self)
        self.btn_2.setText("Огонь")
        self.btn_2.move(10, 60)
        self.btn_2.adjustSize()
        self.btn_2.clicked.connect(self.TS.t2)

        self.btn_3 = QPushButton(self)
        self.btn_3.setText("Холод")
        self.btn_3.move(10, 90)
        self.btn_3.adjustSize()
        self.btn_3.clicked.connect(self.TS.t3)

        self.btn_4 = QPushButton(self)
        self.btn_4.setText("Электричество")
        self.btn_4.move(10, 120)
        self.btn_4.adjustSize()
        self.btn_4.clicked.connect(self.TS.t4)

        self.btn_5 = QPushButton(self)
        self.btn_5.setText("Токсины")
        self.btn_5.move(10, 150)
        self.btn_5.adjustSize()
        self.btn_5.clicked.connect(self.TS.t5)

        self.btn_6 = QPushButton(self)
        self.btn_6.setText("Радиация")
        self.btn_6.move(10, 180)
        self.btn_6.adjustSize()
        self.btn_6.clicked.connect(self.TS.t6)

        gimage = QImage('background.jpg')
        gimage = gimage.scaled(QSize(500, 300))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(gimage))
        self.setPalette(palette)


def app():
    app = QApplication(sys.argv)
    w_1 = Window()

    w_1.show()
    app.exec_()


if __name__ == '__main__':
    app()
