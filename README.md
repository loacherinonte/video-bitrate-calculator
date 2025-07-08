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
python3 VideoBitrateCalculator.py
