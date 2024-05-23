import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class BankQueueApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bank Queue Time Calculator')

        # Create widgets
        self.customer_label = QLabel('Kaç müşteri işlem yapıyor:')
        self.customer_input = QLineEdit()

        self.hours_label = QLabel('Banka kaç saat açık:')
        self.hours_input = QLineEdit()

        self.staff_label = QLabel('Bankada kaç çalışan var:')
        self.staff_input = QLineEdit()

        self.calculate_button = QPushButton('Hesapla')
        self.result_label = QLabel('Beklenen bekleme süresi: ')

        # Connect button to function
        self.calculate_button.clicked.connect(self.calculate_wait_time)

        # Create layouts
        layout = QVBoxLayout()

        layout.addWidget(self.customer_label)
        layout.addWidget(self.customer_input)

        layout.addWidget(self.hours_label)
        layout.addWidget(self.hours_input)

        layout.addWidget(self.staff_label)
        layout.addWidget(self.staff_input)

        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_wait_time(self):
        # Get inputs
        try:
            customers = int(self.customer_input.text())
            hours_open = float(self.hours_input.text())
            staff_count = int(self.staff_input.text())

            # Calculate expected wait time
            if staff_count > 0:
                wait_time = (customers / staff_count) / hours_open
                self.result_label.setText(f'Beklenen bekleme süresi: {wait_time:.2f} saat')
            else:
                self.result_label.setText('Çalışan sayısı sıfırdan büyük olmalı')
        except ValueError:
            self.result_label.setText('Lütfen tüm alanları doğru doldurunuz')


def main():
    app = QApplication(sys.argv)
    ex = BankQueueApp()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
