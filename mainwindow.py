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
        self.removeRowButton.clicked.connect(self.rowRemoved)
        self.app = app

    def getTable(self):
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            return self.ingredientsTable
        return self.instructionsTable

    def tablesPopulated(self):
        # Checks if both tables have at least one row and no blank items
        tables = [self.ingredientsTable, self.instructionsTable]
        for table in tables:
            if table.blanks is False or table.rowCount()==0:
                return False
        return True

    # Slots
    def addButtonClicked(self):
        # change enabled status of buttons
        self.backpageButton.setDisabled(False)
        self.addButton.setDisabled(True)
        self.uploadButton.setDisabled(True)
        # Insert initial blank rows in ingredients and instructions tables
        self.ingredientsTable.insertRow(0)
        self.instructionsTable.insertRow(0)
        # Add blank first rows to respective table empty item sets
        self.ingredientsTable.blanks.update([(0,0),(0,1)])
        self.instructionsTable.blanks.update([(0,0),(0,1)])
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
        table = self.getTable()
        item = table.currentItem()
        if item is None or not item.text():
            # Add item to set of blanks in table
            table.blanks.add((item.row(), item.column()))
            # Remove row if all items now blank
            rowBlank = True
            for column in range(table.columnCount()):
                item = table.itemAt(table.currentRow(), column)
                if item is not None:
                    rowBlank = False
                    break
            if rowBlank:
                # First remove row items from set of blank items in table
                for column in range(table.columnCount()):
                    table.blanks.discard((table.currentRow(), column))
                # Remove row from table
                table.removeRow(table.currentRow())
            else:
                # Disable save button and add row button if row now partially populated
                self.saveButton.setEnabled(False)
                self.addRowButton.setEnabled(False)
                return
        else:
            # Remove newly populated item from set of blanks if present
            table.blanks.discard((item.row(), item.column()))
        if bool(table.blanks) is False:
            # Enable add row button if table now populated
            self.addRowButton.setEnabled(True)
            if (bool(self.ingredientsTable.blanks) is False and 
                bool(self.instructionsTable.blanks) is False):
                # Enable save button if both tables now populated
                self.saveButton.setEnabled(True)
        
    def rowAppended(self):
        # Append row to end of table
        table = self.getTable()
        table.insertRow(table.rowCount())
        # Add row items to set of blank items in table
        for column in range(table.columnCount()):
            table.blanks.add((table.rowCount()-1, column))
        # Set save button, add row button, and remove row button appropriately
        self.saveButton.setEnabled(False)
        self.addRowButton.setEnabled(False)
        self.removeRowButton.setEnabled(True)
    
    def rowRemoved(self):
        table = self.getTable()
        if table.currentRow()>=0:
            row = table.currentRow()
        else:
            # Last row removed if none currently selected
            row = table.rowCount()-1
        # Removes row items from set of empty table items if present
        for column in range(table.columnCount()):
            table.blanks.discard((row, column))
        # Remove row from table
        table.removeRow(row)
        if table.rowCount()==0:
            # Disable remove row button and enable add row button if not rows remaining
            self.removeRowButton.setEnabled(False)
            self.addRowButton.setEnabled(True)
        elif self.tablesPopulated():
            # Enable save button if both tables populated
            self.saveButton.setEnabled(True)