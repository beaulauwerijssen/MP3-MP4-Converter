import tkinter as tk
from tkinter import messagebox
import os
import yt_dlp



def start_download(url_entry, format_var, status_label, root):
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Fout", "Plak eerst een SoundCloud link")
        return

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    selected_format = format_var.get()

    if selected_format == "MP3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
        mode_text = "MP3"
    else:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        })
        mode_text = "WAV"

    try:
        status_label.config(text=f"Bezig met {mode_text} downloaden...", fg="blue")
        root.update()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.config(text="Klaar!", fg="green")
        messagebox.showinfo("Succes", f"Bestand is succesvol opgeslagen als {mode_text}!")

    except Exception as e:
        messagebox.showerror("Fout", f"Er ging iets mis:\n\n{e}")
        status_label.config(text="Fout opgetreden.", fg="red")


def create_ui():
    root = tk.Tk()
    root.title("SoundCloud Downloader Pro")
    root.geometry("450x250")
    root.configure(padx=20, pady=20)

    tk.Label(root, text="SoundCloud URL:", font=("Arial", 10, "bold")).pack(anchor="w")
    url_entry = tk.Entry(root, width=60)
    url_entry.pack(pady=5)
    format_var = tk.StringVar(value="MP3")

    tk.Label(root, text="Audio formaat:", font=("Arial", 10, "bold")).pack(anchor="w")
    ttk = tk.Frame(root)
    ttk.pack(anchor="w")

    tk.Radiobutton(ttk, text="MP3", variable=format_var, value="MP3").pack(anchor="w")
    tk.Radiobutton(ttk, text="WAV", variable=format_var, value="WAV").pack(anchor="w")

    status_label = tk.Label(root, text="Wachten op link...", font=("Arial", 9, "italic"))
    status_label.pack()

    download_btn = tk.Button(
        root,
        text="START DOWNLOAD",
        command=lambda: start_download(url_entry, format_var, status_label, root),
        bg="#2ecc71",
        fg="white",
        font=("Arial", 11, "bold"),
        height=2,
    )
    download_btn.pack(fill="x", pady=10)

    return root


def main():
    root = create_ui()
    root.mainloop()


if __name__ == "__main__":
    main()