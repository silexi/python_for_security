import time
import socket
import threading

acik_portlar = []
kilit = threading.Lock()

def port_tara(ip, port):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)
        port_yanit = soket.connect_ex((ip, port))
        if port_yanit == 0:
            with kilit:
                acik_portlar.append(port)
                #print(f"{ip}:{port} status: Open")
        else:
            pass
            #print(f"{ip}:{port} status: Closed")
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
    hedef_portlar = range(1,64000)

    baslangic_zamani = time.time()

    thread_listesi = []
    for port in hedef_portlar:
        t = threading.Thread(target=port_tara, args=(hedef_ip,port,))
        thread_listesi.append(t)
        t.start()
    
    for t in thread_listesi:
        t.join()

    bitis_zamani = time.time()

    print()
    for port in hedef_portlar:
        if port in acik_portlar:
            print(f"{hedef_ip}:{port} status is: Open")
        else:
            
            print(f"{hedef_ip}:{port} status is: Closed")
    print()
    print(f"{hedef_ip} tarama tamamlandı.")
    print(f"Açık Portlar: {acik_portlar}")
    print(f"Tarama süresi: {bitis_zamani - baslangic_zamani} saniye")

if __name__ == "__main__":
    main()


