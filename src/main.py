import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class FolderCreator(QtWidgets.QMainWindow):
    def __init__(self):
        super(FolderCreator, self).__init__()
        # Load the UI file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ui_path    = os.path.join(script_dir, '..', 'ui', 'folder_creator.ui')
        uic.loadUi(ui_path, self)
        
        # Initialize variables
        self.selected_path = ""
        
        # Connect signals
        self.radio3D.toggled.connect(self.on_project_type_changed)
        self.radioProgramming.toggled.connect(self.on_project_type_changed)
        self.btnSelectPath.clicked.connect(self.select_path)
        self.btnCreate.clicked.connect(self.create_folders)
        
        # Set initial state
        self.radio3D.setChecked(True)
        self.stackedWidget.setCurrentIndex(0)
        
    def on_project_type_changed(self):
        """Handle project type radio button changes"""
        if self.radio3D.isChecked():
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)
            
    def select_path(self):
        """Open file dialog to select project path"""
        path = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if path:
            self.selected_path = path
            self.pathEdit.setText(path)
            
    def create_folders(self):
        """Create the selected folders"""
        if not self.selected_path:
            QMessageBox.warning(self, "Error", "Please select a path first!")
            return
            
        folders = []
        
        if self.radio3D.isChecked():
            # 3D printing folders
            if self.checkSTL.isChecked():
                folders.append("STL")
            if self.checkDesigns.isChecked():
                folders.append("Designs")
            if self.checkGcode.isChecked():
                folders.append("G-code")
            if self.checkSources.isChecked():
                folders.append("Sources")
            if self.checkPrints.isChecked():
                folders.append("Print_Logs")
            if self.checkSettings.isChecked():
                folders.append("Printer_Settings")
        else:
            # Programming folders - General
            if self.checkSrc.isChecked():
                folders.append("src")
            if self.checkLib.isChecked():
                folders.append("lib")
            if self.checkDocs.isChecked():
                folders.append("docs")
            if self.checkTests.isChecked():
                folders.append("tests")
            if self.checkConfig.isChecked():
                folders.append("config")
            if self.checkAssets.isChecked():
                folders.append("assets")
                
            # Web development
            if self.checkStatic.isChecked():
                folders.append("static")
            if self.checkViews.isChecked():
                folders.append("views")
            if self.checkComponents.isChecked():
                folders.append("components")
                
            # ML/Data
            if self.checkNotebooks.isChecked():
                folders.append("notebooks")
            if self.checkModels.isChecked():
                folders.append("models")
            if self.checkDatasets.isChecked():
                folders.append("datasets")
                
        # Create the folders
        try:
            for folder in folders:
                folder_path = os.path.join(self.selected_path, folder)
                os.makedirs(folder_path, exist_ok=True)
            QMessageBox.information(self, "Success", "Folders created successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error creating folders: {str(e)}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FolderCreator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()