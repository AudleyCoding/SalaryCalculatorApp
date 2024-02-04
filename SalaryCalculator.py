"""A salary calculator specifically designed for part-time teachers in Taiwan,
taking into account their unique pay structure and tax regulations.

It allows users to easily select work days on a calendar and calculates their
estimated salary based on pre-defined settings (not implemented yet).

Questions:
1. Is inheriting from both QtWidgets.QMainWindow and Ui_SalaryCalculator necessary?
2.
3.
4.
"""

import sys
from PySide6 import QtWidgets, QtGui, Qt
from PySide6.QtCore import QDate
import calendar

from SalaryCalcDesign import Ui_SalaryCalculator


class SalaryCalcApp(QtWidgets.QMainWindow, Ui_SalaryCalculator):
    """
        This class represents the main application window and inherits from both
        the Qt Main Window class and the generated UI class (Ui_SalaryCalculator)
        to combine application logic and layout management.

        It handles interactions with UI elements like the calendar and buttons,
        manages data (such as selected dates) and performs calculations (to be implemented).
        """
    def __init__(self):
        super(SalaryCalcApp, self).__init__()
        self.setupUi(self)

        # Initialize an empty list to store the selected work days (CHANGE THIS TO A SET)
        self.selected_dates = []

        # Create a QTextCharFormat object to visually highlight selected dates in the calendar
        self.selected_date_format = QtGui.QTextCharFormat()
        self.selected_date_format.setBackground(QtGui.QColor("gray"))

        # Connect the calendar's signal emitted when the selection changes to update the list and formatting
        self.calendarWidget.selectionChanged.connect(lambda: self.update_selected_dates(self.calendarWidget))

        # Connect the Clear button's click signal to the function that clears all selections
        self.ClearButton.clicked.connect(self.clear_calendar)


    def update_selected_dates(self, calendar):
        """
        Handles adding/removing selected dates from the list and updating their visual appearance in the calendar.
        - Retrieves the currently selected date.
        - Checks if it's already selected:
            - If yes, removes it from the list and resets its format to default.
            - If no, adds it to the list and applies the selected date format.
        - Prints the updated list for debugging or demonstration purposes.
        """
        # Get the currently selected date
        current_date = calendar.selectedDate()

        # Check if the date is already in the list
        if current_date in self.selected_dates:
            # Remove it from the list
            self.selected_dates.remove(current_date)
            # Reset its text format
            calendar.setDateTextFormat(current_date, QtGui.QTextCharFormat())
        else:
            # Add it to the list
            self.selected_dates.append(current_date)
            # Set its text format to selected
            calendar.setDateTextFormat(current_date, self.selected_date_format)
        # Print the list
        print(self.selected_dates)

    # Create a function to clear the calendar of all selected dates
    def clear_calendar(self):
        """
        Clears all selected dates from the calendar and resets their visual appearance.
        - Gets the year and month of the currently selected date.
        - Calculates the first and last day of the month.
        - Iterates through all days in the month and resets their formatting to default.
        - Clears the selected dates list.
        - Prints the cleared list for debugging or demonstration purposes.
        """
        selected_date = self.calendarWidget.selectedDate()
        year, month = selected_date.year(), selected_date.month()
        first_day = QDate(year, month, 1)
        last_day = QDate(year, month + 1, 1).addDays(-1)

        # Clear formatting for each date in the month:
        for day in range(1, last_day.day() + 1):
            date = QDate(year, month, day)
            self.calendarWidget.setDateTextFormat(date, QtGui.QTextCharFormat())  # Apply default format to each date

        # Clear the selected dates list:
        self.selected_dates = []
        # Print the list
        print(self.selected_dates)


app = QtWidgets.QApplication(sys.argv)

window = SalaryCalcApp()
window.show()
app.exec()