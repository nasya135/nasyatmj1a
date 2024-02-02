print("======================== BitterSweet Cafe =========================\n")
print("  Bitter                     Sweet                      Desert")
print("- Americano                - Chocolate                - Choco Lava")
print("- Mocha Espresso           - Oreo                     - Roti Bakar Sweet")
print("- Caramel                  - Green Tea                - Red Velvet cake")
print("- Latte                    - Choco Forest             - Tiramisu Cake")
print("- Hezelnut latte           - Susu Matcha              - Matcha Cake")
print("- Vanila Latte             - Teh Dolce                - Hazelnut Cheesecake\n")

def Bitter():
    print("1. Americano           (15)")
    print("2. Mocha Espresso      (23)")
    print("3. Caramel             (20)")
    print("4. Latte               (18)")
    print("5. Hezelnut latte      (22)")
    print("6. Vanila Latte        (22)\n") 

def Sweet():
    print("1. Chocolate            (22)")
    print("2. Oreo                 (20)")
    print("3. Green Tea            (17)")
    print("4. Susu Matcha          (20)")
    print("5. Teh Dolce            (20)\n")

def Desert():
    print("1. Choco Lava          (25)")
    print("2. Roti Bakar Sweet    (22)")
    print("3. Red Velvet cake     (20)")
    print("4. Tiramisu Cake       (20)")
    print("5. Matcha Cake         (20)")
    print("6. Hazelnut Cheesecake (20)\n")

def menu():
    print("1. Bitter")
    print("2. Sweet")
    print("3. Dessert")
    print("4. Keluar")

def pesanan_bitter():
    print("\nPilihan menu Bitter:")
    Bitter()
    menu = int(input("Masukkan pilihan menu :"))
    sugar = int(input("Masukkan pilihan sugar (1.Less Sugar / 2.Normal Sugar): "))
    suhu = int(input("Masukkan pilihan suhu (1.Hot / 2.Cold): "))
    
    if menu == 1:
        menu_text = "Americano (15)"
    elif menu == 2:
        menu_text = "Mocha Espresso (23)"
    elif menu == 3:
        menu_text = "Caramel (20)"
    elif menu == 4:
        menu_text = "Latte (18)"
    elif menu == 5:
        menu_text = "Hezelnut latte (22)"
    elif menu == 6:
        menu_text = "Vanila Latte (22)"

    if sugar == 1:
        sugar_text = "Less Sugar"
    else:
        sugar_text = "Normal Sugar"
    if suhu == 1:
        suhu_text = "Hot"
    else:
        suhu_text = "Cold"

    return sugar_text, suhu_text, menu_text

def pesanan_sweet():
    print("\nPilihan menu Sweet:")
    Sweet()
    menu = int(input("Masukkan pilihan menu :"))
    sugar = int(input("Masukkan pilihan sugar (1.Less Sugar / 2.Normal Sugar): "))
    suhu = int(input("Masukkan pilihan suhu (1.Hot / 2.Cold) : "))
    
    if menu == 1:
        menu_text = "Chocolate (22)"
    elif menu == 2:
        menu_text = "Oreo (20)"
    elif menu == 3:
        menu_text = "Green Tea (17)"
    elif menu == 4:
        menu_text = "Susu Matcha (20)"
    elif menu == 5:
        menu_text = "Teh Dolce (20)"
    
    if sugar == 1:
        sugar_text = "Less Sugar"
    else:
        sugar_text = "Normal Sugar"
    if suhu == 1:
        suhu_text = "Hot"
    else:
        suhu_text = "Cold"

    return sugar_text, suhu_text, menu_text

def pesanan_desert():
    print("\nPilihan menu Dessert:")
    Desert()
    menu = int(input("Masukkan Pilihan menu : "))
    
    if menu == 1:
        menu_text = "Choco Lava (25)"
    elif menu == 2:
        menu_text = "Roti Bakar Sweet (22)"
    elif menu == 3:
        menu_text = "Red Velvet Cake (20)"
    elif menu == 4:
        menu_text = "Tiramisu Cake (20)"
    elif menu == 5:
        menu_text = "Matcha Cake (20)"
    elif menu == 6:
        menu_text = "Hazelnut Cheesecake (20)"
    
    return "", "", menu_text


def main():
    all_orders = [] 

    while True:
        print("\nMenu:")
        menu()
        pilihan = int(input("Masukkan pilihan pesanan (1/2/3/4): "))
        
        if pilihan == 4:
            break
        elif pilihan == 1:
            sugar, suhu, pesanan_text = pesanan_bitter()
        elif pilihan == 2:
            sugar, suhu, pesanan_text = pesanan_sweet()
        elif pilihan == 3:
            sugar, suhu, pesanan_text = pesanan_desert()
        
        print("\nPesanan:")
        print(f"Menu: {pesanan_text}")
        print(f"Sugar: {sugar}")
        print(f"Suhu: {suhu}")

        jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))  
        all_orders.append((pesanan_text, sugar, suhu, jumlah_pesanan)) 

        if pilihan == 4:
            lanjut = input("Apakah ingin melanjutkan pembelian (iya/tidak)? ")
            if lanjut.lower() != 'iya':
                break

        nama_pemesan = (input("\nMasukan Nama Anda: "))
    print("\nRincian Pesanan:")
    total_harga_semua = 0

    for order in all_orders:
        pesanan_text, sugar, suhu, jumlah_pesanan = order
        harga_per_item = int(pesanan_text.split("(")[1][:-1]) 
        total_harga = jumlah_pesanan * harga_per_item
        pajak = total_harga * 0.05
        total_harga += pajak  
        total_harga_semua += total_harga
        print(f"\nNama pemesan: {nama_pemesan}")
        print(f"Pesanan: {pesanan_text}")
        print(f"Sugar: {sugar}")
        print(f"Suhu: {suhu}")
        print(f"Jumlah pesanan: {jumlah_pesanan}")
        print(f"Total harga sebelum pajak: {total_harga - pajak}")
        print(f"Penambahan biaya pajak 5%: {pajak}")
        print(f"Total harga setelah pajak: {total_harga}")

    print("\nTotal Harga Semua Pesanan: ", total_harga_semua)

    print("\nTerima kasih telah berbelanja di BitterSweet Cafe!")
    print("Silahkan berikan rincian pesanan ke kasir dan tunggu pesanan anda!\n")

if __name__ == "__main__":
    main()