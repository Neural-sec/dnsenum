import dns.query
import dns.zone
import dns.resolver

domain = "exemplo.com"
registrosNS = dns.resolver.query(dominio, "NS")
lista = []

for registro in registrosNS:
    lista.append(str(registro))
for registro in lista:
    try:
        transferenciaZona = dns.zone.from_xfr(dns.query.xfr(registro, dominio))
    except:
        print("Erro na transferencia de zona")
    else:
        registroDNS = transferenciaZona.nodes.keys()
        registroDNS.sort()
        for n in registroDNS:
            print(transferenciaZona[n].to_text(n))