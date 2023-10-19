from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QPlainTextEdit,QVBoxLayout,
                             QWidget, QPushButton, QLabel
                             )


class MainWindow(QMainWindow):
    def __init__(self,) -> None:
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        
        self.input_code = QPlainTextEdit()
        self.run = QPushButton('run')
        self.natija = QLabel("...")
        
        self.main_layout.addWidget(self.input_code)
        self.main_layout.addWidget(self.run)
        self.main_layout.addWidget(self.natija)
        
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)
        
        self.run.clicked.connect(self.run_code)
        
        
    def run_code(self):
        code = self.input_code.toPlainText()
        print(code)
        
        with open('problem.py', 'w+') as f:
            txt = """import sys\nfl = open('out.txt','w+')\nsys.stdout = fl"""
            txt += "\n" + code
            
            f.write(txt)
            
        import os
        os.system("python3 problem.py")
        fl = open('out.txt','r')
        self.natija.setText(fl.read())

            
            

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()