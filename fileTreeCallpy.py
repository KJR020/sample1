import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileSystemModel
from fileTreeUi import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # ここから、ファイルツリー表示用のコード
        path = r"C:\Users\jiro-\work\PyQt"
        self.model = QFileSystemModel()
        self.model.setRootPath(path)
        self.model.setNameFilters(["*.py", "*.ui"])  # この設定だけだと、非該当の拡張子はグレー表示
        self.model.setNameFilterDisables(False)  # 上記フィルターに該当しないファイルは非表示
        view = self.ui.treeView
        view.setModel(self.model)
        view.setRootIndex(self.model.index(path))
        view.setColumnWidth(0, 260)

        view.clicked.connect(self.getFileName)

    # クリックした際のメソッド
    def getFileName(self, index):
        from PyQt5.QtWidgets import QMessageBox
        import os

        filepath = []
        indexItem = self.model.index(index.row(), 0, index.parent())
        if os.path.isfile(self.model.filePath(indexItem)):
            filepath.insert(0, self.model.filePath(indexItem))
            QMessageBox.information(
                None, "Notice!", filepath[0] + "\n\n is Selected", QMessageBox.Yes
            )
        else:
            QMessageBox.warning(None, "Notice!", "Select File!", QMessageBox.Yes)


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
