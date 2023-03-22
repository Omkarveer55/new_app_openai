import gradio as gr
import openai
from gtts import gTTS
import os

openai.api_key = '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'

message = 'you are the football advisor.'

print("gradio")
def transcribe(audio):
    audio_file= open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print('tenscript : ',transcript["text"])

    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                            {"role": "system", "content": message},
                            {"role": "user", "content": transcript["text"]},
                        ]
                                )
    audio = gTTS(text=response["choices"][0]["message"]["content"], lang="en", slow=False)
    audio.save("audio_files/example.mp3")
    os.system("start audio_files/example.mp3")
    return response["choices"][0]["message"]["content"]

demo = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone",type="filepath"), outputs="text").launch(share=True)

demo.launch(share=True)   