from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget

class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self._isPopulated = False

    def setPopulated(self, bool):
        self._isPopulated = bool

    """
    def tablePopulated(self):
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                item = self.item(row, column)
                if item is None or not item.text():
                    return False
        return True    
    """