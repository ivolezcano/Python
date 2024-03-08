from pytube import YouTube
import pandas as pd
from pydrive.auth import GoogleAuth
from  pydrive.drive import GoogleDrive

file_path = 'enlaces_video/enlaces.xlsx'
sheet_name = 'Hoja 1'
column_name = 'videos'

# def subir_archivo ():
#     credenciales = login()
#     archivo = credenciales.CreateFile({})

def main ():
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    column_data = df[column_name]
    videos = column_data.values
    # print(videos)

    for link_video in videos:
        yt = YouTube(link_video)
        video = yt.streams.get_highest_resolution()
        video.download('./YT')
        # subir_archivo(f'YT/{video.title}.mp4', id_folder)

if __name__ == '__main__':
    main()