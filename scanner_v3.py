import time
import socket
import threading
from queue import Queue

acik_portlar = []
kilit = threading.Lock()
kuyruk = Queue()
thread_sayisi = 100
hedef_ip = ""

def port_tara(ip, port):
    """Belirtilen IP adresini ön tanımlı portlara göre tarar ve açık ise listeye ekler."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soket:
            soket.settimeout(1)
            port_yanit = soket.connect_ex((ip, port))
            if port_yanit == 0:
                print(f"{ip}:{port} status is: Open")
                time.sleep(1)
                with kilit:
                    acik_portlar.append(port)
                    #print(f"{ip}:{port} status: Open")
            else:
                print(f"{ip}:{port} status is: Closed {port_yanit}")
                #print(f"{ip}:{port} status: Closed")
            socket.close()
    except:
        pass

def get_ip(default_ip="127.0.0.1"):
    """Kullanıcıdan taranmasını istediği IP adresini alır."""
    cevap_ip = ""
    cevap_ip = input("Taramak istediğiniz IP adresini girin (Varsayılan için boş bırakın [127.0.0.1]): ")
    if cevap_ip == "":
        return default_ip
    else:
        return cevap_ip

def calisan_islem():
    """Kuyruktan port alıp tarama işlemi için port_tara() fonksiyona gönderir"""
    while 1==1:
        
        port = kuyruk.get()
        if port is None:
            break
        port_tara("127.0.0.1",port)
        kuyruk.task_done()

def main():
    print("## Port Tarama Aracı KoçSistem ##")
    print()

    hedef_ip = get_ip()
    hedef_portlar = range(1,64000)

    baslangic_zamani = time.time()

    for port in hedef_portlar:
        kuyruk.put(port)


    thread_listesi = []
    for _ in range(thread_sayisi):
        t = threading.Thread(target=calisan_islem)
        t.daemon = True
        t.start()
        thread_listesi.append(t)

    kuyruk.join()

    #Threadlere durma sinyali gönderiyoruz
    for _ in range(thread_sayisi):
        kuyruk.put(None)
    
    
    for t in thread_listesi:
        t.join()

    bitis_zamani = time.time()

    print()
    #for port in hedef_portlar:
    #    if port in acik_portlar:
    #        print(f"{hedef_ip}:{port} status is: Open")
    #    else:
    #        
    #        print(f"{hedef_ip}:{port} status is: Closed")
    print()
    print(f"{hedef_ip} tarama tamamlandı.")
    print(f"Açık Portlar: {acik_portlar}")
    print(f"Tarama süresi: {bitis_zamani - baslangic_zamani} saniye")

if __name__ == "__main__":
    main()


