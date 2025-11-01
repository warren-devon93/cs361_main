from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_mainWindow

class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        # Additional ui setup for app lists and tables
        catalogHeaders = ["", "Recipe Name", ""]
        recipeHeaders = ["Measurement", "Instruction"]
        self.catalogTable.setHorizontalHeaderLabels(catalogHeaders)
        self.ingredientsTable.setHorizontalHeaderLabels(recipeHeaders)
        self.ingredientsTable.setColumnWidth(0, 150)
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
        # Set up blank rows and line edits for user input
        #self.ingredientsTable.insertRow()
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
    