from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        # Set of all empty items in table
        self._emptyItems = {}
        # Signals
        self.rowInserted.connect(self.rowAppended)
        self.rowsAboutToBeRemoved.connect(self.rowRemoved)

    def isPopulated(self):
        if self._emptyItems:
            return True
        return False

    # Slots
    def rowAppended(self):
        # Add new row items to set of empty items
        for column in range(self.columnCount()):
            self._emptyItems.add((self.rowCount()-1, column))

    def rowRemoved(self):
        # Check if row to be removed contains empty items
        row = self.currentRow()
        for column in range(self.columnCount()):
            # Remove empty item in row from set of empty items
            self._emptyItems.discard((row, column))