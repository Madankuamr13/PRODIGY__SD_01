import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def create_gui():
    def convert_temperature():
        try:
            temperature = float(entry_temp.get())
            unit = unit_var.get()
            
            if unit == "Celsius":
                celsius = temperature
                fahrenheit = celsius_to_fahrenheit(celsius)
                kelvin = celsius_to_kelvin(celsius)
            elif unit == "Fahrenheit":
                fahrenheit = temperature
                celsius = fahrenheit_to_celsius(fahrenheit)
                kelvin = fahrenheit_to_kelvin(fahrenheit)
            elif unit == "Kelvin":
                kelvin = temperature
                celsius = kelvin_to_celsius(kelvin)
                fahrenheit = kelvin_to_fahrenheit(kelvin)
            
            lbl_result.config(text=f"Fahrenheit: {fahrenheit:.2f}°F\nCelsius: {celsius:.2f}°C\nKelvin: {kelvin:.2f}K")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid temperature.")
    
    root = tk.Tk()
    root.title("Temperature Converter")
    
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    lbl_temp = ttk.Label(frame, text="Temperature:")
    lbl_temp.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
    
    entry_temp = ttk.Entry(frame)
    entry_temp.grid(row=0, column=1, padx=5, pady=5)
    
    unit_var = tk.StringVar()
    unit_var.set("Celsius")
    
    lbl_unit = ttk.Label(frame, text="Unit:")
    lbl_unit.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
    
    combo_unit = ttk.Combobox(frame, textvariable=unit_var)
    combo_unit['values'] = ("Celsius", "Fahrenheit", "Kelvin")
    combo_unit.grid(row=1, column=1, padx=5, pady=5)
    
    btn_convert = ttk.Button(frame, text="Convert", command=convert_temperature)
    btn_convert.grid(row=2, column=0, columnspan=2, pady=10)
    
    lbl_result = ttk.Label(frame, text="", font=("Arial", 12))
    lbl_result.grid(row=3, column=0, columnspan=2, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
