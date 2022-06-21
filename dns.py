import socket

# site para fazer a varredura
domain = "exemplo.com"
# arquivo de brute force
with open("force.txt") as arquivo:
    names = arquivo.readlines()
for name in names:
    DSN = name.strip("\n") + "." + domain
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass
