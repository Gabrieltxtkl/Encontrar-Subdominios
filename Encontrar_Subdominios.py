import requests

def response(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

lista = []

qual_url = input('Qual o site você quer encontrar o subdomino?: --->')
with open(input('Qual a sua wordlist?: --->'), 'r') as file:
    for line in file.readlines():
        word = line.strip()
        nova_url = word + "." + qual_url

        data = response("http://" + nova_url)

        if data:
            lista.append(nova_url)
            print('[+] Subdominio encontrado ---> ' + nova_url)
        else:
            print('[-] Subdominio não encontrado ---> ' + nova_url)
            pass
print(lista)

salvar_arquivo = open(input('Qual o nome do arquivo para salvar os Subdominios?: ---> ')+'.txt', 'a')

for subdomain in lista:
    salvar_arquivo.write(subdomain +"\n")