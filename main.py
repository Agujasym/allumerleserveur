import requests
from mcstatus import MinecraftServer

def postServerRequest(requestType):
    payload = [{"requesttype":requestType}]
    r = requests.post(
        'https://prod-250.westeurope.logic.azure.com:443/workflows/99bf7de2999e4d15aa95bf1ea4aa7a21/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=ZXMqfMurefNv2IMxmNmidbpq9FyIzXA6aamgtEnfYDU',
        json = payload
    )
    return r.status_code

print("Recherche du serveur...")
try:
    server = MinecraftServer.lookup("cestnotreprojet.westeurope.azurecontainer.io")
    status = server.status()
    print(
        "Le serveur est allume. {0} joueurs sont en ligne et le ping est de {1} ms.\n".format(
            status.players.online,
            status.latency
        )
    )
    isOn = True
    command = input("Pour eteindre le serveur, tapez 'stop'\n")
except:
    print("Le serveur est eteind.")
    isOn = False
    command = input("Pour allumer le serveur, tapez 'start'\n")
    
if command == "start" and ~isOn:
    print("Allumage en cours...")
    if postServerRequest("start") == 202:
        print("L'allumage a reussi! Dans quelques minutes vous pourrez rejoindre le serveur.")
    else:
        print("Allumage echoue. Veuillez prendre contact avec votre administrateur.")

elif command == "stop" and isOn:
    print("Le serveur s'eteind...")
    if postServerRequest("stop") == 202:
        print("Le serveur s'est eteind.")
    else:
        print("Le serveur ne s'est pas eteind. Veuillez prendre contact avec votre administrateur.")

else:
    print("Votre commande n'est pas reconnue")

input("Pour quitter appuyez sur Enter.")