# mantıksal operatorler bizim koşulu ifadelerde birden çok durumu aynı anda kontrol etmemizi sağlıyor

ehliyet = False
araba = True

if ehliyet and araba:
    print("araba kullanabilirsin")

    # not eğer and değişkenini kulanmak istersen her iki side doğru yani true olması gerekiyor

elif ehliyet or araba:
    print("araba kullanmana çok az kaldı")

    # not bu komutun çalışa bilmesi için bir değişkenin false olması gerekiyor yani and de ikisi doğru olmak zorundaydı ama or da birisi bile doğru olsa çalışır aslında birisi false olmak zorunda :))

elif araba and not ehliyet:
    print("sörücü kursumuzu tercih ederek hemen  araba kullana bilirsiniz")

else:
    print("araba kullanmana daha çok var")

    # bu kodun yani else nin çalışması için iki değişkenin de false olmak zorunda

    # and
    # or 
    # not 