from pytube import YouTube

def descargar_video_youtube(url, path):
    try:
        # Crear objeto YouTube
        yt = YouTube(url)
        
        #obtener elvideo de mayor resolución
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        # Descargar el video
        stream.download(output_path=path)
        
        print(f'Video descargado: {yt.title}')
    except Exception as e:
        print(f'Error al descargar el video: {e}')

# Ejemplo de uso
url = "https://www.youtube.com/watch?v=XFkzRNyygfk"  
path = "./videos"  #carpeta
descargar_video_youtube(url, path)
