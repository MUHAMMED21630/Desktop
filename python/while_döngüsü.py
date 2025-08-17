#  while döngüsü ne işe yarar?
#  diyelim 1 den 5 kadar sayı yazmak istiyorum kklasik olarak herkes bilir şunu yani 
# print("1")
# print ("2") 
# print ("3")
# print ("4")
# print("5")

# peki bu sayıyı 10bine çıkartmak istersek 10 bin satır mı yazacaz yoksa!
# hayır:) işte tamda böyle durumlarda while döngüsü devreye giriyor 
# nasıl mı? gelin bakalım:)

# şimdi bir değişken tamlayacam i adında örn olarak 1 den başlayamasını istediğim için 1 yazdım
# whlie yazdıktan sonra yanına bir durum yazmam gerekiyor yani bu durum karşısında bu döngünün içine girecek ben burda 5 e kadar yazdırmak istediğim için i <= (küçük eşittir)5 yazacam ama bunu yazıp bırakırsam sürekli 1 yazacak 
# bunun önüne geçmmek için i yi bir artıracam bunun yolu i = i + 1 yani i yi birle topla demek
# bide print yazdıktan sonra sakın parantezin içine tırnak işareti koymayın yoksa sayı değil harf yazılır:)
i = 1

while i <= 1200:
  print(i)

  i = i + 1