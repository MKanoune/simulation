# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\basti_000\PycharmProjects\simulation\config.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import qdarkstyle



class Ui_Dialog(object):

    def __init__(self):
        self.solar_system = {
            "erde": {"name": "Erde", "mass": "123451", "radius": "2345", "distance": "24"},
            "merkur": {"name": "Merkur", "mass": "123451", "radius": "2345", "distance": "24"},
            "venus": {"name": "Venus", "mass": "123451", "radius": "2345", "distance": "24"},
            "mars": {"name": "Mars", "mass": "123451", "radius": "2345", "distance": "24"},
            "neptun": {"name": "Neptun", "mass": "123451", "radius": "2345", "distance": "24"},
            "uranus": {"name": "Uranus", "mass": "123451", "radius": "2345", "distance": "24"},
            "saturn": {"name": "Saturn", "mass": "123451", "radius": "2345", "distance": "24"},
            "jupiter": {"name": "Jupiter", "mass": "123451", "radius": "2345", "distance": "24"}
        }
        self.all_planets = []

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 686)
        Dialog.setWindowIcon(QIcon("planet_icon.png"))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 640, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.planets_comboBox = QtWidgets.QComboBox(Dialog)
        self.planets_comboBox.setGeometry(QtCore.QRect(350, 110, 339, 25))
        self.planets_comboBox.setObjectName("planets_comboBox")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.add_planet_btn = QtWidgets.QPushButton(Dialog)
        self.add_planet_btn.setGeometry(QtCore.QRect(350, 140, 75, 29))
        self.add_planet_btn.setObjectName("add_planet_btn")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 220, 71, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mass_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.mass_label_3.setObjectName("mass_label_3")
        self.verticalLayout_2.addWidget(self.mass_label_3)
        self.rad_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.rad_label_3.setObjectName("rad_label_3")
        self.verticalLayout_2.addWidget(self.rad_label_3)
        self.dist_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.dist_label_3.setObjectName("dist_label_3")
        self.verticalLayout_2.addWidget(self.dist_label_3)
        self.name_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.name_label_3.setObjectName("name_label_3")
        self.verticalLayout_2.addWidget(self.name_label_3)
        self.add_planet_label = QtWidgets.QLabel(Dialog)
        self.add_planet_label.setGeometry(QtCore.QRect(350, 90, 339, 19))
        self.add_planet_label.setObjectName("add_planet_label")
        self.add_usr_planet_btn = QtWidgets.QPushButton(Dialog)
        self.add_usr_planet_btn.setGeometry(QtCore.QRect(350, 350, 75, 28))
        self.add_usr_planet_btn.setObjectName("add_usr_planet_btn")

        self.remove_planet_btn = QtWidgets.QPushButton(Dialog)
        self.remove_planet_btn.setGeometry(QtCore.QRect(475, 350, 75, 28))
        self.remove_planet_btn.setObjectName("remove_usr_planet_btn")

        self.user_planet_label = QtWidgets.QLabel(Dialog)
        self.user_planet_label.setGeometry(QtCore.QRect(350, 200, 211, 16))
        self.user_planet_label.setObjectName("user_planet_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(420, 220, 191, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mass_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.mass_le.setObjectName("mass_le_3")
        self.verticalLayout.addWidget(self.mass_le)
        self.radius_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.radius_le.setObjectName("radius_le_3")
        self.verticalLayout.addWidget(self.radius_le)
        self.dist_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dist_le.setObjectName("dist_le_3")
        self.verticalLayout.addWidget(self.dist_le)
        self.name_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name_le.setObjectName("name_le_3")
        self.verticalLayout.addWidget(self.name_le)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50, 100, 256, 271))
        self.listWidget.setObjectName("listWidget")

        # Method sets every button an Button event
        self.set_btn_events()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.planets_comboBox.setItemText(0, _translate("Dialog", "Merkur"))
        self.planets_comboBox.setItemText(1, _translate("Dialog", "Venus"))
        self.planets_comboBox.setItemText(2, _translate("Dialog", "Erde"))
        self.planets_comboBox.setItemText(3, _translate("Dialog", "Mars"))
        self.planets_comboBox.setItemText(4, _translate("Dialog", "Jupiter"))
        self.planets_comboBox.setItemText(5, _translate("Dialog", "Saturn"))
        self.planets_comboBox.setItemText(6, _translate("Dialog", "Uranus"))
        self.planets_comboBox.setItemText(7, _translate("Dialog", "Neptun"))
        self.add_planet_btn.setText(_translate("Dialog", "hinzufügen"))
        self.mass_label_3.setText(_translate("Dialog", "Masse"))
        self.rad_label_3.setText(_translate("Dialog", "Radius"))
        self.dist_label_3.setToolTip(
            _translate("Dialog", "<html><head/><body><p>Entfernung zum Massemittelpunkt</p></body></html>"))
        self.dist_label_3.setText(_translate("Dialog", "Entfernung"))
        self.name_label_3.setToolTip(_translate("Dialog", "<html><head/><body><p>Name des Planeten</p></body></html>"))
        self.name_label_3.setText(_translate("Dialog", "Name"))
        self.add_planet_label.setText(_translate("Dialog", "Planet hinzügen"))
        self.add_usr_planet_btn.setText(_translate("Dialog", "hinzufügen"))
        self.remove_planet_btn.setText(_translate("Dialog", "entfernen"))
        self.user_planet_label.setText(_translate("Dialog", "benutzerdefinierter Planet:"))

    def set_btn_events(self):
        self.add_planet_btn.clicked.connect(self.add_planet)
        self.add_usr_planet_btn.clicked.connect(self.add_usr_planet)
        self.remove_planet_btn.clicked.connect(self.remove_planet)

    def add_planet(self):
        combo_box_in = str(self.planets_comboBox.currentText())
        planet = self.solar_system[combo_box_in.lower()]
        self.set_output(planet)

    def add_usr_planet(self):
        if self.all_fields_placed():
            planet ={}
            mass = str(self.mass_le.text())
            planet["mass"] = mass
            dist = str(self.dist_le.text())
            planet["distance"] = dist
            radius = str(self.radius_le.text())
            planet["radius"] = radius
            name = str(self.name_le.text())
            if not name:
                name = "None"
            planet["name"] = name
            self.set_output(planet)
            self.set_blank()

    def set_output(self, planet):
        output = "Name: {}\t Masse:{}, Distanz:{}, Radius: {}".format(planet["name"], planet["mass"],
                                                                      planet["distance"], planet["radius"])
        self.all_planets.append(planet)
        print(self.all_planets)
        self.listWidget.addItem(output)

    def all_fields_placed(self):
        all_le = [self.dist_le, self.mass_le, self.radius_le]
        for le in all_le:
            try:
                int(le.text())
            except ValueError:
                return False
        return True

    def remove_planet(self):
        i = self.listWidget.currentRow()
        if i < 0:
            return
        self.listWidget.takeItem(self.listWidget.currentRow())
        del self.all_planets[i]
        print(self.all_planets)

    def set_blank(self):
        self.mass_le.setText("")
        self.dist_le.setText("")
        self.name_le.setText("")
        self.radius_le.setText("")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Simulation Configuration")
    Dialog.show()
    sys.exit(app.exec())



