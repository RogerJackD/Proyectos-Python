from pytube import YouTube
import os

def descargar_audio_youtube(url, path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        if audio_stream:
            audio_stream.download(output_path=path)
            # Renombrar el archivo descargado con extensión mp3
            file_name = os.path.join(path, audio_stream.default_filename)
            os.rename(file_name, f"{os.path.splitext(file_name)[0]}.mp3")
            print(f'Audio descargado: {yt.title}')
        else:
            print('No se encontró una fuente de audio disponible.')
    except Exception as e:
        print(f'Error al descargar el audio: {e}')

# Ejemplo de uso
url = "https://www.youtube.com/watch?v=ID_DEL_VIDEO"
path = "./audios"  # Carpeta donde se guardará el audio
descargar_audio_youtube(url, path)
