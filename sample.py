import tkinter as tk
from datetime import datetime, timedelta

# Function to predict the next menstrual cycle
def predict_cycle():
    name = name_entry.get()
    last_period_date_str = last_period_entry.get()
    cycle_length = int(cycle_length_entry.get())

    # Convert last_period_date_str to a datetime object
    last_period_date = datetime.strptime(last_period_date_str, "%Y-%m-%d")

    # Calculate the next expected menstrual date of next month
    next_period_date = last_period_date + timedelta(days=cycle_length)
    next_month = next_period_date.month
    while next_period_date.month == next_month:
        next_period_date += timedelta(days=cycle_length)

    # Calculate the expected menstrual cycle of the user
    expected_menstrual_cycle = next_period_date - last_period_date

    # Update the result_label with the user-entered data and the calculated dates
    result_label.config(text=f"Next period date for {name}: {next_period_date.strftime('%Y-%m-%d')}\n"
                              f"Expected menstrual cycle: {expected_menstrual_cycle.days} days")

# Create the main window
window = tk.Tk()
window.title("Menstrual Cycle Prediction")

# Create input fields and labels
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

last_period_label = tk.Label(window, text="Last Period Date (YYYY-MM-DD):")
last_period_label.pack()
last_period_entry = tk.Entry(window)
last_period_entry.pack()

cycle_length_label = tk.Label(window, text="Cycle Length (in days):")
cycle_length_label.pack()
cycle_length_entry = tk.Entry(window)
cycle_length_entry.pack()

# Create a button
predict_button = tk.Button(window, text="Predict Next Cycle", command=predict_cycle)
predict_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()