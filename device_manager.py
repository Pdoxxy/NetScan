class DeviceManager:
    """Hanterar enhetsmappning och kan namnge IP-adresser."""

    def __init__(self):
        # Enhetsmappning: IP -> Namn
        self.device_mapping = {
            "192.168.86.110": "Doxxy Computer",
            "192.168.86.98": "Doxxy work laptop",
            "192.168.86.86": "DoxxyPhone",
        }

    def get_device_name(self, ip):
        """Returnerar enhetens namn om den finns i mappningen, annars returnerar IP-adressen."""
        return self.device_mapping.get(ip, f"Okänd enhet ({ip})")

    def add_device(self, ip, name):
        """Lägger till en ny enhet i mappningen."""
        self.device_mapping[ip] = name

    def remove_device(self, ip):
        """Tar bort en enhet från mappningen."""
        if ip in self.device_mapping:
            del self.device_mapping[ip]

# Exempel på att lägga till en enhet
if __name__ == "__main__":
    dm = DeviceManager()
    dm.add_device("192.168.1.100", "Ny dator")
    print(dm.get_device_name("192.168.1.100"))  # Output: Ny dator
