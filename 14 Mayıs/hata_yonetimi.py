try:
    sayi=int(input("Bir sayi girin:"))
    sonuc = 10 / sayi
except ZeroDivisionError:
    print("Sıfıra Bölünemez!")
except ValueError:
    print("Lütfen geçerli bir sayı giriniz!")
else:
    print(sonuc)
finally:
    print("Dosya kapatılıyor....")

yas = int(input("Yaşınızı Girin:"))
if yas < 0:
    raise ValueError("Yaş Negatif Olamaz!")
