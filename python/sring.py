# stringi tanımlarken şöyle tanımlamıyştık: öneğin:
# isim = "muhammed" veya isim = 'muhammed'
# bu şekilde tanımlamıştık.
# şimdi ise şöyle tanımlayacağız:
# isim = str("muhammed") veya isim = str('muhammed')

# örneğin: bir isimden mesela muhammed isminden herhangi bir harfi almak istersek:
# örneğin: "muh'a'mmed" isminden 'a' harfini almak istersek:
# isim = "muh'a'mmed"
# print(isim[3]) bu şekilde 3. indeksteki harfi alırız.

# not: eğer dışarıdaki tırnak işaretleri çift ise içerdeki tırnak işaretleri tek olmalı. örneğin "muh'a'mmed" ama eğer dışarıdaki tırnak işaretleri tek ise içerideki çift olmak zorunda.  

# stingdeki karakterleri almak isterseniz:
# karakterlerin sıralaması var bu sıralama şöyledir:

# örneğin: "muhammed" ismi
          # 0 1 2 3 4 5 6 7 
          # m u h a m m e d
          # eğer 0. indeksteki harfi almak istersek:
          # print(isim[0]) bu şekilde 0. ideksteki harfi alırız. yani m harfini alırız.
          # eğer 1. indeksteki harfi almak istersek:
          # print(isim[1]) bu şekilde 1. indeksteki harfi alırız. yani
        # u harfini alırız. 
# isim = input("MUHAMMED")

# print("isim"[0]) 
# print("isim"[1])
# print("isim"[2])
# print("isim"[3])
# print("isim"[4])
# print("isim"[5])
# print("isim"[6])
# print("isim"[7])
# sakın böyle yapmayın çünkü bu şekilde isim değişkenini tanımlamış olmuyoruz. eğer böyle yaparsak isim harfleri ayrı ayrı değil hepsi bir arada olur.

# print("MUHAMMED"[0]) 
# print("MUHAMMED"[1])
# print("MUHAMMED"[2])
# print("MUHAMMED"[3])
# print("MUHAMMED"[4])
# print("MUHAMMED"[5])
# print("MUHAMMED"[6])
# print("MUHAMMED"[7])
# doğru olan bu şekilde tanımlamaktır. yani isim değişkenini tanımlamadan harfleri ayrı ayrı alabiliriz.

# diyelim muhaömmed isminden 0 dan başlayarak 3e kadar olan harfleri almak istiyorum ama 3 dahil olmsın. o zaman şöyle yapablirim:
# örneğin: 
# print("muhammed"[0:3])
# bu şekilde 0. indeksten başlayarak 3. indekse kadar olan harfleri alırız ama 3. indeksi almaz. yani 0, 1, 2. indekste olan harfrleri alırız. yani muh harflerini alırız.
# eğer harfleri tersten almak istersek:
# örneğin: "muhammed" isminden d hafini almak istiyorrum o zaman şöyle yapmalıyım: 
# print("muhammed"[-1])
# peki 'd' harfini ve 3 harf daha almak istersem:
# isim = "muhammed"
#           m  u  h  a  m  m  e  d
#          -7 -6 -5 -4 -3 -2 -1  0 böyle sıralanır tersten.
# print("muhammed"[-4:-1])
# diylim uzun bir mektup yazdım ve bu metini olduğu gibi çıkarmak istiyorum. o zaman şöyle yapabilirim:
# mektup = """metin uzun bir mektup""" olduğu gibi çıkar.

# mektup = """ merhaba muhammed, nasılsın? umarım iyisindir."""

# print(mektup) bu şekilde mektubu olduğu gibi çıkarırız.