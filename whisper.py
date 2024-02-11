# prompt: install whisper ai model
# !pip install git+https://github.com/openai/whisper.git

import whisper
import gc
import torch
import tkinter as tk
from tkinter import filedialog

gc.collect()
torch.cuda.empty_cache()
model = whisper.load_model("medium")


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
file_name = file_path.split("/")[-1]

file_name = '240207_1359_10449'
result = model.transcribe("/content/drive/MyDrive/voice_record/file_name")
print(result["text"])

def save_text_to_file(text, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)

# result 딕셔너리에서 "text" 키의 값을 가져옵니다.
text_value = result["text"]

# 텍스트를 저장할 파일 경로를 지정합니다. 필요에 따라 경로와 파일 이름을 수정하세요.
filepath = f"/content/drive/MyDrive/voice_record/txt/{file_name[:-4]}.txt"

# 텍스트를 파일로 저장합니다.
save_text_to_file(text_value, filepath)

print(f"텍스트가 '{filepath}' 파일에 저장되었습니다.")

