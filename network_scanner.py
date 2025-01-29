import nmap

class NmapScanner:
    """Skannar nätverket med Nmap och returnerar en dictionary {IP: (Status, Hostname)}."""

    def __init__(self, network_range="192.168.86.0/24"):
        self.network_range = network_range
        self.scanner = nmap.PortScanner()

    def scan_network(self):
        """Utför en nätverksskanning och returnerar en dictionary med IP, status och hostname."""
        print(f"🔍 Skannar nätverket {self.network_range} med Nmap...\n")
        self.scanner.scan(hosts=self.network_range, arguments="-sn -R")  # -R för Reverse DNS lookup

        devices = {}
        for host in self.scanner.all_hosts():
            status = self.scanner[host].state() == "up"  # True/False
            hostname = self.scanner[host].hostname()  # Hämta hostname, eller tom sträng om det saknas
            devices[host] = (status, hostname if hostname else "Okänd enhet")  # Lägg till hostname

        return devices  # {IP: (True/False, "Hostname")}

if __name__ == "__main__":
    scanner = NmapScanner("192.168.1.0/24")  # Ändra till ditt nätverk
    results = scanner.scan_network()

    print("\n📋 Upptäckta enheter:")
    for ip, (status, hostname) in results.items():
        status_text = "🟢 Online" if status else "🔴 Offline"
        print(f"IP: {ip}  |  Status: {status_text}  |  Namn: {hostname}")
