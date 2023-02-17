import json

with open("sozluk.json", "r", encoding="utf-8") as f:
    hata_sozlugu = json.load(f)

while True:
    hata_adi = input("Lütfen aldığınız hatanın adını girin veya çıkmak için 'q' tuşuna basın: ")
    if hata_adi.lower() == 'q':
        break
    for hata, aciklama in hata_sozlugu.items():
        if hata.lower() == hata_adi.lower():
            print(aciklama)
            break
    else:
        print("Girdiğiniz hata adı geçersiz. Lütfen tekrar deneyin.")