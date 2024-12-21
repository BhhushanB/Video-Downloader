import sys
import os
import datetime
import yt_dlp
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QComboBox
)

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YT Video Downloader.. by Bhushan 😁")
        self.setGeometry(300, 300, 500, 300)

        # Main layout
        layout = QVBoxLayout()

        # URL Input Section
        self.label = QLabel("Link Khali Paste Kara 👇 (Paste kelya nantr 2 Min Wait kara 🤚.. Pani Piu shakta to pariyant 😁):")
        layout.addWidget(self.label)

        self.url_input = QLineEdit(self)
        layout.addWidget(self.url_input)

        # Format Selection (MP3 or MP4)
        self.format_label = QLabel("Tumhala Konta Format Pahije? 🎶📹:")
        layout.addWidget(self.format_label)

        self.format_combo = QComboBox()
        self.format_combo.addItems(["MP4 (Video)", "MP3 (Audio)"])  # Dropdown options
        layout.addWidget(self.format_combo)

        # Buttons (Download and Clear)
        button_layout = QHBoxLayout()

        self.download_button = QPushButton("Download", self)
        self.download_button.clicked.connect(self.download_video)
        button_layout.addWidget(self.download_button)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_input)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)

        # Contact Text
        self.contact_label = QLabel(
            "<b>If there is any query or problem, please contact us on: "
            "<a href='mailto:bhushan168504@gmail.com'>bhushan168504@gmail.com</a></b>"
        )
        self.contact_label.setOpenExternalLinks(True)
        layout.addWidget(self.contact_label)

        # Status Label (to show messages like 'Download Complete')
        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def download_video(self):
        url = self.url_input.text()
        selected_format = self.format_combo.currentText()  # Get selected format

        if url:
            try:
                # Get today's date for folder name
                today_date = datetime.datetime.now().strftime('%Y-%m-%d')

                # Get user's Downloads folder path
                download_path = os.path.join(os.path.expanduser('~'), 'Downloads', today_date)

                # Create the folder if it doesn't exist
                if not os.path.exists(download_path):
                    os.makedirs(download_path)

                # FFmpeg path
                ffmpeg_path = r'C:\PATH_Programs\ffmpeg.exe'

                # Set download options based on the selected format
                if "MP3" in selected_format:
                    ydl_opts = {
                        'outtmpl': os.path.join(download_path, '%(title)s.mp3'),
                        'format': 'bestaudio/best',  # Audio only
                        'ffmpeg_location': ffmpeg_path,
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        'noplaylist': True
                    }
                else:  # MP4 (default)
                    ydl_opts = {
                        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                        'format': 'bestvideo[height<=1080]+bestaudio/best',
                        'merge_output_format': 'mp4',
                        'ffmpeg_location': ffmpeg_path,
                        'noplaylist': True
                    }

                # Download the video/audio
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Success message
                self.status_label.setText(
                    f"Tumchi File '{today_date}' folder madhe Download zali aahe! 🤞 Check Kara 🎉."
                )
            except Exception as e:
                self.status_label.setText(f"❌ Error: {str(e)}")

    def clear_input(self):
        # Clear the URL input field and status message
        self.url_input.clear()
        self.status_label.setText("")
        self.format_combo.setCurrentIndex(0)  # Reset dropdown to default


# Run the application
app = QApplication(sys.argv)
window = YouTubeDownloader()
window.show()
sys.exit(app.exec_())
