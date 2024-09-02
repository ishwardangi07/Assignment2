import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_units():
    try:
        value = float(entry_value.get())
        category = combo_category.get()
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        result = None
        
        if category == 'Weight':
            result = convert_weight(value, from_unit, to_unit)
        elif category == 'Length':
            result = convert_length(value, from_unit, to_unit)
        elif category == 'Time':
            result = convert_time(value, from_unit, to_unit)
        elif category == 'Temperature':
            result = convert_temperature(value, from_unit, to_unit)

        if result is not None:
            if category == 'Time' and from_unit == 'Seconds' and to_unit == 'Hours':
                if result < 1:
                    minutes, seconds = divmod(result * 3600, 60)
                    label_result.config(text=f"{value} {from_unit} = {int(minutes)} minutes and {seconds:.2f} seconds")
                else:
                    hours, remaining_seconds = divmod(result * 3600, 3600)
                    minutes, seconds = divmod(remaining_seconds, 60)
                    label_result.config(text=f"{value} {from_unit} = {int(hours)} hours, {int(minutes)} minutes, and {seconds:.2f} seconds")
            else:
                label_result.config(text=f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            label_result.config(text="Invalid unit selection.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid numeric value.")

def convert_weight(value, from_unit, to_unit):
    if from_unit == 'Kilograms' and to_unit == 'Grams':
        return value * 1000
    elif from_unit == 'Grams' and to_unit == 'Kilograms':
        return value / 1000
    elif from_unit == 'Pounds' and to_unit == 'Kilograms':
        return value * 0.453592
    elif from_unit == 'Kilograms' and to_unit == 'Pounds':
        return value / 0.453592
    elif from_unit==to_unit:
        return value
    return None

def convert_length(value, from_unit, to_unit):
    if from_unit == 'Meters' and to_unit == 'Kilometers':
        return value / 1000
    elif from_unit == 'Kilometers' and to_unit == 'Meters':
        return value * 1000
    elif from_unit == 'Miles' and to_unit == 'Kilometers':
        return value * 1.60934
    elif from_unit == 'Kilometers' and to_unit == 'Miles':
        return value / 1.60934
    elif from_unit == 'Feet' and to_unit == 'Inches':
        return value * 12
    elif from_unit == 'Inches' and to_unit == 'Feet':
        return value / 12
    elif from_unit==to_unit:
        return value
    return None

def convert_time(value, from_unit, to_unit):
    if from_unit == 'Hours' and to_unit == 'Minutes':
        return value * 60
    elif from_unit == 'Hours' and to_unit == 'Seconds':
        return value * 3600
    elif from_unit == 'Minutes' and to_unit == 'Hours':
        return value / 60  # Return the value in hours
    elif from_unit == 'Minutes' and to_unit == 'Seconds':
        return value * 60
    elif from_unit == 'Seconds' and to_unit == 'Minutes':
        return value / 60  # Return the value in minutes
    elif from_unit == 'Seconds' and to_unit == 'Hours':
        return value / 3600  # Return the value in hours
    elif from_unit==to_unit:
        return value
    return None

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273) * 9/5 + 32
    elif from_unit==to_unit:
        return value
    return None

def update_units(event):
    category = combo_category.get()
    if category == 'Weight':
        units = ['Kilograms', 'Grams', 'Pounds']
    elif category == 'Length':
        units = ['Meters', 'Kilometers', 'Miles', 'Feet', 'Inches']
    elif category == 'Time':
        units = ['Hours', 'Minutes', 'Seconds']
    elif category == 'Temperature':
        units = ['Celsius', 'Fahrenheit', 'Kelvin']

    combo_from['values'] = units
    combo_to['values'] = units
    combo_from.current(0)
    combo_to.current(1)

# Create the main window
window = tk.Tk()
window.title("Unit Converter")
window.config(bg='white')# white backgrounded window is created

# Create and grid the widgets
label_category = ttk.Label(window, text="Category:")
label_category.grid(column=0, row=0, padx=10, pady=10)

combo_category = ttk.Combobox(window, values=['Weight', 'Length', 'Time', 'Temperature'])
combo_category.grid(column=1, row=0, padx=10, pady=10)
combo_category.current(0)
combo_category.bind("<<ComboboxSelected>>", update_units)

label_value = ttk.Label(window, text="Value:")
label_value.grid(column=0, row=1, padx=10, pady=10)

entry_value = ttk.Entry(window)
entry_value.grid(column=1, row=1, padx=10, pady=10)

label_from = ttk.Label(window, text="From:")
label_from.grid(column=0, row=2, padx=10, pady=10)

combo_from = ttk.Combobox(window)
combo_from.grid(column=1, row=2, padx=10, pady=10)

label_to = ttk.Label(window, text="To:")
label_to.grid(column=0, row=3, padx=10, pady=10)

combo_to = ttk.Combobox(window)
combo_to.grid(column=1, row=3, padx=10, pady=10)

button_convert = ttk.Button(window, text="Convert", command=convert_units)
button_convert.grid(column=1, row=4, padx=10, pady=10)

label_result = ttk.Label(window, text="",background="gray")
label_result.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Initialize with the default category
update_units(None)

# Start the main event loop
window.mainloop()
