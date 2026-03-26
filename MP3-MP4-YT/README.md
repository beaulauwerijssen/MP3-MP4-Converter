# Python YT Downloader Pro

Een eenvoudige GUI-applicatie om YouTube-video's (of audio als MP3) te downloaden met `yt-dlp`.

## Stappen om te draaien

### 1) Vereisten installeren

```bash
python -m pip install -r requirements.txt
```

### 2) De app starten

```bash
python main.py
```

## Standalone Windows executable maken (optioneel)

Je kunt een zelfstandig uitvoerbaar bestand maken met [PyInstaller](https://pyinstaller.org/):

```bash
python -m pip install pyinstaller
python -m pyinstaller --onefile --windowed main.py
```

Het .exe-bestand komt dan te staan in `dist/main.exe`.

> ✅ Deze `.exe` bevat Python en alle Python-dependencies, dus de gebruiker hoeft zelf niets te installeren.

> ⚠️ Voor MP3-conversie is nog steeds `ffmpeg` nodig (aangeleverd via PATH of in dezelfde map als de `.exe`).
