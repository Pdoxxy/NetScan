from network_scanner import NmapScanner 
from device_manager import DeviceManager
from notifier import Notifier

if __name__ == "__main__":
    scanner = NmapScanner()  
    device_manager = DeviceManager()
    results = scanner.scan_network()

    print("\n📋 Skanningsresultat:")
    for ip, (status, hostname) in results.items():  # Nu hanterar vi tuple (status, hostname)
        # Hämta namn från DeviceManager om det finns
        user_defined_name = device_manager.get_device_name(ip)
        
        # Kombinera båda namnen om båda finns
        if hostname != "Okänd enhet" and user_defined_name != f"Okänd enhet ({ip})":
            device_name = f"{user_defined_name} (hostname: {hostname})"
        elif hostname != "Okänd enhet":
            device_name = hostname
        else:
            device_name = user_defined_name

        status_text = "🟢 Online" if status else "🔴 Offline"
        print(f"IP: {ip}  |  Status: {status_text}  |  Namn: {device_name}")

        # Spara kombinerat namn i DeviceManager om det inte redan finns
        if ip not in device_manager.device_mapping:
            device_manager.add_device(ip, device_name)

    # Skicka larm om någon enhet kopplats bort
    notifier = Notifier("jonasne@student.chalmers.se", "password")
    for ip, (status, hostname) in results.items():
        if not status:
            user_defined_name = device_manager.get_device_name(ip)
            if hostname != "Okänd enhet" and user_defined_name != f"Okänd enhet ({ip})":
                device_name = f"{user_defined_name} (hostname: {hostname})"
            elif hostname != "Okänd enhet":
                device_name = hostname
            else:
                device_name = user_defined_name

            notifier.send_email("security@chalmers.se", "⚠️ Larm! Enhet offline", f"{device_name} ({ip}) har kopplats bort!")
