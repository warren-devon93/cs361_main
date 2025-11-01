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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSplitter, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1070, 721)
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
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
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
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.ingredientsTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.ingredientsTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.ingredientsTable.setObjectName(u"ingredientsTable")
        self.ingredientsTable.setGeometry(QRect(10, 10, 851, 461))
        self.ingredientsTable.horizontalHeader().setMinimumSectionSize(100)
        self.ingredientsTable.horizontalHeader().setStretchLastSection(True)
        self.ingredientsTable.verticalHeader().setMinimumSectionSize(40)
        self.ingredientsTable.verticalHeader().setDefaultSectionSize(40)
        self.tabWidget.addTab(self.ingredientsTab, "")
        self.instructionsTab = QWidget()
        self.instructionsTab.setObjectName(u"instructionsTab")
        self.instructionsTable = QTableWidget(self.instructionsTab)
        if (self.instructionsTable.columnCount() < 1):
            self.instructionsTable.setColumnCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.instructionsTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        self.instructionsTable.setObjectName(u"instructionsTable")
        self.instructionsTable.setGeometry(QRect(10, 10, 851, 461))
        self.instructionsTable.horizontalHeader().setVisible(False)
        self.instructionsTable.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.instructionsTab, "")
        self.stackedWidget.addWidget(self.recipePage)
        self.hSplitter.addWidget(self.pageFrame)
        mainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ingredientsTab), QCoreApplication.translate("mainWindow", u"Ingredients", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.instructionsTab), QCoreApplication.translate("mainWindow", u"Instructions", None))
    # retranslateUi

