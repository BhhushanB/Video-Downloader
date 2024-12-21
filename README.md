# YouTube Video Downloader with PyQt5

Welcome to the **YouTube Video Downloader**! This tool allows users to download YouTube videos and audio in their desired format (MP4/MP3) directly from their desktop. It features a user-friendly GUI built with PyQt5 and supports downloading videos in high quality.

---

## Features
- 🎥 Download videos in MP4 format (up to 1080p quality).
- 🎵 Download audio in MP3 format.
- 📅 Automatically saves downloads in the `Downloads` folder with a subfolder named after the current date.
- 🛠️ No need to manually install FFmpeg (included with the app).
- 📧 Contact option for troubleshooting directly from the GUI.

---

## Requirements
This application was developed with:
- **Python 3.9+**
- **PyQt5**
- **yt-dlp**
- **FFmpeg**

However, if you are using the provided `.exe` file, you don't need to install Python or any libraries. 

---

## How to Use
### Using the Executable File:
1. Download the `YouTubeDownloader.zip` file from the repository.
2. Extract the ZIP file into a folder. ([how to install]([url](https://sites.google.com/view/skillcoursehelp/yt-videos-downloader?authuser=0)3. ))
4. Double-click on `YouTubeDownloader.exe` to launch the application.
5. Paste the YouTube video link in the text box.
6. Select the desired format (MP4 or MP3) from the dropdown.
7. Click on **Download** and wait for the animation to finish.
8. Your file will be saved in the `Downloads` folder in a new subfolder with the current date.

### For Developers:
To run the Python script, ensure you have the following installed:
1. Python 3.9 or higher.
2. Install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python youtube_downloader.py
   ```

---

## File Structure
```
📁 YouTubeDownloader
    ├── YouTubeDownloader.exe       # Executable file (ready to use)
    ├── ffmpeg.exe                  # FFmpeg binary for video processing
    ├── youtube_downloader.py       # Python source code
    ├── requirements.txt            # Python dependencies
    └── README.md                   # This file
```

---

## Built With
- **[PyQt5](https://riverbankcomputing.com/software/pyqt/intro)**: For the graphical user interface.
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: For downloading videos and audio.
- **[FFmpeg](https://ffmpeg.org/)**: For merging video and audio seamlessly.

---

## Screenshots
### Main Interface:
![Main Interface](https://via.placeholder.com/500x300.png?text=Screenshot+Placeholder)

---

## Known Issues
- Antivirus software may flag the `.exe` file as potentially unsafe. This is a false positive due to the packaging process.
- Ensure you have enough disk space in the `Downloads` folder for high-quality video downloads.

---

## Contributing
If you find any bugs or have feature requests, feel free to create an issue or submit a pull request. Contributions are welcome!

---

## Contact
If you encounter any problems or have queries, please reach out at:
**[bhushan168504@gmail.com](mailto:bhushan168504@gmail.com)**

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

Enjoy downloading your favorite YouTube videos hassle-free! 😊
