import requests
diretorios = ['css', 'js', 'img', 'fonts','backups','wp-admin','administrator','database','temp'] #diretorios que podem ser encontrados

site = input("Digite o site ex: https://oabto.org.br  :") #site que será testado
for pasta in diretorios:
    if site[len(site)-1] == "/":
        teste = site+pasta
    else:
        teste = site+"/"+pasta
    try:
        req = requests.get(teste)

        if req.status_code == 200 and req.status_code < 300:
            print("Diretorio encontrado: "+teste)
        elif req.status_code == 400 or req.status_code == 403:
            print("Acesso Negtado: "+teste)
    except:
        print("Erro ao conectar ao site: "+teste)
