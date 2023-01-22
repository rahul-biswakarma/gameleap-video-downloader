## Gameleap Video Downloader Script

This script allows you to download multiple videos in parallel using multi-threading. It takes an array of video links and download them. Here's how you can use it:

1. First, make sure you have the required modules installed: `requests`, `tqdm`, and `threading`. You can install these modules using `pip install requests tqdm threading`.

2. Download the script and save it in a local directory.

3. Open the script in a text editor and modify `video_id`, and `video_name` variables to match the URLs and names of the videos you want to download.

4. Run the script using python video_downloader.py. The script will create a "downloads" folder in the same directory as the script and save the downloaded videos in it.

5. The script also has a pause and resume feature. You can pause the download by calling the pause() method of the MultiThreadDownloader class, and resume the download by calling the resume() method.

##Converter Script

This script allows you to combine .webm and .mp4 files that have the same name into a single .mp4 file. Here's how you can use it:

1. Make sure you have ffmpeg installed on your system. You can install it by running `!pip install ffmpeg-python`

2. Download the script and save it in a local directory.

3. Run the script by providing the directory path where the files are located as an argument. For example, python converter.py path/to/directory.

4. The script will iterate over the files in the directory, check for corresponding .webm and .mp4 files with the same name and combine them into a single .mp4 file. The script will save the output files in the same directory as the input files.

5. The script will also return an array of output file names, so you can keep track of the newly created files.




