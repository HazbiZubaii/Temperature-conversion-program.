import tkinter as tk
from tkinter import messagebox

# Conversion functions
def celsius_to_other_scales(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def fahrenheit_to_other_scales(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return celsius, kelvin

def kelvin_to_other_scales(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit

def convert_temperature():
    try:
        value = float(entry_temp.get())
        scale = dropdown_var.get()

        if scale == "Celsius":
            fahrenheit, kelvin = celsius_to_other_scales(value)
            result_label.config(
                text=f"{value:.2f} °C = {fahrenheit:.2f} °F\n{value:.2f} °C = {kelvin:.2f} K"
            )
        elif scale == "Fahrenheit":
            celsius, kelvin = fahrenheit_to_other_scales(value)
            result_label.config(
                text=f"{value:.2f} °F = {celsius:.2f} °C\n{value:.2f} °F = {kelvin:.2f} K"
            )
        elif scale == "Kelvin":
            celsius, fahrenheit = kelvin_to_other_scales(value)
            result_label.config(
                text=f"{value:.2f} K = {celsius:.2f} °C\n{value:.2f} K = {fahrenheit:.2f} °F"
            )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid temperature value.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Temperature Converter")

# Input Temperature
tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for Scale
tk.Label(root, text="Select Scale:").grid(row=1, column=0, padx=10, pady=10)
dropdown_var = tk.StringVar(value="Celsius")
dropdown = tk.OptionMenu(root, dropdown_var, "Celsius", "Fahrenheit", "Kelvin")
dropdown.grid(row=1, column=1, padx=10, pady=10)

# Convert Button
convert_btn = tk.Button(root, text="Convert", command=convert_temperature)
convert_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
