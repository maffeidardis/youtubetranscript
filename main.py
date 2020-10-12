from pytube import YouTube
import speech_recognition as sr
import moviepy.editor as mp

class TranscriptFromYoutube:

    #Creating a constructor
    def __init__(self, url, video_name):
        self.url = url
        self.video_name = video_name

    #Downloading the youtube video with mp4 extension
    def download(self):
        video = YouTube(self.url)
        video.streams.filter(file_extension='mp4').all()
        video.streams.get_by_itag(18).download()

    #Converting the .mp4 file to .wav, recognizing the speech and saving the transcription into a transcript.txt
    def convert_and_save(self):
        clip = mp.VideoFileClip(fr'{self.video_name}.mp4')
        clip.audio.write_audiofile(fr'{self.video_name}.wav')
        r = sr.Recognizer()
        audio = sr.AudioFile(fr'{self.video_name}.wav')

        with audio as source:
            audio_file = r.record(source)
        result = r.recognize_google(audio_file)

        with open('transcript.txt', mode='w') as file:
            file.write(f"{result}")
            return