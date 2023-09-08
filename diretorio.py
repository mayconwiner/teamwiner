import requests,os,platform

if platform.system() == "Windows":
    os.system("cls")
elif platform.system() == "Linux":
    os.system("reset")
else:
    print("Sistema não suportado")

LIGHT_GREEN = "\033[1;32m"
WHITE = "\033[1;37m"
LIGHT_RED = "\033[1;31m"
LIGHT_CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
CROSSED = "\033[9m"


diretorios = ['css', 'js', 'img', 'fonts', 'backups', 'wp-admin',
              'administrator', 'database', 'temp']  # diretorios que podem ser encontrados

print(LIGHT_CYAN+'''
                                                                                                                                        
@@@@@@@@@@    @@@@@@   @@@ @@@   @@@@@@@   @@@@@@   @@@  @@@     @@@@@@@    @@@@@@   @@@  @@@   @@@@@@@@  @@@        @@@@@@    @@@@@@   
@@@@@@@@@@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@     @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@@  @@@       @@@@@@@@  @@@@@@@   
@@! @@! @@!  @@!  @@@  @@! !@@  !@@       @@!  @@@  @@!@!@@@     @@!  @@@  @@!  @@@  @@!  @@@  !@@        @@!       @@!  @@@  !@@       
!@! !@! !@!  !@!  @!@  !@! @!!  !@!       !@!  @!@  !@!!@!@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!        !@!       !@!  @!@  !@!       
@!! !!@ @!@  @!@!@!@!   !@!@!   !@!       @!@  !@!  @!@ !!@!     @!@  !@!  @!@  !@!  @!@  !@!  !@! @!@!@  @!!       @!@!@!@!  !!@@!!    
!@!   ! !@!  !!!@!!!!    @!!!   !!!       !@!  !!!  !@!  !!!     !@!  !!!  !@!  !!!  !@!  !!!  !!! !!@!!  !!!       !!!@!!!!   !!@!!!   
!!:     !!:  !!:  !!!    !!:    :!!       !!:  !!!  !!:  !!!     !!:  !!!  !!:  !!!  !!:  !!!  :!!   !!:  !!:       !!:  !!!       !:!  
:!:     :!:  :!:  !:!    :!:    :!:       :!:  !:!  :!:  !:!     :!:  !:!  :!:  !:!  :!:  !:!  :!:   !::   :!:      :!:  !:!      !:!   
:::     ::   ::   :::     ::     ::: :::  ::::: ::   ::   ::      :::: ::  ::::: ::  ::::: ::   ::: ::::   :: ::::  ::   :::  :::: ::   
 :      :     :   : :     :      :: :: :   : :  :   ::    :      :: :  :    : :  :    : :  :    :: :: :   : :: : :   :   : :  :: : : 
 _    __                                                              _                       
' )  /                                                          /    //     /        /       /
 /  /_   _    _. __ ______    __  _  _   _   __ ____  _   __.  /__o // o __/ __.  __/ _     / 
(__//_)_</_  (__(_)/ / / <_  / (_</_/_)_/_)_(_)/ / <_/_)_(_/|_/_)<_</_<_(_/_(_/|_(_/_</_   '  
                                       /                                                  o  
      

  '''+WHITE)

# site que será testado
site = input(LIGHT_CYAN+"Digite o site ex:"+YELLOW+"https://oabto.org.br  :"+WHITE)
for pasta in diretorios:
    if site[len(site)-1] == "/":
        teste = site+pasta
    else:
        teste = site+"/"+pasta
    try:
        req = requests.get(teste)

        if req.status_code == 200 and req.status_code < 300:
            print(LIGHT_GREEN+"Diretorio encontrado: "+teste+WHITE)
        elif req.status_code == 400 or req.status_code == 403:
            print("Acesso Negtado: "+teste)
    except:
        print(f'''{requests.status_codes.text}
                Status:                                Diretório:
                {LIGHT_RED}Não foi possivel conectar ao site{WHITE}    {CROSSED}dd{teste}
              ''')


