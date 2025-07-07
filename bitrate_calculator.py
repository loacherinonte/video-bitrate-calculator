import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcola_bitrate():
    try:
        minuti = int(entry_minuti.get())
        secondi = int(entry_secondi.get())
        durata = minuti * 60 + secondi
        if durata <= 0:
            raise ValueError("La durata deve essere maggiore di zero.")

        dimensione_mb = float(entry_dimensione.get())
        dimensione_kb = dimensione_mb * 1024

        audio_bitrate = int(entry_audio_bitrate.get())

        bitrate_totale = (dimensione_kb * 8) / durata  # in kbps
        bitrate_video = bitrate_totale - audio_bitrate
        if bitrate_video <= 0:
            raise ValueError("Bitrate audio troppo alto per la dimensione/durata scelta.")

        risoluzione = combo_risoluzione.get()

        label_risultato.config(
            text=(
                f"Bitrate totale: {bitrate_totale:.0f} kbps\n"
                f"Bitrate video: {bitrate_video:.0f} kbps (audio: {audio_bitrate} kbps)"
            )
        )
    except ValueError as e:
        messagebox.showerror("Errore", f"Input non valido: {e}")

root = tk.Tk()
root.title("Calcolo Bitrate Video")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Durata del video").pack(pady=5)
frame_durata = tk.Frame(root)
frame_durata.pack()
tk.Label(frame_durata, text="Minuti:").pack(side=tk.LEFT)
entry_minuti = tk.Entry(frame_durata, width=5)
entry_minuti.pack(side=tk.LEFT, padx=5)
tk.Label(frame_durata, text="Secondi:").pack(side=tk.LEFT)
entry_secondi = tk.Entry(frame_durata, width=5)
entry_secondi.pack(side=tk.LEFT)

tk.Label(root, text="Dimensione desiderata (MB)").pack(pady=5)
entry_dimensione = tk.Entry(root)
entry_dimensione.pack()

tk.Label(root, text="Bitrate audio (kbps)").pack(pady=5)
entry_audio_bitrate = tk.Entry(root)
entry_audio_bitrate.pack()
entry_audio_bitrate.insert(0, "128")  # valore di default

tk.Label(root, text="Risoluzione").pack(pady=5)
combo_risoluzione = ttk.Combobox(root, values=[
    "1280x720 (HD)",
    "1920x1080 (Full HD)",
    "2560x1440 (2K)",
    "3840x2160 (4K)",
    "7680x4320 (8K)"
])
combo_risoluzione.set("1920x1080 (Full HD)")
combo_risoluzione.pack()

tk.Button(root, text="Calcola Bitrate", command=calcola_bitrate).pack(pady=10)

label_risultato = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_risultato.pack(pady=10)

root.mainloop()
