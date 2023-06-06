import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        status_label.config(text="Téléchargement réussi!")
    except Exception as e:
        status_label.config(text="Erreur lors du téléchargement.")

# Créer une fenêtre
window = tk.Tk()
window.title("Video Downloader")

# Créer une étiquette pour le champ URL
url_label = tk.Label(window, text="URL de la vidéo:")
url_label.pack()

# Créer un champ de saisie pour l'URL
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Créer un bouton de téléchargement
download_button = tk.Button(window, text="Télécharger", command=download_video)
download_button.pack()

# Créer une étiquette pour le statut du téléchargement
status_label = tk.Label(window, text="")
status_label.pack()

# Lancer la boucle principale
window.mainloop()
