from random_variables import (RandomVariable, SmoothedRandomVariable, NormalRandomVariable, UniformRandomVariable,
                              LaplaceRandomVariable, ExponentialRandomVariable, CauchyRandomVariable)
from random_number_generators import SimpleRandomNumberGenerator
from bandwidth_calculator import calculate_bandwidth
from estimations import EDF, Histogram
from enums import DistComboBoxValues
from plotting import plot_distributions, plot_histograms
from PyQt5 import QtWidgets


import sys
import numpy as np
import ui_Lab2


class MyApplication(QtWidgets.QMainWindow, ui_Lab2.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.distComboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.calcButton.clicked.connect(self.calculate)
        self.bandwidthRadioButton.toggled.connect(self.on_bandwidth_radio_button_toggled)

    def on_combobox_changed(self) -> None:
        selected_text = self.distComboBox.currentText()

        if selected_text == DistComboBoxValues.UniformDist.value:
            lower_label, upper_label = ("a:", "b:")
        elif selected_text == DistComboBoxValues.ExponentialDist.value:
            lower_label, upper_label = ("lambda:", "")
            self.UpperBoundLabel.setEnabled(False)
            self.UpperBoundLineEdit.setEnabled(False)
        else:
            lower_label, upper_label = ("Сдвиг:", "Масштаб:")
            self.UpperBoundLabel.setEnabled(True)
            self.UpperBoundLineEdit.setEnabled(True)

        self.LowerBoundLabel.setText(lower_label)
        self.UpperBoundLabel.setText(upper_label)

    def on_bandwidth_radio_button_toggled(self, checked: bool) -> None:
        self.BandwidthLineEdit.setReadOnly(checked)

    def calculate(self) -> None:
        self.firstGraphWidget.clear()
        self.secondGraphWidget.clear()

        location, scale, N, bandwidth, m = self.get_input_parameters()

        rv = self.get_selected_random_variable(location, scale)

        generator = SimpleRandomNumberGenerator(rv)
        sample = generator.get(N)

        if self.bandwidthRadioButton.isChecked():
            bandwidth = calculate_bandwidth(sample)
            self.BandwidthLineEdit.clear()
            self.BandwidthLineEdit.setText(str(bandwidth))

        M = 100
        X = np.linspace(np.min(sample), np.max(sample), M)
        Y_truth = np.vectorize(rv.cdf)(X)

        edf = EDF(sample)
        Y_edf = np.vectorize(edf.value)(X)

        srv = SmoothedRandomVariable(sample, bandwidth)
        Y_kernel = np.vectorize(srv.cdf)(X)

        plot_distributions(self.firstGraphWidget, X, Y_truth, Y_edf, Y_kernel)

        hist = Histogram(sample, m)
        P_1 = np.vectorize(rv.pdf)(X)
        P_2 = np.vectorize(hist.value)(X)
        P_3 = np.vectorize(srv.pdf)(X)

        plot_histograms(self.secondGraphWidget, X, P_1, P_2, P_3)

    def get_input_parameters(self) -> tuple:
        return (
            float(self.LowerBoundLineEdit.text()),
            float(self.UpperBoundLineEdit.text()),
            int(self.NLineEdit.text()),
            float(self.BandwidthLineEdit.text()),
            int(self.MLineEdit.text())
        )

    def get_selected_random_variable(self, location: float, scale: float) -> RandomVariable:
        selected_text = self.distComboBox.currentText()

        if selected_text == DistComboBoxValues.NormalDist.value:
            rv = NormalRandomVariable(location, scale)
        if selected_text == DistComboBoxValues.UniformDist.value:
            rv = UniformRandomVariable(location, scale)
        elif selected_text == DistComboBoxValues.ExponentialDist.value:
            rv = ExponentialRandomVariable(location)
        elif selected_text == DistComboBoxValues.LaplaceDist.value:
            rv = LaplaceRandomVariable(location, scale)
        elif selected_text == DistComboBoxValues.CauchyDist.value:
            rv = CauchyRandomVariable(location, scale)

        return rv


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApplication()
    window.show()
    app.exec_()
