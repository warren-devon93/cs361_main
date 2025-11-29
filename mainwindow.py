from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_mainWindow
from tablewidget import TableWidget
    
class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        # Set of all empty items in ingredients and instructions table
        
        # Additional ui setup for app lists and tables
        self.catalogTable.setHorizontalHeaderLabels(["", "Recipe Name", ""])
        self.ingredientsTable.setHorizontalHeaderLabels(["Measurement", 
                                                         "Ingredient"])
        # Signals
        self.addButton.clicked.connect(self.addButtonClicked)
        self.backpageButton.clicked.connect(self.backpageButtonClicked)
        self.addRowButton.clicked.connect(self.addRowButtonClicked)
        self.removeRowButton.clicked.connect(self.removeRowButtonClicked)
        self.ingredientsTable.itemChanged.connect(self.recipeChanged)
        self.instructionsTable.itemChanged.connect(self.recipeChanged)
        self.addItemButton.clicked.connect(self.addItemButtonClicked)
        self.removeItemButton.clicked.connect(self.removeItemButtonClicked)
        self.app = app

    def tablesPopulated(self):
        tables = [self.ingredientsTable, self.instructionsTable]
        for table in tables:
            for row in range(table.rowCount()):
                for column in range(table.columnCount()):
                    item = table.item(row, column)
                    if item is None or not item.text():
                        return False
        return True

    def getTable(self):
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            return self.ingredientsTable
        else:
            return self.instructionsTable        

    # Slots
    def addRowButtonClicked(self):
        # Retrieve current table
        table = self.getTable()
        # Append row to end of table
        table.insertRow(table.rowCount())
        # Disable add row button
        self.addRowButton.setEnabled(False)
        self.removeRowButton.setEnabled(True)
    
    def removeRowButtonClicked(self):
        # Retrieve current table
        table = self.getTable()
        if table.currentRow()>=0:
            # Remove selected row from table
            table.removeRow(table.currentRow())
        else:
            # Remove last row from table if no row selected
            table.removeRow(table.rowCount()-1)

    def addButtonClicked(self):
        # change enabled status of buttons
        self.backpageButton.setEnabled(True)
        self.addButton.setEnabled(False)
        self.uploadButton.setEnabled(False)
        self.addRowButton.setEnabled(False)
        self.removeRowButton.setEnabled(False)
        # Insert initial blank rows in ingredients and instructions tables
        self.ingredientsTable.insertRow(0)
        self.instructionsTable.insertRow(0)
        # Set appropriate stacked widgets indices
        self.stackedPages.setCurrentWidget(self.recipePage)
        self.stackedWidget.setCurrentWidget(self.guidePage)

    def backpageButtonClicked(self):
        # Set disabled status of toolbar buttons
        self.backpageButton.setEnabled(False)
        self.addButton.setEnabled(True)
        self.editButton.setEnabled(False)
        self.makeListButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.uploadButton.setEnabled(True)
        # Set stacked widget index to recipePage
        self.stackedPages.setCurrentWidget(self.catalogPage)
    
    def editButtonClicked(self):
        # Change disabled status of toolbar buttons
        self.backpageButton.setEnabled(True)
        self.editButton.setEnabled(False)
        self.uploadButton.setEnabled(False)
        # TODO: Populate rows of ingredients and instructions tables with recipe data
        # Set stacked widget index to recipe page
        self.stackedPages.setCurrentWidget(self.recipePage)
        # TODO: Render step-by-step guide to adding recipes
    
    def makeListButtonClicked(self):
        # Change disabled status of toolbar buttons
        self.backpageButton.setEnabled(True)
        self.makeListButton.setEnabled(False)
        self.uploadButton.setEnabled(False)
        # TODO: Populate rows of grocery list table with ingredients data
        # TODO: Set stacked widget to grocery list page

    # Enables addRowButton, removeRowButton, and saveButton based on status of each table
    def recipeChanged(self):
        table = self.getTable()
        row = table.currentRow()
        blanks = 0
        # Searches current row for blank cells
        for column in range(table.columnCount()):
            item = table.item(row, column)
            if item is None or not item.text():
                blanks+=1
        match blanks:
            case 0:
                # Enable addRowButton if table populated
                # TODO: Control structure
                self.addRowButton.setEnabled(True)
                # Enable save button if both tables entirely populated
                if self.saveButton.isEnabled() is False and self.tablesPopulated():
                    self.saveButton.setEnabled(True)
                return
            case 1:
                # Disables save button if current row only partially populated
                self.saveButton.setEnabled(False)
                self.addRowButton.setEnabled(False)
                return
            case _:
                # Removes blank row from table
                table.removeRow(table.currentRow())
                # Enable save button if both tables entirely populated
                if self.saveButton.isEnabled() is False and self.tablesPopulated():
                    self.saveButton.setEnabled(True)
                return