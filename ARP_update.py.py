from scapy.all import ARP, Ether, srp, conf

conf.verb = 2  

target_ip = "192.168.65.134"  

arp_request = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp_request

print(f"Sending ARP request to {target_ip}...")
result = srp(packet, timeout=3, verbose=True)[0]  

if result:
    print("\n--- ARP Response ---")
    for sent, received in result:
        print(f"IP Address: {received.psrc} | MAC Address: {received.hwsrc}")
else:
    print("No response received. The target may be blocking ARP requests.")
