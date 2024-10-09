import time
import socket
import threading
from queue import Queue
import ipaddress

#192.168.1.114
baslangic_ip = "192.168.1.110"
bitis_ip = "192.168.1.120"
port_araligi = range(80,140)
thread_sayisi = 100

acik_portlar = {}
kilit = threading.Lock()
kuyruk = Queue()

def port_tara(ip, port):
    """Belirtilen IP adresini ön tanımlı portlara göre tarar ve açık ise listeye ekler."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soket:
            soket.settimeout(1)
            port_yanit = soket.connect_ex((str(ip), port))
            if port_yanit == 0:
                with kilit:
                    if ip not in acik_portlar:
                        acik_portlar[ip] = []
                    acik_portlar[ip].append(port)
                    print(f"IP: {ip}, Port: {port} open")
            else:
                pass
    except Exception as e:
        print(e)
        


def calisan_islem():
    """Kuyruktan port alıp tarama işlemi için port_tara() fonksiyona gönderir"""
    while 1==1:
        
        ip_port = kuyruk.get()
        if ip_port is None:
            break
        ip, port = ip_port
        port_tara(ip,port)
        kuyruk.task_done()

def main():
    print("## Port Tarama Aracı KoçSistem ##")
    print()

    #hedef_ip = get_ip()

    baslangic_zamani = time.time()


    ip_araligi = ipaddress.summarize_address_range(
        ipaddress.ip_address(baslangic_ip),
        ipaddress.ip_address(bitis_ip)
        )

    for ip_network in ip_araligi:
        for ip in ip_network:
            for port in port_araligi:
                kuyruk.put((ip, port))



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
    print(f"Tarama tamamlandı.")
    for ip, portlar in acik_portlar.items():
        print(f"{ip}, Açık portlar: {sorted(portlar)}")
    gecen_sure = bitis_zamani - baslangic_zamani
    print(f"Tarama süresi: {gecen_sure:.2f} saniye")

if __name__ == "__main__":
    main()


