from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget
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
        self.ingredientsTable.verticalHeader().setVisible(False)
        self.instructionsTable.verticalHeader().setVisible(True)
        # TODO: Testing set parent for stacked widget
        self.stackedWidget.setParent(self.tabWidget)
        self.stackedWidget.move(21, 325)
        # TODO: Set up text wraps and max string length limits for all table fields
        # Set button signals
        self.addButton.clicked.connect(self.addButtonClicked)
        self.backpageButton.clicked.connect(self.backpageButtonClicked)
        self.ingredientsTable.itemChanged.connect(self.recipeChanged)
        self.instructionsTable.itemChanged.connect(self.recipeChanged)
        self.addItemButton.clicked.connect(self.addItemButtonClicked)
        self.removeItemButton.clicked.connect(self.removeItemButtonClicked)
        self.app = app

    # Slots
    def addButtonClicked(self):
        # change disabled status of toolbar buttons
        self.backpageButton.setDisabled(False)
        self.addButton.setDisabled(True)
        self.saveButton.setDisabled(True)
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

    def addItemButtonClicked(self):
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            table = self.ingredientsTable
        else:
            table = self.instructionsTable
        table.insertRow(table.rowCount())

    def removeItemButtonClicked(self):
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            table = self.ingredientsTable
        else:
            table = self.instructionsTable
        table.removeRow(table.currentRow())
        # TODO: Figure out how to call recipeChanged to check if removal makes both tables full

    def recipeChanged(self):
        tables = [self.ingredientsTable, self.instructionsTable]
        for table in tables:
            blankField = False
            for row in range(table.rowCount()):
                for column in range(table.columnCount()):
                    if table.item(row, column) is None:
                        blankField = True
                        break
            if not blankField:

            elif (table.currentRow()==table.rowCount()-1 and
                table.currentColumn()==table.columnCount()-1):
                table.insertRow(table.rowCount())

        """
        if self.tabWidget.currentWidget() is self.ingredientsTab:
            table = self.ingredientsTable
        else:
            table = self.instructionsTable
        for column in range(table.columnCount()):        
        """


"""
        row = table.currentRow()
        blank = True
        for column in range(table.columnCount()):
            if table.item(row, column) is not None and table.item(row, column).text().strip():
                blank = False
                break
        if blank:
            table.removeRow(table.currentRow())
        elif (table.currentRow()==table.rowCount()-1 and
              table.currentColumn()==table.columnCount()-1):
            table.insertRow(table.rowCount())
"""



"""
    def deleteButtonClicked(self):
        #TODO:
    
    def saveButtonClicked(self):
        # TODO:
    
    def uploadButtonClicked(self):
        #TODO:
"""
