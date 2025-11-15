import whisper

def transcribe_audio(path_to_wav):
    model = whisper.load_model("small")   # small is a good tradeoff
    res = model.transcribe(path_to_wav)
    return res["text"]
