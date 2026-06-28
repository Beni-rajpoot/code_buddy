import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Step 1: App banayen (har PyQt5 app ko ek "QApplication" chahiye hota hai)
app = QApplication(sys.argv)

# Step 2: Window banayen
window = QWidget()
window.setWindowTitle("Meri Pehli PyQt5 App")
window.setGeometry(100, 100, 400, 300)  # x, y, width, height

# Step 3: Window dikhayen
window.show()

# Step 4: App ko "chalate" rakhen (warna window foran band ho jayegi)
sys.exit(app.exec_())