# Chatbots

from datetime import datetime
import random

now = datetime.now()
tanggal = now.strftime("%d")
bulan = now.strftime("%B")
tahun = now.strftime("%Y")

nama = "Najwa Syiba Hansyaf"
default = [
  "maaf, aku tidak tahu jawaban dari pertanyaan mu",
  "sepertinya aku harus banyak belajar"
]

# perlu pip3 install gTTS pyttsx3 playsound
# text to speech 
import gtts
from playsound import playsound
tts = gtts.gTTS("Hola Mundo", lang="es")
tts.save("hola.mp3")
playsound("hola.mp3")

# referensi https://www.thepythoncode.com/article/convert-text-to-speech-in-python


# list message
   
# Just Examples
# list jawaban untuk pertanyaan tentang nama
jawaban_nama = [
      "nama saya {0}".format(nama),
      "orang-orang memanggil saya {0}".format(nama),
      "panggil saja saya {0}".format(nama)
   ]

# Just Examples
# list jawaban untuk pertanyaan tentang tanggal
jawaban_tanggal = [
      "hari ini tanggal {0}".format(tanggal),
      "ya ampun masa tidak tahu, hari ini tanggal {0}".format(tanggal)
    ]

# list jawaban untuk pertanyaan tentang bulan
jawaban_bulan = [
      "sekarang bulan {0}".format(bulan),
      "hmm sekarang bulan {0} nih".format(bulan)
    ]

# list jawaban untuk pertanyaan tentang tahun
jawaban_tahun = [
      "sekarang tahun {0}".format(tahun),
      "wah udah tahun {0}".format(tahun)
    ]

# list jawaban untuk pertanyaan tentang kabar
jawaban_kabar = [
      "kabar saya baik",
      "not bad"
    ]


# Just Examples
# opsi pertanyaan yang bisa dijawab
pertanyaan = {
    "nama kamu siapa?": jawaban_nama,
    "kamu siapa?" : jawaban_nama,
    "tanggal berapa hari ini?": jawaban_tanggal,
    "hari ini tanggal berapa?" : jawaban_tanggal,
    "bulan apa sekarang?" : jawaban_bulan,
    "sekarang bulan apa?" : jawaban_bulan,
    "tahun berapa sekarang?" : jawaban_tahun,
    "sekarang tahun berapa?" : jawaban_tahun,
    "apa kabar?" : jawaban_kabar,
    "default": default
}

# Just Examples
# list jawaban untuk sebuah argument selain pertanyaan
statement =  [
    'ceritakan lebih banyak!',
    'kenapa kamu berpikir begitu?',
    'sudah berapa lama kamu merasa seperti ini?',
    'Itu sangat menarik!',
    'oh wow!',
    ':)'
]
   
# Just Examples tambahkan sesuai selera
# respon keseluruhan
responses = {
    'pertanyaan' : pertanyaan,
    'statement' : statement,
    # ...
}

# Task
# ----
# bot dapat membalas sapaan
# bot dapat memberikan informasi dirinya
# bot juga daapt menjawab beberapa informasi umum atau informasi yang anda inginkan
# bot menjawab dengan mencari pattern pada kalimat
# bot menjawab dengan kata yang tidak sama untuk setiap kalinya
# bot menjawab sesuai dengan senang atau tidak
# bot dapat menjawab dengan suara
# optional file suara setelah dipakai auto dihapus
# gunakan file ini sebagai module , buat file testing.py dan jalankan bot pada file testing.py
# bebas berkreasi :)
   
# Just Examples
def chatbot(message):
    respon1 = responses['pertanyaan']
    if 'siapa' in message:
      respon2 = random.choices(jawaban_nama)
      return (respon2)
    elif 'tanggal' in message:
      respon2 = random.choices(jawaban_tanggal)
      return (respon2)
    elif 'bulan' in message:
      respon2 = random.choices(jawaban_bulan)
      return (respon2)
    elif 'tahun' in message:
      respon2 = random.choices(jawaban_tahun)
      return (respon2)
    elif 'kabar' in message:
      respon2 = random.choices(jawaban_kabar)
      return (respon2)
    else:
      return respon1['default']

def main():
    print("Halo, selamat datang!  (type 'e' to exit)")
    while True:
      question = str(input("Mau tanya apa: "))
      if question == "e":
          print("-----------------------------------------", "\n")
          break
      answer = chatbot(question)
      print(answer)
      print("-----------------------------------------", "\n")

if __name__ == "__main__":
    main()