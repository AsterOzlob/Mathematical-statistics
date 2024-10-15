from pyqtgraph import mkPen
from PyQt5.QtWidgets import QWidget


PEN_RED = mkPen(color='r', width=2)
PEN_BLUE = mkPen(color='b', width=2)
PEN_GREEN = mkPen(color='g', width=2)


def plot_distributions(first_widget: QWidget, x, y_truth, y_edf, y_kernel) -> None:
    first_widget.plot(x, y_truth, pen=PEN_RED)
    first_widget.plot(x, y_edf, pen=PEN_BLUE)
    first_widget.plot(x, y_kernel, pen=PEN_GREEN)


def plot_histograms(second_widget: QWidget, x, p_1, p_2, p_3) -> None:
    second_widget.plot(x, p_1, pen=PEN_RED)
    second_widget.plot(x, p_2, pen=PEN_BLUE)
    second_widget.plot(x, p_3, pen=PEN_GREEN)
