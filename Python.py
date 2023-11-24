import sqlite3
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menentukan prediksi fakultas berdasarkan nilai tertinggi
def prediksi_fakultas(biologi, fisika, inggris):
    if biologi > fisika and biologi > inggris:
        return "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        return "Teknik"
    elif inggris > biologi and inggris > fisika:
        return "Bahasa"
    else:
        return "Tidak dapat diprediksi"

# Fungsi membuat Hover
def on_hover(event):
    predict_button.config(bg='gray', fg='white')

def on_leave(event):
    predict_button.config(bg='SystemButtonFace', fg='black')

# Fungsi untuk menyimpan data ke database SQLite
def simpan_data(nama_siswa, biologi, fisika, inggris):
    try:
        conn = sqlite3.connect("C:\Pemrograman Multiplatform\Database dan Python\database.db")
        cursor = conn.cursor()

        # Membuat tabel jika belum ada
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nilai_siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_siswa TEXT,
                biologi INTEGER,
                fisika INTEGER,
                inggris INTEGER,
                prediksi_fakultas TEXT
            )
        ''')

        # Menghitung prediksi fakultas
        prediksi = prediksi_fakultas(biologi, fisika, inggris)

        # Memasukkan data ke tabel
        cursor.execute('''
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        ''', (nama_siswa, biologi, fisika, inggris, prediksi))

        conn.commit()
        conn.close()

        messagebox.showinfo("Info", "Data berhasil disimpan.")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk menangani tombol submit
def submit_nilai():
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    simpan_data(nama_siswa, biologi, fisika, inggris)

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas")

# Label dan Entry untuk Nama Siswa
label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

# Label dan Entry untuk Nilai Biologi
label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

# Label dan Entry untuk Nilai Fisika
label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

# Label dan Entry untuk Nilai Inggris
label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

# Button untuk hasil prediksi
predict_button = tk.Button(root, text="Submit", command=submit_nilai)
predict_button.pack()
predict_button.pack(pady=20)
predict_button.bind("<Enter>", on_hover)
predict_button.bind("<Leave>", on_leave)

# Menjalankan loop utama Tkinter
root.mainloop()