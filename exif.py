from PIL import Image
from PIL.ExifTags import TAGS
import os

print("""     ______________________________________________________________________
    / ____/\ \  / /    /_  _/  / ___/ /__  ___/ / ____  /  / ____  /  /  / 
   / /___   \ \/ /      / /   / /__     / /    / /   / /  / /   / /  /  /
  / ____/   / /\ \     / /   / ___/    / /    / /   / /  / /   / /  /  /
 / /___    / /  \ \  _/ /_  / /       / /    / /___/ /  / /___/ /  /  /____
/_____/    \/    \/ /____/ /_/       /_/    /_______/  /_______/  /_______/ 
                                                                ~ismailkucuk """)
print("Hoşgeldiniz // Welcome \n");
while True:
    try:
        secim = int(input("""Türkçe için 1'e basınız.
Press 2 for English.\n"""));


        if secim == 1:
            def extract_and_create_google_maps_link(image_path):
                try:
                    # Resmi aç
                    img = Image.open(image_path)

                    # EXIF verilerini al
                    exif_data = img._getexif()

                    if exif_data is not None:
                        # GPS verilerini çıkart
                        gps_info = exif_data.get(34853, "Bilgi yok")  # 34853, GPS etiketinin numarasıdır

                        if gps_info != "Bilgi yok":
                            # Google Maps URL'sini oluştur
                            latitude = convert_decimal_degrees(float(gps_info[2][0]), float(gps_info[2][1]),
                                                               float(gps_info[2][2]),
                                                               gps_info[1])
                            longitude = convert_decimal_degrees(float(gps_info[4][0]), float(gps_info[4][1]),
                                                                float(gps_info[4][2]),
                                                                gps_info[3])
                            google_maps_url = f"https://maps.google.com/?q={latitude},{longitude}"

                            # EXIF bilgilerini ve Google Maps URL'sini .txt dosyasına kaydet
                            save_to_txt(image_path, exif_data, google_maps_url)
                        else:
                            print("Bu resmin GPS verisi yok.")
                    else:
                        print("Bu resmin EXIF verisi yok.")
                except Exception as e:
                    print(f"Hata: {e}")


            def save_to_txt(image_path, exif_data, google_maps_url):
                try:
                    # Dosya adını ve dizinini al
                    dosya_adı = f"exif_bilgileri_{os.path.basename(image_path)}.txt"
                    dizin = os.path.dirname(image_path)

                    # EXIF ve Google Maps URL bilgilerini yazma
                    with open(os.path.join(dizin, dosya_adı), "w") as file:
                        file.write("EXIF Bilgileri:\n")
                        for tag, value in exif_data.items():
                            tag_name = TAGS.get(tag, tag)
                            file.write(f"{tag_name}: {value}\n")

                        file.write("\nGoogle Maps URL'si:\n")
                        file.write(f"{google_maps_url}\n")

                    print(f"EXIF bilgileri ve Google Maps URL'i '{dosya_adı}' isimli dosyaya, {dizin} dizinine kaydedildi.")
                except Exception as e:
                    print(f"Hata: {e}")

            def convert_decimal_degrees(degree, minutes, seconds, direction):
                decimal_degrees = degree + minutes / 60 + seconds / 3600
                if direction == "S" or direction == "W":
                    decimal_degrees *= -1
                return decimal_degrees


            resim_yolu = input("Dosya dizinini giriniz: ")

            extract_and_create_google_maps_link(resim_yolu)

            input("Çıkmak için Enter'a basınız...")
            break

        elif secim == 2:
            def extract_and_create_google_maps_link(image_path):
                try:
                    # Open picture
                    img = Image.open(image_path)

                    # Get EXIF data
                    exif_data = img._getexif()

                    if exif_data is not None:
                        # Extract GPS data
                        gps_info = exif_data.get(34853, "No information")  # 34853 is the number of the GPS tag

                        if gps_info != "No information":
                            # Generate Google Maps URL
                            latitude = convert_decimal_degrees(float(gps_info[2][0]), float(gps_info[2][1]),
                                                               float(gps_info[2][2]),
                                                               gps_info[1])
                            longitude = convert_decimal_degrees(float(gps_info[4][0]), float(gps_info[4][1]),
                                                                float(gps_info[4][2]),
                                                                gps_info[3])
                            google_maps_url = f"https://maps.google.com/?q={latitude},{longitude}"

                            # Save EXIF information and Google Maps URL in a .txt file
                            save_to_txt(image_path, exif_data, google_maps_url)
                        else:
                            print("This picture has no GPS data.")
                    else:
                        print("This image has no EXIF data.")
                except Exception as e:
                    print(f"Error: {e}")


            def save_to_txt(image_path, exif_data, google_maps_url):
                try:
                    # Get file name and directory
                    dosya_adı = f"exif_information_{os.path.basename(image_path)}.txt"
                    dizin = os.path.dirname(image_path)

                    # Writing EXIF and Google Maps URL information
                    with open(os.path.join(dizin, dosya_adı), "w") as file:
                        file.write("EXIF Information:\n")
                        for tag, value in exif_data.items():
                            tag_name = TAGS.get(tag, tag)
                            file.write(f"{tag_name}: {value}\n")

                        file.write("\nGoogle Maps URL:\n")
                        file.write(f"{google_maps_url}\n")

                    print(f"EXIF information and Google Maps URL were saved in a file named '{dosya_adı}' in the directory {dizin}.")
                except Exception as e:
                    print(f"Error: {e}")

            def convert_decimal_degrees(degree, minutes, seconds, direction):
                decimal_degrees = degree + minutes / 60 + seconds / 3600
                if direction == "S" or direction == "W":
                    decimal_degrees *= -1
                return decimal_degrees


            resim_yolu = input("Enter the file directory: ")

            extract_and_create_google_maps_link(resim_yolu)

            input("Press Enter to exit...");
            break

        else:
            print("Eksik veya hatalı giriş yaptınız. // You have made an incomplete or incorrect entry.\n")

    except ValueError:
        print("Eksik veya hatalı giriş yaptınız. // You have made an incomplete or incorrect entry.\n");