import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from loadpj import Ui_MainWindow1


class MyMainForm(QMainWindow, Ui_MainWindow1):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.anim=None
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.lineEdit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
    # def __init__(self, parent=None):
    #     super().__init__(parent)
    #     self.setupUi(self)
    #     self.start_x = None
    #     self.start_y = None
    #     self.anim=None
    #     self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    #     self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
    #     self.lineEdit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
    #     self.lineEdit_2.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
    #     self.resize(QDesktopWidget().screenGeometry().width(),
    #                 QDesktopWidget().screenGeometry().height())  # 主窗大小
    #     self.e = 1
        # 按ESC键开关
        
    def keyPressEvent(self, QKeyEvent):
        """快捷键"""
        if QKeyEvent.key() == Qt.Key_Escape:  # esc
            if self.e == 1:
                self.animation_exit()
                QTimer.singleShot(1000,app.quit)#退出程序
            elif self.e == 0:
                self.animation_start()

    def animation_start(self):
        self.e = 1
        self.show()
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        self.anim.setStartValue(QRect(QDesktopWidget().screenGeometry().width()  -230, QDesktopWidget().screenGeometry().height()  - 338, 461, 676))
        self.anim.setEndValue(QRect(int(QDesktopWidget().screenGeometry().width()/2  -230), int(QDesktopWidget().screenGeometry().height()/2  -400), int(QDesktopWidget().screenGeometry().width() /2), int(QDesktopWidget().screenGeometry().height()/2)))
        self.anim.setDuration(400)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(0)
        main_opacity.setEndValue(1)
        main_opacity.setDuration(400)
        main_opacity.start()

        # self.anim.setLoopCount(-1)  # 设置循环旋转
        self.anim.start()

    def animation_exit(self):
        self.e = 0
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        self.anim.setEndValue(QRect(0, 0, self.width(), self.height()))
        self.anim.setStartValue(QRect(int(QDesktopWidget().screenGeometry().width()/2  -230), int(QDesktopWidget().screenGeometry().height()/2  -400), 461,676))
        self.anim.setDuration(400)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(1)
        main_opacity.setEndValue(0)
        main_opacity.setDuration(400)
        main_opacity.start()

        # self.anim.setLoopCount(-1)  # 设置循环旋转
        self.anim.start()
        # self.close(10)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(MyMainForm, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except:
            pass

    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(12, 12)  # 偏移
        effect_shadow.setBlurRadius(128)  # 阴影半径
        effect_shadow.setColor(QColor(155, 230, 237, 150))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.animation_start()
    sys.exit(app.exec_())
