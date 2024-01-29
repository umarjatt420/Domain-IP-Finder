import socket

def get_domain_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

# Example usage
domain = input('Write Domian name here: ')
ip_address = get_domain_ip(domain)
if ip_address:
    print(f"The IP address of {domain} is: {ip_address}")
else:
    print(f"Failed to retrieve the IP address of {domain}")