from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from ui_mainwindow import Ui_mainWindow

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        # Additional ui setup for app lists and tables
        self.catalogTable.setHorizontalHeaderLabels(["", "Recipe Name", ""])
        self.ingredientsTable.setHorizontalHeaderLabels(["Measurement", 
                                                         "Instruction"])
        self.ingredientsTable.setColumnWidth(0, 150)
        # TODO: Set up text wraps and max string length limits for all table fields
        # Setting up button signals
        self.addButton.clicked.connect(self.addButtonClicked)
        self.backpageButton.clicked.connect(self.backpageButtonClicked)
        self.app = app
    # Slots
    def addButtonClicked(self):
        # Set disabled status of toolbar buttons
        self.backpageButton.setDisabled(False)
        self.addButton.setDisabled(True)
        self.editButton.setDisabled(True)
        self.makeListButton.setDisabled(True)
        self.deleteButton.setDisabled(True)
        self.saveButton.setDisabled(True)
        self.uploadButton.setDisabled(True)
        # Insert first blank row in ingredients and instructions tables
        self.ingredientsTable.insertRow(0)
        self.ingredientsTable.setVerticalHeaderLabels([""])
        self.instructionsTable.insertRow(0)
        self.instructionsTable.setVerticalHeaderLabels(["1. "])
        # Set stacked widget index to recipePage
        self.stackedWidget.setCurrentWidget(self.recipePage)
    def backpageButtonClicked(self):
        # Set disabled status of toolbar buttons
        self.backpageButton.setDisabled(True)
        self.addButton.setDisabled(False)
        self.editButton.setDisabled(True)
        self.makeListButton.setDisabled(True)
        self.deleteButton.setDisabled(True)
        self.saveButton.setDisabled(True)
        self.uploadButton.setDisabled(False)
        # Set stacked widget index to recipePage
        self.stackedWidget.setCurrentWidget(self.catalogPage)
    