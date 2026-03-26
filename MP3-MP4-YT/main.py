import tkinter as tk
from tkinter import messagebox, ttk
import yt_dlp
import os

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
        messagebox.showerror("Fout", f"\n\nFout: {e}")
        status_label.config(text="Fout opgetreden.", fg="red")



def create_ui():
    """Create and return the main Tk root with its widgets."""

    root = tk.Tk()
    root.title("Python YT Downloader Pro")
    root.geometry("450x250")
    root.configure(padx=20, pady=20)

    tk.Label(root, text="YouTube URL:", font=("Arial", 10, "bold")).pack(anchor="w")
    url_entry = tk.Entry(root, width=60)
    url_entry.pack(pady=5)

    mp3_var = tk.BooleanVar()
    check_mp3 = tk.Checkbutton(root, text="Alleen Audio (MP3) downloaden", variable=mp3_var)
    check_mp3.pack(pady=10, anchor="w")

    status_label = tk.Label(root, text="Wachten op link...", font=("Arial", 9, "italic"))
    status_label.pack()

    download_btn = tk.Button(
        root,
        text="START DOWNLOAD",
        command=lambda: start_download(url_entry, mp3_var, status_label, root),
        bg="#2ecc71",
        fg="white",
        font=("Arial", 11, "bold"),
        height=2,
    )
    download_btn.pack(fill="x", pady=10)

    return root


def main():
    """Entrypoint for the application."""

    root = create_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
