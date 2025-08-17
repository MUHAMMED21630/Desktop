yas = int(input("yaşınızı giriniz. "))
OkumaDurumu = input("okuyor musunuz? (evet: e, hayır:h)")

if yas >= 18 and OkumaDurumu == "h":
    print("Askere Gelme Yaşınız Geldi")

elif yas >= 18 and OkumaDurumu == "e":
    print("okulunuz bittiğinde askere geleceksiniz!")

else:
    print("askerlik yaşınız daha gelmedi")