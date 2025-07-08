# 🎥 Video Bitrate Calculator

**Video Bitrate Calculator** is a simple and lightweight macOS app that helps you calculate the ideal video bitrate in **kilobits per second (kbps)** based on your **target file size** (in MB) and **video duration** (in minutes and seconds).

---

## ✏️ How the Bitrate is Calculated

The app uses the following formula:

Why:
- 1 MB = 1024 KB
- 1 KB = 8 kilobits
- Bitrate is measured in **kbps** (kilobits per second)

📌 Example:  
- File size: 50 MB  
- Duration: 10 minutes → 600 seconds  
- Calculation:  
  `(50 × 1024 × 8) / 600 = 683 kbps,`
  ` without audio (128 kbps) = 555 kbps`

---

## 💻 How to Use

1. Enter the **desired file size** in megabytes (MB)
2. Enter the **video duration** (in minutes and seconds)
3. Click the **Calculate** button
4. The app will show the required **bitrate** in kbps

---

## 📥 Download

You can download the macOS app here:

👉 [Download VideoBitrateCalculator.dmg](https://github.com/loacherinonte/Video-Bitrate-Calculator/releases/latest)

Once downloaded:
- Double-click the `.dmg`
- Drag the app into the **Applications** folder

---

## ⚙️ For Developers

### ▶️ Run the Python script

If you want to run the script manually:

```bash
python3 VideoBitrateCalculator.pyù

# 🎥 Video Bitrate Calculator

## 🇮🇹 Calcola il bitrate perfetto in base alla dimensione desiderata

Video Bitrate Calculator è un'app semplice e leggera per macOS che ti aiuta a calcolare il bitrate video ideale in **kilobit per secondo (kbps)** in base alla **dimensione del file desiderata (in MB)** e alla **durata del video (in minuti e secondi)**.

## ✏️ Formula usata
📌 1 MB = 1024 KB  
📌 1 KB = 8 kilobits  
📌 Bitrate is calculated in **kbps** (kilobits per second)

🧮 Esempio:
- File size: 50 MB  
- Duration: 10 minutes → 600 seconds  
- Bitrate = (50 × 1024 × 8) / 600 = **682.66 kbps**

---

## 📦 Requisiti / Requirements

- macOS 12+ (Apple Silicon o Intel)
- Python 3.11+ (solo per sviluppatori)

---

## 💻 Come si usa / How to use

### 🖱️ Interfaccia:
1. Inserisci la **dimensione desiderata** in MB.
2. Inserisci la **durata del video** (minuti e secondi).
3. Premi **Calcola** per ottenere il bitrate.

---

## 📥 Download

### 🇮🇹 Scarica l’app per macOS:  
👉 [Download VideoBitrateCalculator.dmg](https://github.com/loacherinonte/Video-Bitrate-Calculator/releases/latest)

Trascina l’app nella cartella **Applicazioni**.

## 🧑‍💻 Per sviluppatori

### ▶️ Avviare lo script direttamente:
```bash
python3 VideoBitrateCalculator.py
