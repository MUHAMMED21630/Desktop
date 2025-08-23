# evet arkadaşlar bu proje biraz zor bu yüzden dikkatlice dinleyin çünkü birazdan kopleks bir proje olacak 
# bu proje şimdi ilk olarak benim kullanıcıdan almak istediğim iki tane değer var birincisi ilk sayısı ikincisi de ikinci sayısı bunun için ilk sayı ve 2 sayı adında 2 tane değişken oluşturacağım ve bu değişkenlerle kullanıcımdan iki tane sayıda alacağım bunun için 
# input fonksiyonu kullanacağım doğal olarak ilk sayıya girmesi için ilk sayıya giriniz yazıyorum 
# ikinci sayıda giremesi için aynı bunu kopyalayarak ikinci sayıya giriniz yazacağım ekranı şimdi
# kullanıcım iki tane sayıda girdi fakat burada bir sorun var input fonksiyonu bizim verimizi string olarak kaydediyor yani text gibi düşünebilirsiniz text olarak kaydediyor bunu benim integre dönüştürmem lazım ki bununla işlem yapabileyim bu yüzdenben bu aldığım değeri int fonksiyonu ile intergre dönüştöreceğim her ikisini de bunları interger a dönüştürdükten sonra sırada kullanıcının yapmak istediği işlemi öğrenmek var
# bunun için de işlem alanında bir değişiklik oluşturacağım ve kullanıcıya yapmak istediği işlemi soracağım fakat bu biraz uzun bir soru olacak hemen göstereyim  ne kadar uzun olduğunu
# ilk olarak kullanıcıya yapmak istediği işleme giriniz diye söyleyeceğim fakat burda kullanıcı hani nasıl girrecek yani toplama mı yazacak artıya mı basacak bunu belirtmek için de alt satıra geçip bir tane parantez açacağım ve bunun içine her işlemin simgesini yazacağım yani toplama yapmak istiyorsan artıya bas aynı şekilde çıkarma yapmak istyorsan  eksiye bas gibi bütün işlemleri böyle tanımlayacağım böylece kullanıcım tek bir karakterle yaptığı işleme belirtmiş olacak çarpma yapmak istiyorsan x bas 
#  ve son olarak 4 işlemm olacak bu hesap makinesi bölme yapmak istiyorsan da slash'a bas hemen bunu nasıl gözüktüğünü göstermek istiyorum ilk sayım 8 ikinci sayım 4 burada şimdi kullanıcıma diyor ki
# bakın fark ettiyseniz 3 tırnak koyduğum için aynı şekilde yapıştırdı buraya yani noktasından virgülüne satır başına kadar şimdi burda bana dior ki 
# toplama yapmak istiyorsan artıya bas böyle böyle çıkarma yapmak istiyorsan eksiye bas burada da 
# kullanıcıya artıya basacak eksiye mi basacak falan böyle basttıktan sonra  enter'a basacak ve böylece 
# hangi işlemi yapmak istediğini öğrenmiş oldm sırada bu iki sayıyı o işlemi yaptırmak var bunun için if durumunu kullanacağım eğer kullanıcı işlemi toplama girdiyse yani eşit eşit artıya denk geliyor bu kodlamada eğer kullanıcı toplama yapmak isrtiyorsa ben bu iki sayıyı toplayacağım yani sayı 1 ile daha doğrusu ilk sayıyla ikinci sayıyı toplayacağıım fakat burda sadece ekrana direkt sonucu yazdırmak istemiyorum aynı zamanda bunların başına hani daha güzel gözüksün diye sonuç iki noktaya yazdıracağım fakat burada bildiğiniz üzere sitringleri birleştirmek İçin araya bir artı koymamız gerekiyor ve bu ikisi string değil tamam bu string ama bu şu an  integer hatırlarsanız bunu da benim stringe dönüştürmem gerekiyor bunun için de str komutunu kullanacağım ve böylece bu iki sayı toplandıktan sonra stringe dönüşecek vve bundan sonra bu iki stringi isstediğin gibi birleştirmiş olacak aynen böyle şimdi sırada aynı şeyleri diğer işlemler için yapmak var bunlar için elif durumunu kullanacağım eğer kullanıcı çıkarma yaapmak istiyorsa bu sefer aynı bunu kullanacağım aslında aynı şeyi yazacağım bunun için direkt kopyalıyorum fakat bu sefer çıkarma yapacak bu ikisinin arasında yani eksi kullanacağım sonra kullanıcı çarpma yapmak istiyorsa yani işleme x'e basısa bu sefer de bu iki sayıyı çarpacağım ve son olarak 4 işlemimiz kullanıcım eğer bölme yapmak istiyorsa bu sefer de bu iki sayıyı böleceğim kodum bu kadar zaten çok açıklayıcı bir kod oldu bence hemen deneyerek göstermek istiyorum .

ilksayı = int(input("ilk sayıyı giriniz:"))
ikincisayı = int(input("ikinci sayıyı giriniz: "))
islem = input("""yapmak istediğiniz işlemi giriniz: 
(toplama: +, çıkarma: -, çarpma: x, bölme:  /)""")

if islem == "+":
    print("sonuç: "+str(ilksayı+ikincisayı))

elif islem == "-":
    print("sonuç: " + str(ilksayı-ikincisayı))

elif islem == "x":
    print("sonuç: " + str    (ilksayı * ikincisayı))

elif islem == "/":
    print("sonuç: " + str(ilksayı / ikincisayı))

# işte hepsi bu kadardı 