def roma_to_int(roma):
    # Roma rakamlarının değer tablosu
    roma_rakam_degerleri = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    toplam = 0
    önceki_deger = 0
    
    for harf in reversed(roma):
        deger = roma_rakam_degerleri[harf]
        if deger < önceki_deger:
            toplam -= deger
        else:
            toplam += deger
        önceki_deger = deger
    
    return toplam

def roma_gecerli_mi(roma):
    # Geçerli Roma rakamları
    roma_rakamları = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    # Geçersiz karakterleri kontrol etmek
    for harf in roma:
        if harf not in roma_rakamları:
            return False

    # Ardışık aynı karakterlerin doğru miktarda kullanımını kontrol etmek 
    # Örneğin: 'IIII' veya 'VV' gibi geçersiz yazımları kontrol et
    geçersiz_kombinasyonlar = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
    for kombinasyon in geçersiz_kombinasyonlar:
        if kombinasyon in roma:
            return False

    # Çıkartma kurallarını kontrol et 
    hatalı_çıkartmalar = ['IL', 'IC', 'ID', 'IM',  # I yalnızca V ve X'ten çıkarılabilir
                          'VX', 'VL', 'VC', 'VD', 'VM',  # V hiçbir şeyden çıkarılamaz
                          'XD', 'XM',  # X yalnızca L ve C'den çıkarılabilir
                          'LC', 'LD', 'LM',  # L hiçbir şeyden çıkarılamaz
                          'DM']  # D yalnızca M'den çıkarılabilir
    for çıkartma in hatalı_çıkartmalar:
        if çıkartma in roma:
            return False

    return True

def main():
    print("Roma Rakamı Çevirici (1-4999)")
    print("-" * 30)
    while True:
        roma_rakamı = input("Roma rakamını girin (Çıkmak için 'q' yazın): ").upper()
        if roma_rakamı == 'Q':
            print("Programdan çıkılıyor.")
            break
        if roma_gecerli_mi(roma_rakamı):
            tamsayı = roma_to_int(roma_rakamı)
            if 1 <= tamsayı <= 4999:
                print(f"Girilen Roma rakamı '{roma_rakamı}', tamsayı olarak: {tamsayı}")
            else:
                print("Hatalı giriş: Lütfen 1 ile 4999 arasında bir Roma rakamı girin.")
        else:
            print("Geçersiz Roma rakamı! Lütfen doğru bir Roma rakamı girin.")

if __name__ == "__main__":
    main()
