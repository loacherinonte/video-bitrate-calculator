![Anteprima dell'app](https://github.com/loacherinonte/video-bitrate-calculator/raw/main/vbc.png)

# 🎥 Video Bitrate Calculator

# 🇺🇸
Video Bitrate Calculator is a simple desktop app that helps you calculate the optimal video bitrate based on the desired file size, video duration, and audio bitrate. It features a clean graphical interface, multilingual support (English and Italian), and allows you to select common resolutions like 1080p, 2K, 4K and more. The app is available for both Windows and macOS, with a one-click installer for each platform. Developed by Rino Caccamo.

# The bitrate (in kilobits per second, kbps) is calculated by dividing the file size (in bits) by the duration (in seconds):

Bitrate (kbps) = Size (bits) / Duration (seconds)

# Since file sizes are usually measured in megabytes (MB), convert MB to kilobits by multiplying:

Size (bits) = Desired size in MB × 1024 (KB per MB) × 8 (kilobits per KB)

# Example:

For a 1 MB file with duration 1 second:

1 MB × 1024 × 8 = 8192 kilobits / 1 second = 8192 kbps

---

# 🇮🇹 
Video Bitrate Calculator è una semplice applicazione desktop che ti aiuta a calcolare il bitrate video ottimale in base alla dimensione desiderata del file, alla durata del video e al bitrate audio. Ha un'interfaccia grafica pulita, supporto multilingua (inglese e italiano) e permette di selezionare risoluzioni comuni come 1080p, 2K, 4K e altre. L'app è disponibile sia per Windows che per macOS, con un installer a un solo clic per ogni piattaforma. Sviluppata da Rino Caccamo.

# Il bitrate (in kilobit al secondo, kbps) si calcola dividendo la dimensione del file (in bit) per la durata (in secondi):

Bitrate (kbps) = Dimensione (bit) / Durata (secondi)

# Poiché la dimensione del file è solitamente espressa in megabyte (MB), si converte MB in kilobit moltiplicando:

Dimensione (bit) = Dimensione desiderata in MB × 1024 (KB per MB) × 8 (kilobit per KB)

# Esempio:

Per un file di 1 MB e durata 1 secondo:

1 MB × 1024 × 8 = 8192 kilobit / 1 secondo = 8192 kbps

---

## ▶️ 🇺🇸 Run from Python source

To run the app directly from the Python source file (`Video Bitrate Calculator.py`), make sure you have Python 3 installed with Tkinter and Pillow. Then open a terminal or command prompt, navigate to the folder where the file is saved, and run:

## ▶️ 🇮🇹 Esegui dal codice sorgente Python
Per eseguire l'app direttamente dal file sorgente Python (`Video Bitrate Calculator.py`), assicurati di aver installato Python 3 con Tkinter e Pillow. Quindi apri un terminale o un prompt dei comandi, vai alla cartella in cui è salvato il file ed esegui:

```bash
python "Video Bitrate Calculator.py"
