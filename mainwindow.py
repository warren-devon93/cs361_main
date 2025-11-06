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
        #self.saveButton.clicked.connect()
        #self.backpageButton.clicked.connect(self.backpageButtonClicked)
        self.ingredientsTable.itemChanged.connect(self.recipeChanged)
        self.instructionsTable.itemChanged.connect(self.recipeChanged)
        self.addRowButton.clicked.connect(self.rowAppended)
        self.removeRowButton.clicked.connect(self.rowRemoved)
        self.tabWidget.currentChanged.connect(self.resetTableButtons)
        self.app = app

    def getTable(self):
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            return self.ingredientsTable
        return self.instructionsTable

    def tablePopulated(self, QTableWidget):
        # Return false if table contains no rows or missing items
        if bool(QTableWidget.blanks) or QTableWidget.rowCount()==0:
            return False
        return True

    # Slots
    def addButtonClicked(self):
        # Set enabled status of buttons
        self.backpageButton.setEnabled(True)
        self.addButton.setEnabled(False)
        self.editButton.setEnabled(False)
        self.makeListButton.setEnabled(False)
        self.deleteButton.setEnabled(True)
        self.saveButton.setEnabled(False)
        self.uploadButton.setEnabled(False)
        # Insert initial blank rows in ingredients and instructions tables
        self.ingredientsTable.insertRow(0)
        self.instructionsTable.insertRow(0)
        # Permit editing of header text field
        # Add blank first rows to respective table empty item sets
        self.ingredientsTable.blanks.update([(0,0),(0,1)])
        self.instructionsTable.blanks.update([(0,0)])
        # Set appropriate stacked widgets indices
        self.stackedPages.setCurrentWidget(self.recipePage)
        self.stackedWidget.setCurrentWidget(self.guidePage)
    
    def saveButtonClicked(self):
        # Set enabled status of buttons
        self.backpageButton.setEnabled(False)
        self.addButton.setEnabled(True)
        self.editButton.setEnabled(False)
        self.makeListButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.saveButton.setEnabled(False) 
        self.uploadButton.setEnabled(True)
        # Insert new recipe into catalog table
        

    def recipeChanged(self):
        table = self.getTable()
        item = table.currentItem()
        if item is None or not item.text():
            # Add item to set of blanks in table
            table.blanks.add((item.row(), item.column()))
            # Remove row if all its items are blank
            rowBlank = True
            for column in range(table.columnCount()):
                item = table.item(item.row(), column)
                if item and item.text():
                    rowBlank = False
                    break
            if rowBlank:
                # Remove row items from set of blank items in table
                for column in range(table.columnCount()):
                    table.blanks.discard((item.row(), column))
                table.removeRow(item.row())
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
            if (self.tablePopulated(self.ingredientsTable) and 
                self.tablePopulated(self.instructionsTable)):
                # Enable save button if both tables populated
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
            # Disable remove row button and enable add row button if no rows remaining
            self.removeRowButton.setEnabled(False)
            self.addRowButton.setEnabled(True)
        elif (self.tablePopulated(self.ingredientsTable) and 
              self.tablePopulated(self.instructionsTable)):
            # Enable save button if both tables populated
            self.saveButton.setEnabled(True)

    def resetTableButtons(self):
        # Enable add row button and remove row button if ingredients table populated
        table = self.getTable()
        if table.rowCount()==0:
            # Set if table has no rows
            self.addRowButton.setEnabled(True)
            self.removeRowButton.setEnabled(False)
        elif self.tablePopulated(table):
            # Set if table fully populated
            self.addRowButton.setEnabled(True)
            self.removeRowButton.setEnabled(True)
        else:
            # Set if table has at least one blank item
            self.addRowButton.setEnabled(False)
            self.removeRowButton.setEnabled(True)
        