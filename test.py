def start_chat():
    print("Selamat datang! Mari kita bantu Anda memilih spesifikasi PC.")
    print("---------------------------------------------------------")
    tujuan = input("1. Apa tujuan utama penggunaan PC Anda? \n(Gaming/Produktivitas/Konten Kreasi/Umum): ").strip().lower()
    
    if tujuan == "gaming":
        genre = input("\n2. Genre game yang dimainkan? \n(eSports/Open World/Streaming/VR): ").strip().lower()
        budget = input("\n3. Budget Anda? \n(<10 juta/10-15 juta/>15 juta): ").strip().lower()
        resolusi = input("\n4. Resolusi monitor? \n(1080p/1440p/4K/Ultrawide): ").strip().lower()
        refresh_rate = input("\n5. Refresh rate monitor? \n(60Hz/120Hz/144Hz/240Hz): ").strip().lower()
        prioritas = input("\n6. Prioritas utama? \n(Performa/Harga/Kualitas Visual/Fitur): ").strip().lower()
        processor_brand = input("\n7. Processor brand pilihan? \n(Intel/AMD): ").strip().lower()
        motherboard = input("\n8. Chipset motherboard? \n(H610/B660/Z690/A520/B550/X570): ").strip().upper()
        storage = input("\n9. Tipe storage? \n(SSD 500GB/SSD 1TB/HDD + SSD): ").strip()
        ram = input("\n10. Kapasitas RAM? \n(8GB/16GB/32GB): ").strip()
        
        print("\n--- Rekomendasi PC Gaming Anda ---")
        print(f"Tujuan: {tujuan.capitalize()}")
        print(f"Genre Game: {genre.capitalize()}")
        print(f"Budget: {budget.capitalize()}")
        print(f"Resolusi Monitor: {resolusi.upper()}")
        print(f"Refresh Rate: {refresh_rate}")
        print(f"Prioritas Utama: {prioritas.capitalize()}")
        print(f"Processor: {processor_brand.capitalize()}")
        print(f"Chipset Motherboard: {motherboard}")
        print(f"Storage: {storage}")
        print(f"RAM: {ram}")

    elif tujuan == "produktifitas":
        pekerjaan = input("\n2. Jenis pekerjaan? \n(Programming/Office/Data Analysis/Design): ").strip().lower()
        budget = input("\n3. Budget Anda? \n(<10 juta/10-15 juta/>15 juta): ").strip().lower()
        storage = input("\n4. Tipe storage? \n(SSD 500GB/SSD 1TB/HDD + SSD): ").strip()
        ram = input("\n5. Kapasitas RAM? \n(8GB/16GB/32GB): ").strip()
        
        print("\n--- Rekomendasi PC Produktivitas Anda ---")
        print(f"Tujuan: {tujuan.capitalize()}")
        print(f"Jenis Pekerjaan: {pekerjaan.capitalize()}")
        print(f"Budget: {budget.capitalize()}")
        print(f"Storage: {storage}")
        print(f"RAM: {ram}")

    elif tujuan == "konten kreasi":
        konten = input("\n2. Jenis konten yang dibuat? \n(Video/Foto/Streaming): ").strip().lower()
        budget = input("\n3. Budget Anda? \n(<10 juta/10-15 juta/>15 juta): ").strip().lower()
        processor_brand = input("\n4. Processor brand pilihan? \n(Intel/AMD): ").strip().lower()
        gpu = input("\n5. GPU yang diinginkan? \n(Integrated/RTX Series/GTX Series): ").strip().upper()
        storage = input("\n6. Tipe storage? \n(SSD 500GB/SSD 1TB/HDD + SSD): ").strip()
        ram = input("\n7. Kapasitas RAM? \n(16GB/32GB/64GB): ").strip()
        
        print("\n--- Rekomendasi PC Konten Kreasi Anda ---")
        print(f"Tujuan: {tujuan.capitalize()}")
        print(f"Jenis Konten: {konten.capitalize()}")
        print(f"Budget: {budget.capitalize()}")
        print(f"Processor: {processor_brand.capitalize()}")
        print(f"GPU: {gpu}")
        print(f"Storage: {storage}")
        print(f"RAM: {ram}")

    elif tujuan == "umum":
        aktivitas = input("\n2. Aktivitas utama? \n(Browsing/Office/Multimedia): ").strip().lower()
        budget = input("\n3. Budget Anda? \n(<5 juta/5-10 juta/>10 juta): ").strip().lower()
        storage = input("\n4. Tipe storage? \n(SSD 256GB/SSD 500GB/HDD + SSD): ").strip()
        ram = input("\n5. Kapasitas RAM? \n(4GB/8GB/16GB): ").strip()
        
        print("\n--- Rekomendasi PC Umum Anda ---")
        print(f"Tujuan: {tujuan.capitalize()}")
        print(f"Aktivitas Utama: {aktivitas.capitalize()}")
        print(f"Budget: {budget.capitalize()}")
        print(f"Storage: {storage}")
        print(f"RAM: {ram}")

    else:
        print("\nPilihan tidak valid. Silakan mulai lagi.")
        start_chat()

# Menjalankan chatbot
start_chat()
