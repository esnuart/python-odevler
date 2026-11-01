print("--- 1. BÖLÜM: Ad, Soyad ve Şehir ---")
ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
sehir = input("Yaşadığınız şehri giriniz: ")
print(f"Merhaba, benim adım {ad} {soyad} ve {sehir}'de yaşıyorum.\n")


print("--- 2. BÖLÜM: İndirim Hesaplama ---")
fiyatsiz_tutar = float(input("Ürünün etiket fiyatını giriniz: "))
indirim_yuzdesi = float(input("İndirim yüzdesini giriniz (Örn: 20): "))
indirim_tutari = fiyatsiz_tutar * (indirim_yuzdesi / 100)
son_fiyat = fiyatsiz_tutar - indirim_tutari
print(f"İndirim Tutarı: {indirim_tutari:.2f} TL, İndirimli Fiyat: {son_fiyat:.2f} TL\n")


print("--- 3. BÖLÜM: Yaş ve Ehliyet Durumu ---")
dogum_yili = int(input("Doğum yılınızı giriniz: "))
dogum_ayi = int(input("Doğum ayınızı giriniz (Sayı olarak, örn: 12): "))

mevcut_yil = 2026
mevcut_ayi = 11  # Kasım ayı

yas = mevcut_yil - dogum_yili
if dogum_ayi > mevcut_ayi:
    yas -= 1

print(f"Yaşınız: {yas}")
if yas >= 18:
    print("Ehliyet alabilirsiniz.\n")
else:
    print("Ehliyet alamazsınız, henüz 18 yaşından küçüksünüz.\n")


print("--- 4. BÖLÜM: Vize-Final ve Harf Notu ---")
vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.40) + (final * 0.60)

if ortalama >= 85:
    harf = "AA"
elif ortalama >= 70:
    harf = "BA"
elif ortalama >= 60:
    harf = "BB"
elif ortalama >= 50:
    harf = "CB"
else:
    harf = "FF"

print(f"Dönem Ortalamanız: {ortalama:.2f} - Harf Notunuz: {harf}")

input("\nÇıkmak için Enter tuşuna basınız...")
