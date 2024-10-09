# Değişkenler ve veri tipleri
print("## Değişkenler ve Veri Tipleri ##")

username = "hacker123"
age = 25 # integer
is_admin = False
password = "Password!"
password_strength = 8.5

#print(username)
#print("Kullanici adi: ", username)
#print("Admin mi?", is_admin, "ve parola gücü:",password_strength )

print(f"Kullanici adi: {username} ve {age} yaşında.")
print("Kullanici adi: {username} ve {age} yaşında.")

print()

print("## Listeler ##")
zafiyetli_portlar = [21,80,443,3306]
zafiyetli_portlar.append(8000)


print(f"Zafiyetli Portlar: {zafiyetli_portlar}")

#print("1. değer: ", zafiyetli_portlar[5])

print()

print("## Sözlükler ##")
server_info = {
    "ip": "192.168.1.55",
    "os": "Linux",
    "open_ports": [22,80,443],
    "owner": "Berkay İpek"
}


print("IP:", server_info["ip"])
print("İşletim Sistemi:", server_info["os"])
print("Açık Portlar:", server_info["open_ports"])
print("Sorumlu:", server_info["owner"])

print()

print("## Kontrol Yapıları if-elif-else ##")

port1= 80
port2= 443

if port2 < port1:
    print(f"Port {port2}, {port1}'den küçüktür.")
else:
    print(f"Port {port2}, {port1}'den küçük değildir.")

print()

#port_user = int(input())

# if port_user in zafiyetli_portlar:
#     print(f"{port_user} zafiyetli_portlar listesinin içerisindedir.")
#     print(zafiyetli_portlar)
# else:
#     print(f"{port_user} zafiyetli_portlar listesinin içerisinde değildir.")
#     print(zafiyetli_portlar)

maksimum_deneme = 5
deneme_sirasi = 0
while maksimum_deneme != deneme_sirasi:

    tuttugum_sayi= 7
    print(f"Hakkınız: {maksimum_deneme - deneme_sirasi}")
    tahmin_kullanici = int(input("Bir sayı tuttum tahmin et:"))
    user_response = ""
    if tahmin_kullanici >= 10 or tahmin_kullanici < 5:
        print("5 ile 10 arasında bir değer seçin. (10 hariç)")
    else:
        if tahmin_kullanici == tuttugum_sayi:
            print("Bildiniz")
            break
        else:
            print("Bilemediniz.")
            print(f"Kalan hakkınız: {maksimum_deneme - deneme_sirasi}")
            deneme_sirasi = deneme_sirasi + 1
            user_response = input("Devam etmek istiyor musunuz (e/h):")

    if user_response != "":
        if(user_response == "e"):
            pass
        elif (user_response == "h"):
            print("Pes ettiniz.")
            break
        else:
            print("Hatalı yanıt verdiniz. Program sonlanıyor.")
            break
        user_response = ""
    elif user_response == "":
        pass

print("Bitti.")


#print(type(zafiyetli_portlar))


#print(type(is_admin))
#print(username)
#print(type(username))