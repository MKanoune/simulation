# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\basti_000\PycharmProjects\simulation\config.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets

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
        Dialog.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 640, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(40, 370, 295, 144))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_6)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_5.addWidget(self.checkBox)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mass_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.mass_label_2.setObjectName("mass_label_2")
        self.verticalLayout_4.addWidget(self.mass_label_2)
        self.radius_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.radius_label_2.setObjectName("radius_label_2")
        self.verticalLayout_4.addWidget(self.radius_label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.add_usr_sun_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.add_usr_sun_btn.setObjectName("add_usr_sun_btn")
        self.verticalLayout_6.addWidget(self.add_usr_sun_btn)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 60, 601, 251))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.add_planet_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.add_planet_label.setObjectName("add_planet_label")
        self.verticalLayout_8.addWidget(self.add_planet_label)
        self.planets_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.planets_comboBox.setObjectName("planets_comboBox")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.planets_comboBox.addItem("")
        self.verticalLayout_8.addWidget(self.planets_comboBox)
        self.add_planet_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.add_planet_btn.setObjectName("add_planet_btn")
        self.verticalLayout_8.addWidget(self.add_planet_btn)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mass_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.mass_label.setObjectName("mass_label")
        self.verticalLayout_2.addWidget(self.mass_label)
        self.rad_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.rad_label.setObjectName("rad_label")
        self.verticalLayout_2.addWidget(self.rad_label)
        self.dist_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.dist_label.setObjectName("dist_label")
        self.verticalLayout_2.addWidget(self.dist_label)
        self.name_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_2.addWidget(self.name_label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mass_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.mass_le.setObjectName("mass_le")
        self.verticalLayout.addWidget(self.mass_le)
        self.radius_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.radius_le.setObjectName("radius_le")
        self.verticalLayout.addWidget(self.radius_le)
        self.dist_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.dist_le.setObjectName("dist_le")
        self.verticalLayout.addWidget(self.dist_le)
        self.name_le = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.name_le.setObjectName("name_le")
        self.verticalLayout.addWidget(self.name_le)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.user_planet_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.user_planet_label.setObjectName("user_planet_label")
        self.verticalLayout_7.addWidget(self.user_planet_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_usr_planet_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.add_usr_planet_btn.setObjectName("add_usr_planet_btn")
        self.horizontalLayout_5.addWidget(self.add_usr_planet_btn)
        self.remove_planet_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.remove_planet_btn.setObjectName("remove_planet_btn")
        self.horizontalLayout_5.addWidget(self.remove_planet_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.buttonBox.raise_()
        self.label.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.listWidget.raise_()

        self.set_btn_events()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simulation Configuration"))
        self.label.setText(_translate("Dialog", "Masseschwerpunkt"))
        self.checkBox.setText(_translate("Dialog", "Sonne (Masse: 1,989 × 10^30 kg, Radius: 695.700 km)"))
        self.label_2.setText(_translate("Dialog", "Benutzerdefiniert:"))
        self.mass_label_2.setText(_translate("Dialog", "Masse"))
        self.radius_label_2.setText(_translate("Dialog", "Radius"))
        self.add_usr_sun_btn.setText(_translate("Dialog", "hinzufügen"))
        self.add_planet_label.setText(_translate("Dialog", "Planet hinzügen"))
        self.planets_comboBox.setItemText(0, _translate("Dialog", "Merkur"))
        self.planets_comboBox.setItemText(1, _translate("Dialog", "Venus"))
        self.planets_comboBox.setItemText(2, _translate("Dialog", "Erde"))
        self.planets_comboBox.setItemText(3, _translate("Dialog", "Mars"))
        self.planets_comboBox.setItemText(4, _translate("Dialog", "Jupiter"))
        self.planets_comboBox.setItemText(5, _translate("Dialog", "Saturn"))
        self.planets_comboBox.setItemText(6, _translate("Dialog", "Uranus"))
        self.planets_comboBox.setItemText(7, _translate("Dialog", "Neptun"))
        self.add_planet_btn.setText(_translate("Dialog", "hinzufügen"))
        self.mass_label.setText(_translate("Dialog", "Masse"))
        self.rad_label.setText(_translate("Dialog", "Radius"))
        self.dist_label.setToolTip(_translate("Dialog", "<html><head/><body><p>Entfernung zum Massemittelpunkt</p></body></html>"))
        self.dist_label.setText(_translate("Dialog", "Entfernung"))
        self.name_label.setToolTip(_translate("Dialog", "<html><head/><body><p>Name des Planeten</p></body></html>"))
        self.name_label.setText(_translate("Dialog", "Name"))
        self.user_planet_label.setText(_translate("Dialog", "benutzerdefinierter Planet:"))
        self.add_usr_planet_btn.setText(_translate("Dialog", "hinzufügen"))
        self.remove_planet_btn.setText(_translate("Dialog", "entfernen"))

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



