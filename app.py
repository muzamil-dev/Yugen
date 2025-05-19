from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__ (self):
        super().__init__()

        # print("MainWindow") okay so thats not how you print in the window
        self.setWindowTitle("Yugen")
                
        # Create a label and set it as the central widget
        hello = QLabel("One Piece")
        # self.setCentralWidget(hello)no longer needed as I will use the layout
        
        # creating a image label and getting the image
        self.image_label = QLabel()
        pixmap = QPixmap("MVOP.jpg")
        self.image_label.setPixmap(pixmap)
        # Make it resize to fit
        self.image_label.setScaledContents(True)  
        # Width x Height
        self.image_label.setFixedSize(200, 300)   

        # layout for multiple widgets
        layout = QVBoxLayout()
        layout.addWidget(hello) #adds the hello
        layout.addWidget(self.image_label)

        # set layout on q widget 
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
# window = QWidget() not gonna use this
window = MainWindow()  # Use the MainWindow class instead

window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
