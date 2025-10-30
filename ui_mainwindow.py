# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHeaderView,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSplitter, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(915, 721)
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.hSplitter = QSplitter(self.centralWidget)
        self.hSplitter.setObjectName(u"hSplitter")
        self.hSplitter.setGeometry(QRect(0, 0, 1081, 721))
        self.hSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.toolbarFrame = QFrame(self.hSplitter)
        self.toolbarFrame.setObjectName(u"toolbarFrame")
        self.toolbarFrame.setMinimumSize(QSize(120, 0))
        self.toolbarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.toolbarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.toolbarFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 93, 675))
        self.toolbarVLayout = QVBoxLayout(self.layoutWidget)
        self.toolbarVLayout.setObjectName(u"toolbarVLayout")
        self.toolbarVLayout.setContentsMargins(0, 0, 0, 0)
        self.backpageButton = QPushButton(self.layoutWidget)
        self.backpageButton.setObjectName(u"backpageButton")
        self.backpageButton.setEnabled(False)
        self.backpageButton.setMinimumSize(QSize(91, 91))
        icon = QIcon()
        icon.addFile(u":/icons/backpage.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backpageButton.setIcon(icon)
        self.backpageButton.setIconSize(QSize(50, 50))

        self.toolbarVLayout.addWidget(self.backpageButton)

        self.addButton = QPushButton(self.layoutWidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMinimumSize(QSize(91, 91))
        icon1 = QIcon()
        icon1.addFile(u":/icons/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QSize(50, 50))

        self.toolbarVLayout.addWidget(self.addButton)

        self.editButton = QPushButton(self.layoutWidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setEnabled(False)
        self.editButton.setMinimumSize(QSize(91, 91))
        icon2 = QIcon()
        icon2.addFile(u":/icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setIconSize(QSize(50, 50))

        self.toolbarVLayout.addWidget(self.editButton)

        self.makeListButton = QPushButton(self.layoutWidget)
        self.makeListButton.setObjectName(u"makeListButton")
        self.makeListButton.setEnabled(False)
        self.makeListButton.setMinimumSize(QSize(91, 91))
        icon3 = QIcon()
        icon3.addFile(u":/icons/cart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.makeListButton.setIcon(icon3)
        self.makeListButton.setIconSize(QSize(50, 50))

        self.toolbarVLayout.addWidget(self.makeListButton)

        self.deleteButton = QPushButton(self.layoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)
        self.deleteButton.setMinimumSize(QSize(91, 91))
        icon4 = QIcon()
        icon4.addFile(u":/icons/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteButton.setIcon(icon4)
        self.deleteButton.setIconSize(QSize(50, 50))

        self.toolbarVLayout.addWidget(self.deleteButton)

        self.saveButton = QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)
        self.saveButton.setMinimumSize(QSize(91, 91))
        icon5 = QIcon()
        icon5.addFile(u":/icons/floppy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon5)
        self.saveButton.setIconSize(QSize(50, 50))

        self.toolbarVLayout.addWidget(self.saveButton)

        self.uploadButton = QPushButton(self.layoutWidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setEnabled(True)
        self.uploadButton.setMinimumSize(QSize(91, 91))
        icon6 = QIcon()
        icon6.addFile(u":/icons/upload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.uploadButton.setIcon(icon6)
        self.uploadButton.setIconSize(QSize(50, 50))

        self.toolbarVLayout.addWidget(self.uploadButton)

        self.hSplitter.addWidget(self.toolbarFrame)
        self.pageFrame = QFrame(self.hSplitter)
        self.pageFrame.setObjectName(u"pageFrame")
        self.pageFrame.setMinimumSize(QSize(831, 0))
        self.pageFrame.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pageFrame.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.headerTextEdit = QTextEdit(self.pageFrame)
        self.headerTextEdit.setObjectName(u"headerTextEdit")
        self.headerTextEdit.setGeometry(QRect(130, 30, 581, 51))
        self.headerTextEdit.setReadOnly(True)
        self.stackedWidget = QStackedWidget(self.pageFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 100, 901, 541))
        self.catalogPage = QWidget()
        self.catalogPage.setObjectName(u"catalogPage")
        self.searchButton = QPushButton(self.catalogPage)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(10, 430, 101, 101))
        self.searchButton.setMinimumSize(QSize(91, 91))
        icon7 = QIcon()
        icon7.addFile(u":/icons/spyglass.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchButton.setIcon(icon7)
        self.searchButton.setIconSize(QSize(50, 50))
        self.catalogTable = QTableWidget(self.catalogPage)
        if (self.catalogTable.columnCount() < 3):
            self.catalogTable.setColumnCount(3)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.catalogTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.catalogTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.catalogTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.catalogTable.rowCount() < 17):
            self.catalogTable.setRowCount(17)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(11, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(12, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(13, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(14, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(15, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.catalogTable.setVerticalHeaderItem(16, __qtablewidgetitem19)
        icon8 = QIcon()
        icon8.addFile(u":/icons/star_clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/star_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setIcon(icon8);
        __qtablewidgetitem20.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(0, 0, __qtablewidgetitem20)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.catalogTable.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setCheckState(Qt.Unchecked);
        __qtablewidgetitem22.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setIcon(icon8);
        self.catalogTable.setItem(1, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font1);
        self.catalogTable.setItem(1, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setCheckState(Qt.Unchecked);
        __qtablewidgetitem25.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(1, 2, __qtablewidgetitem25)
        icon9 = QIcon()
        icon9.addFile(u":/icons/star_clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setIcon(icon9);
        self.catalogTable.setItem(2, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font1);
        self.catalogTable.setItem(2, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setCheckState(Qt.Unchecked);
        __qtablewidgetitem28.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(2, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setIcon(icon9);
        self.catalogTable.setItem(3, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font1);
        self.catalogTable.setItem(3, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setCheckState(Qt.Unchecked);
        __qtablewidgetitem31.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(3, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setIcon(icon9);
        self.catalogTable.setItem(4, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font1);
        self.catalogTable.setItem(4, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setCheckState(Qt.Unchecked);
        __qtablewidgetitem34.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(4, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setIcon(icon9);
        self.catalogTable.setItem(5, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font1);
        self.catalogTable.setItem(5, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setCheckState(Qt.Unchecked);
        __qtablewidgetitem37.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(5, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setIcon(icon9);
        self.catalogTable.setItem(6, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font1);
        self.catalogTable.setItem(6, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setCheckState(Qt.Unchecked);
        __qtablewidgetitem40.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(6, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setIcon(icon9);
        self.catalogTable.setItem(7, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font1);
        self.catalogTable.setItem(7, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setCheckState(Qt.Unchecked);
        __qtablewidgetitem43.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(7, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setIcon(icon9);
        self.catalogTable.setItem(8, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setFont(font1);
        self.catalogTable.setItem(8, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setCheckState(Qt.Unchecked);
        __qtablewidgetitem46.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(8, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setIcon(icon9);
        self.catalogTable.setItem(9, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font1);
        self.catalogTable.setItem(9, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setCheckState(Qt.Unchecked);
        __qtablewidgetitem49.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(9, 2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setIcon(icon9);
        self.catalogTable.setItem(10, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font1);
        self.catalogTable.setItem(10, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setCheckState(Qt.Unchecked);
        __qtablewidgetitem52.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(10, 2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setIcon(icon9);
        self.catalogTable.setItem(11, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setFont(font1);
        self.catalogTable.setItem(11, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setCheckState(Qt.Unchecked);
        __qtablewidgetitem55.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(11, 2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setIcon(icon9);
        self.catalogTable.setItem(12, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setFont(font1);
        self.catalogTable.setItem(12, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setCheckState(Qt.Unchecked);
        __qtablewidgetitem58.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(12, 2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setIcon(icon9);
        self.catalogTable.setItem(13, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setFont(font1);
        self.catalogTable.setItem(13, 1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setCheckState(Qt.Unchecked);
        __qtablewidgetitem61.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(13, 2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setIcon(icon9);
        self.catalogTable.setItem(14, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font1);
        self.catalogTable.setItem(14, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setCheckState(Qt.Unchecked);
        __qtablewidgetitem64.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(14, 2, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setIcon(icon9);
        self.catalogTable.setItem(15, 0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setFont(font1);
        self.catalogTable.setItem(15, 1, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setCheckState(Qt.Unchecked);
        __qtablewidgetitem67.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(15, 2, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setIcon(icon9);
        self.catalogTable.setItem(16, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setFont(font1);
        self.catalogTable.setItem(16, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setCheckState(Qt.Unchecked);
        __qtablewidgetitem70.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.catalogTable.setItem(16, 2, __qtablewidgetitem70)
        self.catalogTable.setObjectName(u"catalogTable")
        self.catalogTable.setEnabled(True)
        self.catalogTable.setGeometry(QRect(10, 10, 881, 411))
        self.catalogTable.setLineWidth(1)
        self.catalogTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.catalogTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.catalogTable.setAlternatingRowColors(True)
        self.catalogTable.setGridStyle(Qt.PenStyle.DotLine)
        self.catalogTable.setSortingEnabled(True)
        self.catalogTable.horizontalHeader().setVisible(True)
        self.catalogTable.horizontalHeader().setCascadingSectionResizes(True)
        self.catalogTable.horizontalHeader().setDefaultSectionSize(263)
        self.catalogTable.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.catalogTable.horizontalHeader().setStretchLastSection(False)
        self.catalogTable.verticalHeader().setProperty(u"showSortIndicator", True)
        self.lineEdit = QLineEdit(self.catalogPage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 450, 741, 61))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.lineEdit.setFont(font2)
        self.stackedWidget.addWidget(self.catalogPage)
        self.recipePage = QWidget()
        self.recipePage.setObjectName(u"recipePage")
        self.tabWidget = QTabWidget(self.recipePage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 881, 521))
        self.tabWidget.setFont(font)
        self.ingredientsTab = QWidget()
        self.ingredientsTab.setObjectName(u"ingredientsTab")
        self.ingredientsTable = QTableWidget(self.ingredientsTab)
        if (self.ingredientsTable.columnCount() < 2):
            self.ingredientsTable.setColumnCount(2)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setFont(font1);
        self.ingredientsTable.setHorizontalHeaderItem(0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setFont(font1);
        self.ingredientsTable.setHorizontalHeaderItem(1, __qtablewidgetitem72)
        if (self.ingredientsTable.rowCount() < 16):
            self.ingredientsTable.setRowCount(16)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(5, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(6, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(7, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(8, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(9, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(10, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(11, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(12, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(13, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(14, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.ingredientsTable.setVerticalHeaderItem(15, __qtablewidgetitem88)
        self.ingredientsTable.setObjectName(u"ingredientsTable")
        self.ingredientsTable.setGeometry(QRect(10, 10, 851, 461))
        self.ingredientsTable.horizontalHeader().setMinimumSectionSize(100)
        self.ingredientsTable.horizontalHeader().setStretchLastSection(True)
        self.ingredientsTable.verticalHeader().setMinimumSectionSize(40)
        self.ingredientsTable.verticalHeader().setDefaultSectionSize(40)
        self.tabWidget.addTab(self.ingredientsTab, "")
        self.instructionsTab = QWidget()
        self.instructionsTab.setObjectName(u"instructionsTab")
        self.instructionsList = QListWidget(self.instructionsTab)
        __qlistwidgetitem = QListWidgetItem(self.instructionsList)
        __qlistwidgetitem.setFont(font1);
        __qlistwidgetitem1 = QListWidgetItem(self.instructionsList)
        __qlistwidgetitem1.setFont(font1);
        __qlistwidgetitem2 = QListWidgetItem(self.instructionsList)
        __qlistwidgetitem2.setFont(font1);
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        __qlistwidgetitem3 = QListWidgetItem(self.instructionsList)
        __qlistwidgetitem3.setFont(font3);
        __qlistwidgetitem4 = QListWidgetItem(self.instructionsList)
        __qlistwidgetitem4.setFont(font1);
        self.instructionsList.setObjectName(u"instructionsList")
        self.instructionsList.setGeometry(QRect(10, 10, 851, 461))
        self.instructionsList.setAlternatingRowColors(True)
        self.instructionsList.setProperty(u"isWrapping", False)
        self.instructionsList.setSpacing(5)
        self.instructionsList.setUniformItemSizes(True)
        self.tabWidget.addTab(self.instructionsTab, "")
        self.stackedWidget.addWidget(self.recipePage)
        self.hSplitter.addWidget(self.pageFrame)
        mainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.backpageButton.setToolTip(QCoreApplication.translate("mainWindow", u"click to return to previous page", None))
#endif // QT_CONFIG(tooltip)
        self.backpageButton.setText("")
#if QT_CONFIG(tooltip)
        self.addButton.setToolTip(QCoreApplication.translate("mainWindow", u"add new recipe to catalog", None))
#endif // QT_CONFIG(tooltip)
        self.addButton.setText("")
#if QT_CONFIG(tooltip)
        self.editButton.setToolTip(QCoreApplication.translate("mainWindow", u"edit selected recipe", None))
#endif // QT_CONFIG(tooltip)
        self.editButton.setText("")
#if QT_CONFIG(tooltip)
        self.makeListButton.setToolTip(QCoreApplication.translate("mainWindow", u"generate grocery list with selected recipes", None))
#endif // QT_CONFIG(tooltip)
        self.makeListButton.setText("")
#if QT_CONFIG(tooltip)
        self.deleteButton.setToolTip(QCoreApplication.translate("mainWindow", u"delete selected recipe(s)", None))
#endif // QT_CONFIG(tooltip)
        self.deleteButton.setText("")
#if QT_CONFIG(tooltip)
        self.saveButton.setToolTip(QCoreApplication.translate("mainWindow", u"save changes", None))
#endif // QT_CONFIG(tooltip)
        self.saveButton.setText("")
#if QT_CONFIG(tooltip)
        self.uploadButton.setToolTip(QCoreApplication.translate("mainWindow", u"upload recipes with CSV file", None))
#endif // QT_CONFIG(tooltip)
        self.uploadButton.setText("")
        self.headerTextEdit.setHtml(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Recipe Catalog</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.searchButton.setToolTip(QCoreApplication.translate("mainWindow", u"search catalog", None))
#endif // QT_CONFIG(tooltip)
        self.searchButton.setText("")
        ___qtablewidgetitem = self.catalogTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mainWindow", u"Favorite", None));
        ___qtablewidgetitem1 = self.catalogTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mainWindow", u"Recipe Name", None));
        ___qtablewidgetitem2 = self.catalogTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("mainWindow", u"Select", None));

        __sortingEnabled = self.catalogTable.isSortingEnabled()
        self.catalogTable.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.catalogTable.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("mainWindow", u"Beef Stroganoff", None));
        ___qtablewidgetitem4 = self.catalogTable.item(1, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("mainWindow", u"Spaghetti and Meatballs", None));
        ___qtablewidgetitem5 = self.catalogTable.item(2, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("mainWindow", u"Tenderloin Steak", None));
        ___qtablewidgetitem6 = self.catalogTable.item(3, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("mainWindow", u"Vegan Hamburgers", None));
        ___qtablewidgetitem7 = self.catalogTable.item(4, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("mainWindow", u"Garbanzo Bean Salad", None));
        ___qtablewidgetitem8 = self.catalogTable.item(5, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("mainWindow", u"Sauerkraut", None));
        ___qtablewidgetitem9 = self.catalogTable.item(6, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("mainWindow", u"Matzo Ball Soup", None));
        ___qtablewidgetitem10 = self.catalogTable.item(7, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("mainWindow", u"Pancakes", None));
        ___qtablewidgetitem11 = self.catalogTable.item(8, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("mainWindow", u"Pho", None));
        ___qtablewidgetitem12 = self.catalogTable.item(9, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("mainWindow", u"Vegetarian Pizza", None));
        ___qtablewidgetitem13 = self.catalogTable.item(10, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("mainWindow", u"BBQ Salmon", None));
        ___qtablewidgetitem14 = self.catalogTable.item(11, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("mainWindow", u"Cherry Pie", None));
        ___qtablewidgetitem15 = self.catalogTable.item(12, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("mainWindow", u"Chocolate Cupcakes", None));
        ___qtablewidgetitem16 = self.catalogTable.item(13, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("mainWindow", u"Grilled Cheese Sandwiches", None));
        ___qtablewidgetitem17 = self.catalogTable.item(14, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("mainWindow", u"Roasted Potatoes", None));
        ___qtablewidgetitem18 = self.catalogTable.item(15, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("mainWindow", u"Mac and Cheese", None));
        ___qtablewidgetitem19 = self.catalogTable.item(16, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("mainWindow", u"Chickn Noodle Soup with Rice", None));
        self.catalogTable.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem20 = self.ingredientsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("mainWindow", u"Measurement", None));
        ___qtablewidgetitem21 = self.ingredientsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("mainWindow", u"Ingredient", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ingredientsTab), QCoreApplication.translate("mainWindow", u"Ingredients", None))

        __sortingEnabled1 = self.instructionsList.isSortingEnabled()
        self.instructionsList.setSortingEnabled(False)
        ___qlistwidgetitem = self.instructionsList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("mainWindow", u"1. First Instruction", None));
        ___qlistwidgetitem1 = self.instructionsList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("mainWindow", u"2. Second Instruction", None));
        ___qlistwidgetitem2 = self.instructionsList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("mainWindow", u"3. Third Instruction", None));
        ___qlistwidgetitem3 = self.instructionsList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("mainWindow", u"4. Fourth instruction", None));
        ___qlistwidgetitem4 = self.instructionsList.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("mainWindow", u"5. Fifth instruction", None));
        self.instructionsList.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.instructionsTab), QCoreApplication.translate("mainWindow", u"Instructions", None))
    # retranslateUi

