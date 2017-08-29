while True:
    ilk_sayı=input("Bölme işlemi için ilk sayı (Çıkmak için q tuşuna basın): ")

    if ilk_sayı=="q":
        break

    ikinci_sayı=input("İkinci sayı: ")

    try:
        sayı1=int(ilk_sayı)
        sayı2=int(ikinci_sayı)
        print(sayı1,"/",sayı2,"=",sayı1/sayı2)
    except (ValueError,ZeroDivisionError):
        print("Hata!")
        print("Lütfen tekrar deneyin!")
