# koşular bazı eylemler yapmamızı sağlıyor

# if değişkeni koşulu ifadelerde kullanılır ingilizce türkçe karşıtı eğer ilk ona bakılır


yagmurlu = False
guneşli = True


if yagmurlu:
   print("ceketini giy")

# eğer false koysaydım olmiyacaktı
# ama eğer başka bir değişken eklersem hata vermez

elif guneşli:
   print("gözlüğünü yanına al")

# bunun gibi elif nerden geliyo elif else if in kısaltması ingizcede elif türkçede aksi taktirde anlamı taşır.
# ikisinide if yapıp yağmurlu ve güneşliyide true yapsaydım ikisinide verecekti.
# yani birincisi olmuuyorsa öbürünü kontrol et diyecek yani if olmasa elif i koontrol edecek sistem.
# sistem birincisini kontrol edecek doğruysa yani true ise duracak değise diğerine geçecek yani if e bakacak true ise duracak değilse elif'e geçecek.


else:
   print("normal bir şekilde dışarı çık")

# peki bunların hiç biri değilse yani yağmurlu veya güneşli false olursa ne yapmalıyım işte tamda burda else deveye giriyor yani şöyle sistem kontrol edecek if e eğer doğruysa(true) duracak ama eğer yanlışsa(false) 2 incisine geçecek o true ise duracak ama oda false ise işte o zaman da 3 üncü yani son basamak kontrol edilecek else nin çalışması için her iki değişkeninde false olması lazım.