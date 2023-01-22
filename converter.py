import os
import subprocess

def combine_files(dir_path):
    video_folder = os.path.join(dir_path, "../" , "videos")
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    files = os.listdir(dir_path)
    mp4_files = [f for f in files if f.endswith(".mp4")]
    webm_files = [f for f in files if f.endswith(".webm")]
    output_files = []
    for webm_file in webm_files:
        mp4_file = webm_file.replace(".webm", ".mp4")
        if mp4_file in mp4_files:
            output_file = webm_file.replace(".webm", "_combined.mp4")
            mp4_path = os.path.join(dir_path, mp4_file)
            webm_path = os.path.join(dir_path, webm_file)
            output_path = os.path.join(dir_path, output_file)
            command = "ffmpeg -i {} -i {} -c copy -map 0:v -map 1:a {}".format(webm_path, mp4_path, output_path)
            subprocess.run(command, shell=True)
            output_files.append(output_file)
    return output_files

if __name__ == "__main__":
    dir_path = "./downloads"
    output_files = combine_files(dir_path)
    print(output_files)
