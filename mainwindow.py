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
        # Initialize instruction and ingredients table layouts
        self.ingredientsTable.setColumnWidth(0, 150)
        self.ingredientsTable.verticalHeader().setVisible(False)
        self.instructionsTable.verticalHeader().setVisible(True)
        # Initialize sets containing empty table item tuples
        self.instructionsTable.blanks = set()
        self.ingredientsTable.blanks = set()
        # Set stacked widget parent and layout location
        self.stackedWidget.setParent(self.tabWidget)
        self.stackedWidget.move(21, 325)
        # Signals
        self.addButton.clicked.connect(self.addButtonClicked)
        self.backpageButton.clicked.connect(self.backpageButtonClicked)
        self.ingredientsTable.itemChanged.connect(self.recipeChanged)
        self.instructionsTable.itemChanged.connect(self.recipeChanged)
        self.addRowButton.clicked.connect(self.rowAppended)
        self.app = app

    def getTable(self):
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            return self.ingredientsTable
        return self.instructionsTable

    def tablesPopulated(self):
        tables = [self.ingredientsTable, self.instructionsTable]
        for table in tables:
            for row in range(table.rowCount()):
                for column in range(table.columnCount()):
                    item = table.item(row, column)
                    if item is None or not item.text():
                        return False
        return True

    # Slots
    def addButtonClicked(self):
        # change disabled status of toolbar buttons
        self.backpageButton.setDisabled(False)
        self.addButton.setDisabled(True)
        self.uploadButton.setDisabled(True)
        # Insert initial blank rows in ingredients and instructions tables
        self.ingredientsTable.insertRow(0)
        self.instructionsTable.insertRow(0)
        # Set appropriate stacked widgets indices
        self.stackedPages.setCurrentWidget(self.recipePage)
        self.stackedWidget.setCurrentWidget(self.guidePage)

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

    def recipeChanged(self):
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            table = self.ingredientsTable
        else:
            table = self.instructionsTable
        row = table.currentRow()
        blanks = 0
        # Searches current row for blank cells
        for column in range(table.columnCount()):
            item = table.item(row, column)
            if item is None or not item.text():
                blanks+=1
        match blanks:
            case 0:
                # Enable save button if both tables entirely populated
                if self.saveButton.isEnabled() is False and self.tablesPopulated():
                    self.saveButton.setEnabled(True)
                # Adds new row if current row last in table
                if table.currentRow()==table.rowCount()-1:
                    table.insertRow(table.currentRow()+1)
                return
            case 1:
                # Disables save button if current row only partially populated
                self.saveButton.setDisabled(True)
                return
            case _:
                # Removes blank row from table
                table.removeRow(table.currentRow())
                # Enable save button if both tables entirely populated
                if self.saveButton.isEnabled() is False and self.tablesPopulated():
                    self.saveButton.setEnabled(True)
                return

    def rowAppended(self):
        # Disable save button when new row appended to table
        self.saveButton.setEnabled(False)
        # Add row items to set of blank items in table
        table = self.getTable()
        for column in range(table.columnCount()):
            table.blanks.add((table.rowCount()-1, column))