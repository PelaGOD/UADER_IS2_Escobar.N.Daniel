import os
import platform

class Ping:
    def execute(self, ip: str):
        if not ip.startswith("192."):
            raise ValueError("IP no permitida. Debe comenzar con '192.'")
        self._ping(ip)

    def executefree(self, ip: str):
        self._ping(ip)

    def _ping(self, ip: str):
        param = "-n" if platform.system().lower() == "windows" else "-c"
        print(f"Haciendo ping a {ip}...")
        os.system(f"ping {param} 10 {ip}")

class PingProxy:
    def __init__(self):
        self.real_ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("IP especial detectada. Redirigiendo a www.google.com con ejecutefree().")
            self.real_ping.executefree("www.google.com")
        else:
            self.real_ping.execute(ip)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    proxy = PingProxy()
    
    # Este hará ping a www.google.com
    proxy.execute("192.168.0.254")
    
    # Este hará ping a la IP indicada si empieza con "192."
    proxy.execute("192.168.1.1")

    # Este lanzará una excepción porque la IP no comienza con "192."
    try:
        proxy.execute("10.0.0.1")
    except ValueError as e:
        print(f"Error: {e}")
