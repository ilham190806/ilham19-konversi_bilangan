from tkinter import *
from tkinter import messagebox

# Data warna resistor (digit, multiplier, tolerance)
color_data = {
    "Hitam": (0, 1, None),
    "Coklat": (1, 10, 1),
    "Merah": (2, 100, 2),
    "Oranye": (3, 1000, None),
    "Kuning": (4, 10000, None),
    "Hijau": (5, 100000, 0.5),
    "Biru": (6, 1000000, 0.25),
    "Ungu": (7, 10000000, 0.1),
    "Abu-abu": (8, None, 0.05),
    "Putih": (9, None, None),
    "Emas": (None, 0.1, 5),
    "Perak": (None, 0.01, 10)
}

def calculate_resistance():
    try:
        band1_color = band1_var.get()
        band2_color = band2_var.get()
        multiplier_color = multiplier_var.get()
        tolerance_color = tolerance_var.get()

        # Cek validitas warna
        if (band1_color not in color_data or 
            band2_color not in color_data or 
            multiplier_color not in color_data or 
            tolerance_color not in color_data):
            messagebox.showerror("Error", "Pastikan semua gelang sudah dipilih dengan benar.")
            return

        digit1 = color_data[band1_color][0]
        digit2 = color_data[band2_color][0]
        multiplier = color_data[multiplier_color][1]
        tolerance = color_data[tolerance_color][2]

        if None in (digit1, digit2, multiplier, tolerance):
            messagebox.showerror("Error", "Beberapa warna tidak memiliki nilai lengkap.")
            return

        base_value = int(str(digit1) + str(digit2))
        resistance = base_value * multiplier

        result_label.config(
            text=f"Nilai Resistor: {resistance} Ω ±{tolerance}%",
            fg="black"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# GUI
root = Tk()
root.title("Kalkulator Nilai Resistor 4-Gelang")
root.configure(bg="white")
root.geometry("340x460")

Label(root, text="Kalkulator Nilai Resistor 4-Gelang",
      font=("Arial", 14, "bold"), bg="white", fg="black").pack(pady=10)

# Variabel warna dengan default
first_color = list(color_data.keys())[0]
band1_var = StringVar(value=first_color)
band2_var = StringVar(value=first_color)
multiplier_var = StringVar(value=first_color)
tolerance_var = StringVar(value=first_color)

# Layout vertikal (label di atas, menu di bawah)
Label(root, text="Gelang 1 (Digit Pertama):", bg="white", anchor="w").pack(fill="x", padx=30)
OptionMenu(root, band1_var, *color_data.keys()).pack(pady=5)

Label(root, text="Gelang 2 (Digit Kedua):", bg="white", anchor="w").pack(fill="x", padx=30)
OptionMenu(root, band2_var, *color_data.keys()).pack(pady=5)

Label(root, text="Gelang 3 (Pengali):", bg="white", anchor="w").pack(fill="x", padx=30)
OptionMenu(root, multiplier_var, *color_data.keys()).pack(pady=5)

Label(root, text="Gelang 4 (Toleransi):", bg="white", anchor="w").pack(fill="x", padx=30)
OptionMenu(root, tolerance_var, *color_data.keys()).pack(pady=5)

# Tombol Hitung
Button(root, text="Hitung Nilai", command=calculate_resistance,
       bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
       relief=FLAT, padx=10, pady=5).pack(pady=20)

# Hasil
result_label = Label(root, text="Nilai Resistor: -", bg="white", fg="gray", font=("Arial", 12))
result_label.pack()

root.mainloop()