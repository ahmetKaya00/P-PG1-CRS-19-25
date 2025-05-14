with open("demo.txt","r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

with open("demo.txt","w",encoding="utf-8") as dosya:
    dosya.write("Selamlar\n")
    dosya.write("Nasılsınız\n")

with open("demo.txt","a",encoding="utf-8") as dosya:
    dosya.write("Acun Medya\n")
    dosya.write("Pyton Eğitimi\n")

isim = input("Adınızı Girin:")

with open("kullanici.txt","a",encoding="utf-8") as dosya:
    dosya.write(f"Merhaba, {isim}!")


