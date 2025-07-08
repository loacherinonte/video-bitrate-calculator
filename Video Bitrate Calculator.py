import tkinter as tk
from tkinter import ttk, messagebox

current_language = "en"

labels = {
    "en": {
        "title": "Video Bitrate Calculator",
        "duration": "Video duration",
        "minutes": "Minutes:",
        "seconds": "Seconds:",
        "size": "Target size (MB)",
        "audio_bitrate": "Audio bitrate (kbps)",
        "resolution": "Resolution",
        "calculate": "Calculate Bitrate",
        "language_menu": "Language",
        "credits_menu": "Credits",
        "credits_text": "App created by Rino Caccamo",
        "error": "Invalid input",
        "result": "Total bitrate: {total:.0f} kbps\nVideo bitrate: {video:.0f} kbps (audio: {audio} kbps)"
    },
    "it": {
        "title": "Calcolatore Bitrate Video",
        "duration": "Durata del video",
        "minutes": "Minuti:",
        "seconds": "Secondi:",
        "size": "Dimensione desiderata (MB)",
        "audio_bitrate": "Bitrate audio (kbps)",
        "resolution": "Risoluzione",
        "calculate": "Calcola Bitrate",
        "language_menu": "Lingua",
        "credits_menu": "Crediti",
        "credits_text": "App creata da Rino Caccamo",
        "error": "Input non valido",
        "result": "Bitrate totale: {total:.0f} kbps\nBitrate video: {video:.0f} kbps (audio: {audio} kbps)"
    }
}

def set_language(lang):
    global current_language
    current_language = lang
    l = labels[current_language]
    root.title(l["title"])
    label_durata.config(text=l["duration"])
    label_minuti.config(text=l["minutes"])
    label_secondi.config(text=l["seconds"])
    label_size.config(text=l["size"])
    label_audio.config(text=l["audio_bitrate"])
    label_resol.config(text=l["resolution"])
    button_calcola.config(text=l["calculate"])
    ricrea_menu()

def calcola_bitrate():
    try:
        minuti = int(entry_minuti.get())
        secondi = int(entry_secondi.get())
        durata = minuti * 60 + secondi
        if durata <= 0:
            raise ValueError("Durata non valida")

        dimensione_mb = float(entry_dimensione.get())
        audio_bitrate = int(entry_audio_bitrate.get())

        dimensione_kb = dimensione_mb * 1024
        bitrate_totale = (dimensione_kb * 8) / durata
        bitrate_video = bitrate_totale - audio_bitrate
        if bitrate_video <= 0:
            raise ValueError("Bitrate audio troppo alto")

        l = labels[current_language]
        label_risultato.config(text=l["result"].format(
            total=bitrate_totale,
            video=bitrate_video,
            audio=audio_bitrate
        ))

    except ValueError:
        messagebox.showerror("Errore", labels[current_language]["error"])

def mostra_crediti():
    l = labels[current_language]
    messagebox.showinfo(l["credits_menu"], l["credits_text"])

def ricrea_menu():
    menubar = tk.Menu(root)

    language_menu = tk.Menu(menubar, tearoff=0)
    language_menu.add_command(label="English", command=lambda: set_language("en"))
    language_menu.add_command(label="Italiano", command=lambda: set_language("it"))
    menubar.add_cascade(label=labels[current_language]["language_menu"], menu=language_menu)

    credits_menu = tk.Menu(menubar, tearoff=0)
    credits_menu.add_command(label=labels[current_language]["credits_menu"], command=mostra_crediti)
    menubar.add_cascade(label=labels[current_language]["credits_menu"], menu=credits_menu)

    root.config(menu=menubar)

# === GUI ===
root = tk.Tk()
root.geometry("400x400")
root.resizable(False, False)
root.title(labels[current_language]["title"])

ricrea_menu()

label_durata = tk.Label(root, text=labels[current_language]["duration"])
label_durata.pack(pady=5)

frame_durata = tk.Frame(root)
frame_durata.pack()
label_minuti = tk.Label(frame_durata, text=labels[current_language]["minutes"])
label_minuti.pack(side=tk.LEFT)
entry_minuti = tk.Entry(frame_durata, width=5)
entry_minuti.pack(side=tk.LEFT, padx=5)
label_secondi = tk.Label(frame_durata, text=labels[current_language]["seconds"])
label_secondi.pack(side=tk.LEFT)
entry_secondi = tk.Entry(frame_durata, width=5)
entry_secondi.pack(side=tk.LEFT)

label_size = tk.Label(root, text=labels[current_language]["size"])
label_size.pack(pady=5)
entry_dimensione = tk.Entry(root)
entry_dimensione.pack()

label_audio = tk.Label(root, text=labels[current_language]["audio_bitrate"])
label_audio.pack(pady=5)
entry_audio_bitrate = tk.Entry(root)
entry_audio_bitrate.insert(0, "128")
entry_audio_bitrate.pack()

label_resol = tk.Label(root, text=labels[current_language]["resolution"])
label_resol.pack(pady=5)
combo_risoluzione = ttk.Combobox(root, values=[
    "1280x720 (HD)",
    "1920x1080 (Full HD)",
    "2560x1440 (2K)",
    "3840x2160 (4K)",
    "7680x4320 (8K)"
])
combo_risoluzione.set("1920x1080 (Full HD)")
combo_risoluzione.pack()

button_calcola = tk.Button(root, text=labels[current_language]["calculate"], command=calcola_bitrate)
button_calcola.pack(pady=10)

label_risultato = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_risultato.pack(pady=10)

root.mainloop()
