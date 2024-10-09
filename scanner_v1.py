import time
import socket

acik_portlar = []

def port_tara(ip, port):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)
        port_yanit = soket.connect_ex((ip, port))
        if port_yanit == 0:
            acik_portlar.append(port)
            print(f"{ip}:{port} status: Open")
        else:
            print(f"{ip}:{port} status: Closed")
        socket.close()
    except:
        pass

def get_ip():
    hedef_ip = ""
    cevap_ip = ""
    cevap_ip = input("Taramak istediğiniz IP adresini girin (Varsayılan için boş bırakın [127.0.0.1]): ")
    if cevap_ip == "":
        return "127.0.0.1"
    else:
        return cevap_ip

def main():
    print("## Port Tarama Aracı KoçSistem ##")
    print()

    hedef_ip = get_ip()
    hedef_portlar = range(0,81)

    #print(hedef_ip,hedef_portlar,sep=":")

    baslangic_zamani = time.time()

    for port in hedef_portlar:
        port_tara(hedef_ip,port)
    
    bitis_zamani = time.time()

    print()
    print(f"Tarama tamamlandı.")
    print(f"Açık Portlar: {acik_portlar}")
    print(f"Tarama süresi: {bitis_zamani - baslangic_zamani} saniye")



if __name__ == "__main__":
    main()




# hedef_port = ""
# cevap_port = ""
# cevap_port = input("Taramak istediğiniz portu girin (Varsayılan için boş bırakın [80]): ")
# if cevap_port == "":
#     hedef_port = "80"
# else:
#     hedef_port = cevap_port


# for ad in ["bartu","can bartu","ergün","birol"]:
#     if ad == "cem":
#         print(f"Kullanıcı bulundu: {ad}")
#         break
#     else:
#         print(f"Kullanıcı bulunamadı: {ad}")

# for item in [1,7,3,4,5]:
#     print(item)
