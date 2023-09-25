# Aqui está o código organizado:

# Imprime a arte ASCII para o titulo
print('''
   _________________________________________________________
 /|     -_-                                             _-  |\
/ |_-_- _                                         -_- _-   -| \\   
  |                            _-  _--                      | 
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |          
  |   /   |   ()        \\      U      /   |    ()       \\   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |  
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -        lc \
/   -_- _ -             _- _---                       -_-  -_ \

 ---.----.__..----.----| _|_||___||___||___||___||___||___||_|_ |
    |        |    |    | -.-..---..---..---..---..---..---..-.- |--.-
 ---'--.-----'----'--.-|  | ||   ||   ||   ||   ||   ||   || |  | `|
       |:           (| |  | ||   ||   ||   ||   ||   ||   || |  |--'-
       |:.           | | _|_||___||___||___||___||___||___||_|_ |
 ------'----.-.,----.'-| -.-..---..---..---..---..---..---..-.- |-.--
        ,/) |       |  |  | ||   ||   ||   ||   ||   ||   || |  | |`
 ----.---8--'--.----'--|  | ||   ||   ||   ||   ||   ||   || |  | |
     |   8     |:      | _|_||___||___||___||___||___||___||_|_ |-'--
     | ,)//    |:.     | -.-..---..---..---..---..---..---..-.- |:.
 ----'-`=;'--.-'-.----.|  | ||   ||   ||   ||   ||   ||   || |  |--.-
       //   /_ _( \\    |  | ||   ||   ||   ||   ||   ||   || |  | /|
 ---.-//----)/\\,'_/----| _|_||___||___||___||___||___||___||_|_ | `|
    |/|     `;=.(      | -.-..---..---..---..---..---..---..-.- |--'-
 (  |`.`.   |`,-/      |,-'-||---||---||---||---||---||---||-'-.|
 -`-'-.`.`-.';'=`.-..--'-.--------.-------------.--.-------.----'--.-
      |  `-./.}{-'\\.)    |        )             |   `)     |       \
      |    :`-}{-''||    |:.      |   ,_        |          |:.     |
 ---'`'-.--|`-}{-'||)----'-.------'--'.,`--.----'--------.-'-------'-
        |  :`-`'-'/)|      |               |:.           |
 -.-----'--;`.}{,`.||----,-'--------.------'---.--------,'--.,-------
  |:     ,'/.`..'_(/(    |:         |          |             \
  |:.  ,',' |`--`.('))   |:.        |          |             |:
 -'--,' <.._|__,. >`,----'----------'--------.,'-------------'----SSt
     ``----....(','
            _,'>'
            )/
            `'

     888                                                         
     888                                                         
     888                                                         
 .d88888888  88888888b.  .d88b.  .d88b.  .d88b. 88888b. .d8888b  
d88" 888888  888888 "88bd88P"88bd8P  Y8bd88""88b888 "88b88K      
888  888888  888888  888888  88888888888888  888888  888"Y8888b. 
Y88b 888Y88b 888888  888Y88b 888Y8b.    Y88..88P888  888     X88 
 "Y88888 "Y88888888  888 "Y88888 "Y8888  "Y88P" 888  888 88888P' 
                             888                                 
                        Y8b d88P                                 
                         "Y88P"       
''')

# Imprime a mensagem de boas-vindas
print("Bem-vindo às Masmorras da Ilha do Tesouro.")
print("Seu objetivo é encontrar o tesouro que está escondido nesta terrível ilha.")

# Primeira escolha
primeira_escolha = input(
    "Após uma terrível tempestade, você chegou à ilha e à sua frente, existem dois caminhos. Qual caminho você gostaria de seguir? Digite 'esquerda' ou 'direita' \n").lower()

if primeira_escolha == "esquerda":
    # Segunda escolha
    segunda_escolha = input(
        "Você conseguiu entrar em uma caverna escura e úmida. Com a tocha que pegou ao longo do caminho, você se depara com vários corpos, dentre eles estão algumas armas. Qual você escolhe? Digite 'espada', 'besta' ou 'lança' \n").lower()

    if segunda_escolha == "espada":
        print("Você escolheu a espada.")

    elif segunda_escolha == "besta":
        print("Você escolheu a besta, mas precisa encontrar virotes.")

    elif segunda_escolha == "lança":
        print("Você escolheu a lança.")

    # Terceira escolha
    terceira_escolha = input(
        f"Ao escolher a {segunda_escolha}, um monstro desperta e tenta te atacar. O que você faz? Digite 'esquivar', 'atacar' ou 'defender' \n").lower()

    # Imprime a arte ASCII para o monstro
    print('''
    (                      )
          |\    _,--------._    / |
          | `.,'            `. /  |
          `  '              ,-'   '
           \/_         _   (     /
          (,-.`.    ,',-.`. `__,'
           |/#\ ),-','#\`= ,'.` |
           `._/)  -'.\_,'   ) ))|
           /  (_.)\     .   -'//
          (  /\____/\    ) )`'\
           \ |V----V||  ' ,    \
            |`- -- -'   ,'   \  \      _____
     ___    |         .'    \ \  `._,-'     `-
        `.__,`---^---'       \ ` -'
           -.______  \ . /  ______,-
                   `.     ,'            
    ''')

    # Bloco de código para cada opção de terceira escolha
    if terceira_escolha == "esquivar":
        terceira_escolha1 = input(
            "A esquiva foi bem-sucedida e você está atrás do monstro. Você quer atacar? Digite 'sim' ou 'não' \n").lower()

        if terceira_escolha1 == "sim":
            print("O monstro foi derrotado e você pode vasculhar o corpo do monstro.")

        else:
            print("O monstro se vira rapidamente e com um ataque brutal, acaba com a sua vida. Fim de Jogo!")

    elif terceira_escolha == "atacar":
        print("O monstro foi derrotado com um ataque veloz e você pode vasculhar o corpo do monstro.")

    else:
        terceira_escolha2 = input("A defesa foi bem sucedida. Você quer atacar? Digite 'sim' ou 'não' \n").lower()
        if terceira_escolha2 == "sim":
            print("O monstro foi derrotado e você pode vasculhar o corpo do monstro.")
        else:
            print("O monstro se vira rapidamente e com um ataque brutal, acaba com a sua vida. Fim de Jogo!")

    # Quarta escolha
    quarta_escolha = input(
        "Ao vasculhar o monstro você encontra uma chave, que pode abrir uma das três portas, uma vermelha, outra amarela e a última azul. Qual você escolhe? \n").lower()
    if quarta_escolha == "vermelha":
        print("É uma sala cheia de pítons. Fim de Jogo.")
    elif quarta_escolha == "amarela":
        print("Você encontrou o tesouro! Você venceu!")
        # Imprime a arte ASCII para o tesouro
        print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    elif quarta_escolha == "azul":
        print("Você entrou numa sala cheia de monstros que acordam com o abrir da porta e te atacam. Fim de Jogo.")
    else:
        print("Sua escolha não existe. Fim de Jogo.")

else:
    print("Você caiu em um buraco cheio de estacas. Fim de Jogo.")
