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
                                                         "Ingredient"])
        self.ingredientsTable.setColumnWidth(0, 150)
        # TODO: Set up text wraps and max string length limits for all table fields
        # Set button signals
        self.addButton.clicked.connect(self.addButtonClicked)
        self.backpageButton.clicked.connect(self.backpageButtonClicked)
        self.ingredientsTable.itemChanged.connect(self.ingredientAdded)
        self.app = app

    # TODO: Renders recipe page
    def renderRecipePage(self):
        # change disabled status of toolbar buttons
        self.backpageButton.setDisabled(False)
        self.addButton.setDisabled(True)
        self.uploadButton.setDisabled(True)
        # Set stacked widget index to recipe page
        self.stackedPages.setCurrentWidget(self.recipePage)

    # Slots
    def addButtonClicked(self):
        # change disabled status of toolbar buttons
        self.backpageButton.setDisabled(False)
        self.addButton.setDisabled(True)
        self.uploadButton.setDisabled(True)
        # Insert first blank row in ingredients and instructions tables
        self.ingredientsTable.insertRow(0)
        self.ingredientsTable.verticalHeader().setVisible(False)
        self.instructionsTable.insertRow(0)
        self.instructionsTable.setVerticalHeaderLabels(["1. "])
        # Set appropriate stacked widgets indices
        self.stackedPages.setCurrentWidget(self.recipePage)
        self.stackedWidget.setCurrentWidget(self.guidePage)
        self.stackedWidget_2.setCurrentWidget(self.guidePage_2)

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
        self.stackedPages.setCurrentWidget(self.catalogPage)
    
    def editButtonClicked(self):
        # Change disabled status of toolbar buttons
        self.backpageButton.setDisabled(False)
        self.editButton.setDisabled(True)
        self.uploadButton.setDisabled(True)
        # TODO: Populate rows of ingredients and instructions tables with recipe data
        # Set stacked widget index to recipe page
        self.stackedPages.setCurrentWidget(self.recipePage)
        # TODO: Render step-by-step guide to adding recipes
    
    def makeListButtonClicked(self):
        # Change disabled status of toolbar buttons
        self.backpageButton.setDisabled(False)
        self.makeListButton.setDisabled(True)
        self.uploadButton.setDisabled(True)
        # TODO: Populate rows of grocery list table with ingredients data
        # TODO: Set stacked widget to grocery list page

    def ingredientAdded(self):
        if (self.ingredientsTable.currentIndex().column()==1
            and self.ingredientsTable.currentIndex().row()==
            self.ingredientsTable.rowCount()-1):
            self.ingredientsTable.insertRow(self.ingredientsTable.rowCount())
    
    def instructionAdded(self):
        if (self.instructionsTable.currentIndex().column()==1
            and self.instructionsTable.currentIndex().row()==
            self.inssTable.rowCount()-1):
            self.ingredientsTable.insertRow(self.ingredientsTable.rowCount())

"""
    def deleteButtonClicked(self):
        #TODO:
    
    def saveButtonClicked(self):
        # TODO:
    
    def uploadButtonClicked(self):
        #TODO:
"""
