import sys
from PyQt5 import QtWidgets
import numpy as np
import math
import design_file
import functions


class ExampleApp(QtWidgets.QMainWindow, design_file.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Настройка графиков
        self.graph1_widget.setBackground("w")
        self.graph1_widget.setLogMode(x=True)
        self.graph1_widget.setYRange(0, 1)

        self.graph2_widget.setBackground("w")
        self.graph2_widget.setLogMode(x=True)
        self.graph2_widget.setYRange(0, 1)

        self.exp_pushButton.clicked.connect(self.calculate)

    def calculate(self) -> None:
        n = int(self.n_lineEdit.text())
        m = int(self.m_lineEdit.text())
        alpha = float(self.alpha_doubleSpinBox.text().replace(',', '.'))
        confidence_interval = np

        self.graph1_widget.clear()
        self.graph2_widget.clear()

        # Построение графика зависимости частоты от N для каждой серии M
        vs = functions.exp_serial(m, n)

        for i in range(m):
            self.graph1_widget.plot(range(1, n + 1), vs[i], pen='black')

        # Доверительный интервал
        confidence_interval = functions.conf_interval(vs, alpha)

        self.graph1_widget.plot(range(1, n + 1), confidence_interval[0,], pen="blue")
        self.graph1_widget.plot(range(1, n + 1), confidence_interval[1,], pen="blue")

        # Среднее
        mean_values = functions.mean(vs)

        self.graph1_widget.plot(range(1, n + 1), mean_values, pen='red')

        # Построение графика ошибки
        # Подсчёт зависимости экспериментальной ошибки от N
        exp_error = (confidence_interval[1,] - confidence_interval[0,]) / 2

        # Вычисляем теоретическую ошибку частоты от N
        coef = functions.normal_quantile((1 + alpha) / 2)

        theory_error = np.zeros(n)
        for i in range(1, n + 1):
            theory_error[i - 1] = coef * math.sqrt(0.5 * 0.5 / i)

        # Построение графиков ошибки
        self.graph2_widget.plot(range(1, n + 1), theory_error, pen='blue')
        self.graph2_widget.plot(range(1, n + 1), exp_error, pen='red')

        # Вывод результатов моделирования
        self.resultLineEdit.clear()

        self.resultLineEdit.setText(
            f"{round(mean_values[-1], 5)} +- {round((confidence_interval[1, -1] - confidence_interval[0, -1]) / 2, 5)}")


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
