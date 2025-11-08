import tkinter as tk
from tkinter import ttk, messagebox

# --- Fungsi Konversi ---
def konversi():
    """Mengambil nilai input dan basis asal, mengkonversinya ke Desimal, 
    kemudian mengkonversinya ke Biner, Oktal, dan Heksadesimal, 
    dan menampilkan hasilnya."""
    try:
        nilai_input = entry_nilai.get().strip()
        basis_asal = combo_asal.get()

        # Validasi input
        if not nilai_input:
            messagebox.showwarning("Peringatan", "Masukkan nilai terlebih dahulu!")
            return
        
        if not basis_asal:
             messagebox.showwarning("Peringatan", "Pilih basis asal!")
             return

        # Konversi nilai ke desimal terlebih dahulu
        if basis_asal == "Desimal":
            # Cek apakah input hanya berisi angka
            if not nilai_input.isdigit():
                raise ValueError
            desimal = int(nilai_input)
        elif basis_asal == "Biner":
            desimal = int(nilai_input, 2)
        elif basis_asal == "Oktal":
            desimal = int(nilai_input, 8)
        elif basis_asal == "Heksadesimal":
            desimal = int(nilai_input, 16)
        else:
            # Seharusnya tidak tercapai karena state="readonly"
            messagebox.showerror("Error", "Pilih basis asal!") 
            return

        # Konversi ke basis lain
        hasil_desimal.set(str(desimal))
        # bin(), oct(), dan hex() mengembalikan string dengan awalan ('0b', '0o', '0x'). [2:] menghapus awalan ini.
        hasil_biner.set(bin(desimal)[2:])
        hasil_oktal.set(oct(desimal)[2:])
        hasil_heksa.set(hex(desimal)[2:].upper()) # .upper() untuk hasil heksadesimal huruf kapital

    except ValueError:
        messagebox.showerror("Error", "Input tidak valid untuk basis yang dipilih!")

# --- Fungsi Reset ---
def reset():
    """Mengosongkan semua field input dan output."""
    entry_nilai.delete(0, tk.END)
    combo_asal.set("")
    hasil_desimal.set("")
    hasil_biner.set("")
    hasil_oktal.set("")
    hasil_heksa.set("")

# --- Membuat Jendela Utama ---
root = tk.Tk()
root.title("Konversi Bilangan")
root.geometry("420x450") # Sedikit lebih besar untuk tampilan yang lebih baik
root.resizable(False, False)
root.configure(bg="#f0f0f0") # Warna latar belakang jendela

# --- Judul Aplikasi ---
judul = tk.Label(root, text="Aplikasi Konversi Bilangan", 
                 font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333333")
judul.pack(pady=15)

# --- Frame Input ---
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10, padx=20)

tk.Label(frame_input, text="Masukkan Nilai:", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nilai = tk.Entry(frame_input, width=25, font=("Arial", 11), bd=2, relief=tk.SUNKEN)
entry_nilai.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Basis Asal:", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5, sticky="w")
basis_options = ["Desimal", "Biner", "Oktal", "Heksadesimal"]
combo_asal = ttk.Combobox(frame_input, values=basis_options, state="readonly", width=23, font=("Arial", 11))
combo_asal.grid(row=1, column=1, padx=5, pady=5)

# Mengatur default selection agar mirip gambar
# combo_asal.set("Desimal") 

# --- Tombol ---
frame_tombol = tk.Frame(root, bg="#f0f0f0") 
frame_tombol.pack(pady=15)

btn_konversi = tk.Button(frame_tombol, text="Konversi", command=konversi, width=15, 
                         bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), relief=tk.RAISED)
btn_konversi.grid(row=0, column=0, padx=10)

btn_reset = tk.Button(frame_tombol, text="Reset", command=reset, width=15, 
                      bg="#f44336", fg="white", font=("Arial", 11, "bold"), relief=tk.RAISED)
btn_reset.grid(row=0, column=1, padx=10)

# --- Hasil Konversi ---
frame_hasil = tk.Frame(root, bg="#f0f0f0")
frame_hasil.pack(pady=10, padx=20)

# Variabel untuk menampung hasil
hasil_desimal = tk.StringVar()
hasil_biner = tk.StringVar()
hasil_oktal = tk.StringVar()
hasil_heksa = tk.StringVar()

# Fungsi helper untuk membuat baris hasil
def create_result_row(frame, row_num, label_text, var):
    tk.Label(frame, text=label_text, width=15, anchor="w", font=("Arial", 11), bg="#f0f0f0").grid(row=row_num, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(frame, textvariable=var, width=25, state="readonly", font=("Arial", 11), bd=2, relief=tk.FLAT, bg="#e0e0e0").grid(row=row_num, column=1, padx=5, pady=5)

create_result_row(frame_hasil, 0, "Desimal:", hasil_desimal)
create_result_row(frame_hasil, 1, "Biner:", hasil_biner)
create_result_row(frame_hasil, 2, "Oktal:", hasil_oktal)
create_result_row(frame_hasil, 3, "Heksadesimal:", hasil_heksa)

# --- Footer ---
tk.Label(root, text="Dibuat dengan Python Tkinter", font=("Arial", 9, "italic"), 
         fg="gray", bg="#f0f0f0").pack(side="bottom", pady=10)

# --- Main Loop ---
root.mainloop()