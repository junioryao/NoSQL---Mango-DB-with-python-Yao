import DataBaseManagement


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CineStore(object):
    def setupUi(self, CineStore):
        CineStore.setObjectName("CineStore")
        CineStore.resize(1261, 776)
        CineStore.setDocumentMode(False)
        CineStore.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(CineStore)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 50, 301, 651))
        self.groupBox.setObjectName("groupBox")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setGeometry(QtCore.QRect(10, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.Movie_name_textedit = QtWidgets.QTextEdit(self.groupBox)
        self.Movie_name_textedit.setGeometry(QtCore.QRect(100, 50, 181, 61))
        self.Movie_name_textedit.setObjectName("Movie_name_textedit")
        self.Movie_genre_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.Movie_genre_textEdit.setGeometry(QtCore.QRect(100, 160, 181, 61))
        self.Movie_genre_textEdit.setObjectName("Movie_genre_textEdit")
        self.name_label_2 = QtWidgets.QLabel(self.groupBox)
        self.name_label_2.setGeometry(QtCore.QRect(10, 180, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_2.setFont(font)
        self.name_label_2.setObjectName("name_label_2")
        self.Movie_descriptopm_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.Movie_descriptopm_textEdit.setGeometry(QtCore.QRect(100, 270, 181, 61))
        self.Movie_descriptopm_textEdit.setObjectName("Movie_descriptopm_textEdit")
        self.name_label_3 = QtWidgets.QLabel(self.groupBox)
        self.name_label_3.setGeometry(QtCore.QRect(10, 290, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_3.setFont(font)
        self.name_label_3.setObjectName("name_label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(170, 480, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.name_label_4 = QtWidgets.QLabel(self.groupBox)
        self.name_label_4.setGeometry(QtCore.QRect(10, 480, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_4.setFont(font)
        self.name_label_4.setObjectName("name_label_4")
        self.name_label_5 = QtWidgets.QLabel(self.groupBox)
        self.name_label_5.setGeometry(QtCore.QRect(10, 390, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_5.setFont(font)
        self.name_label_5.setObjectName("name_label_5")
        self.Movie_language_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.Movie_language_textEdit.setGeometry(QtCore.QRect(100, 370, 181, 61))
        self.Movie_language_textEdit.setObjectName("Movie_language_textEdit")
        self.Addmovie_button = QtWidgets.QPushButton(self.groupBox)
        self.Addmovie_button.setGeometry(QtCore.QRect(110, 590, 75, 23))
        self.Addmovie_button.setObjectName("Addmovie_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 50, 311, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.name_label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.name_label_6.setGeometry(QtCore.QRect(30, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_6.setFont(font)
        self.name_label_6.setObjectName("name_label_6")
        self.Delete_movie_nameTextedit = QtWidgets.QTextEdit(self.groupBox_2)
        self.Delete_movie_nameTextedit.setGeometry(QtCore.QRect(120, 40, 181, 61))
        self.Delete_movie_nameTextedit.setObjectName("Delete_movie_nameTextedit")
        self.name_label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.name_label_7.setGeometry(QtCore.QRect(30, 140, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_7.setFont(font)
        self.name_label_7.setObjectName("name_label_7")
        self.Delete_movie_language_textedit = QtWidgets.QTextEdit(self.groupBox_2)
        self.Delete_movie_language_textedit.setGeometry(QtCore.QRect(120, 130, 181, 61))
        self.Delete_movie_language_textedit.setObjectName("Delete_movie_language_textedit")
        self.deletemovie_button = QtWidgets.QPushButton(self.groupBox_2)
        self.deletemovie_button.setGeometry(QtCore.QRect(100, 220, 101, 23))
        self.deletemovie_button.setObjectName("deletemovie_button")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(440, 320, 311, 381))
        self.groupBox_3.setObjectName("groupBox_3")
        self.name_label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.name_label_8.setGeometry(QtCore.QRect(20, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_8.setFont(font)
        self.name_label_8.setObjectName("name_label_8")
        self.update_movie_name_textedit = QtWidgets.QTextEdit(self.groupBox_3)
        self.update_movie_name_textedit.setGeometry(QtCore.QRect(100, 50, 181, 61))
        self.update_movie_name_textedit.setObjectName("update_movie_name_textedit")
        self.name_label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.name_label_9.setGeometry(QtCore.QRect(20, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_9.setFont(font)
        self.name_label_9.setObjectName("name_label_9")
        self.update_description_textedit = QtWidgets.QTextEdit(self.groupBox_3)
        self.update_description_textedit.setGeometry(QtCore.QRect(100, 150, 181, 61))
        self.update_description_textedit.setObjectName("update_description_textedit")
        self.updatemovie_button = QtWidgets.QPushButton(self.groupBox_3)
        self.updatemovie_button.setGeometry(QtCore.QRect(100, 340, 101, 23))
        self.updatemovie_button.setObjectName("updatemovie_button")
        self.name_label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.name_label_10.setGeometry(QtCore.QRect(20, 260, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_label_10.setFont(font)
        self.name_label_10.setObjectName("name_label_10")
        self.update_dateEdit = QtWidgets.QDateEdit(self.groupBox_3)
        self.update_dateEdit.setGeometry(QtCore.QRect(170, 260, 110, 22))
        self.update_dateEdit.setObjectName("update_dateEdit")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(850, 50, 301, 651))
        self.groupBox_4.setObjectName("groupBox_4")
        self.listallMovies = QtWidgets.QListWidget(self.groupBox_4)
        self.listallMovies.setGeometry(QtCore.QRect(20, 30, 256, 321))
        self.listallMovies.setObjectName("listallMovies")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 360, 101, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listView = QtWidgets.QListWidget(self.groupBox_4)
        self.listView.setGeometry(QtCore.QRect(20, 400, 256, 192))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(180, 612, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(50, 610, 104, 31))
        self.textEdit.setObjectName("textEdit")
        CineStore.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CineStore)
        self.statusbar.setObjectName("statusbar")
        CineStore.setStatusBar(self.statusbar)

        self.retranslateUi(CineStore)
        QtCore.QMetaObject.connectSlotsByName(CineStore)

        self.Addmovie_button.clicked.connect(self.addmovie)
        self.deletemovie_button.clicked.connect(self.deletemovie)
        self.updatemovie_button.clicked.connect(self.updatemovie)
        self.pushButton_4.clicked.connect(self.readallmovie)
        self.pushButton.clicked.connect(self.search)
    def retranslateUi(self, CineStore):
        _translate = QtCore.QCoreApplication.translate
        CineStore.setWindowTitle(_translate("CineStore", "Cine Store"))
        self.groupBox.setTitle(_translate("CineStore", "ADD MOVIE"))
        self.name_label.setText(_translate("CineStore", "Name"))
        self.name_label_2.setText(_translate("CineStore", "Genre"))
        self.name_label_3.setText(_translate("CineStore", "Description"))
        self.name_label_4.setText(_translate("CineStore", "Release Date"))
        self.name_label_5.setText(_translate("CineStore", "Language"))
        self.Addmovie_button.setText(_translate("CineStore", "ADD MOVIE"))
        self.groupBox_2.setTitle(_translate("CineStore", "DELETE MOVIE"))
        self.name_label_6.setText(_translate("CineStore", "Name"))
        self.name_label_7.setText(_translate("CineStore", "Language"))
        self.deletemovie_button.setText(_translate("CineStore", "DELETE  MOVIE"))
        self.groupBox_3.setTitle(_translate("CineStore", "UPDATE MOVIE"))
        self.name_label_8.setText(_translate("CineStore", "Name"))
        self.name_label_9.setText(_translate("CineStore", "Description"))
        self.updatemovie_button.setText(_translate("CineStore", "UPDATE MOVIE"))
        self.name_label_10.setText(_translate("CineStore", "Release Date"))
        self.groupBox_4.setTitle(_translate("CineStore", "LIST ALL MOVIE"))
        self.pushButton_4.setText(_translate("CineStore", "READ MOVIES"))
        self.pushButton.setText(_translate("CineStore", "Search"))

    def addmovie(self):
        DataBaseManagement.push_movie(self.Movie_name_textedit.toPlainText() , self.Movie_genre_textEdit.toPlainText(), self.Movie_descriptopm_textEdit.toPlainText() , self.Movie_language_textEdit.toPlainText() , self.dateEdit.text() )

    def deletemovie(self):
        DataBaseManagement.delete_by_name(self.Delete_movie_nameTextedit.toPlainText() , self.Delete_movie_language_textedit.toPlainText())

    def updatemovie(self):
        DataBaseManagement.update(self.update_movie_name_textedit.toPlainText() , self.update_description_textedit.toPlainText(),self.update_dateEdit.text())


    def readallmovie(self):
        count = 1
        self.listallMovies.clear()
        assembler =  DataBaseManagement.display_all()

        for i in assembler:
            for j,e in i.items():
                if j == '_id':
                    self.listallMovies.insertItem(count , " " )
                    count = count+1
                    continue

                self.listallMovies.insertItem(count , j+" : "+e )
                count = count+1

    def search(self):
        count = 1
        self.listView.clear()
        assembler =  DataBaseManagement.search(self.textEdit.toPlainText())

        for i in assembler:
            for j,e in i.items():
                if j == '_id':
                    self.listView.insertItem(count , " " )
                    count = count+1
                    continue

                self.listView.insertItem(count , j+" : "+e )
                count = count+1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CineStore = QtWidgets.QMainWindow()
    ui = Ui_CineStore()
    ui.setupUi(CineStore)
    CineStore.show()
    sys.exit(app.exec_())
