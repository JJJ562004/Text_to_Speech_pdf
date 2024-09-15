
import pyttsx3 as tts
import PyPDF2
from pyttsx3 import voice


def pdf_to_text(pdf_path, output_txt):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

    return text


custom_voice = voice.Voice(age=12, gender='female', id=3, languages=['en-US'])
pdf_path = 'icann2010_maxpool.pdf'
txt_file = 'icann2010_maxpool.txt'
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say(pdf_to_text(pdf_path, txt_file))

engine.runAndWait()

#===================API METHOD==================================
# import requests
# import webbrowser
#
# url = "https://api.play.ht/api/v2/tts"
#
# payload = {
#     "text": "Ngoc Tu an is a bitch of mine",
#     "voice": "s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json",
#     "output_format": "mp3",
#     "voice_engine": "PlayHT2.0"
# }
# headers = {
#     "AUTHORIZATION": "40b280441900487cb40651643d059943",
#     "X-USER-ID": "roEmQySSfSTRy5ehRVR3Y5LzGk53",
#     "accept": "text/event-stream",
#     "content-type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# output_text = response.text
# print(output_text)
# output_index_start = output_text.index("https://")
# output_index_stop = output_text.rindex(".mp3")
# output_url = output_text[output_index_start:output_index_stop+4]
# print(output_url)
# # output_link = output_text.find("url")
# webbrowser.open(output_url)