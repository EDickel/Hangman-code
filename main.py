from tkinter import *
import random

animal = [
    'Cachorro', 'Gato', 'Golfinho', 'Leao', 'Girafa', 'Lobo', 'Macaco',
    'Ovelha', 'Papagaio', 'Polvo', 'Pombo', 'Rinoceronte', 'Tartaruga',
    'Touro', 'Urso', 'Vaca'
]

fruta = [
    'Abacate', 'Abacaxi', 'Açai', 'Acerola', 'Amora', 'Banana', 'Cacau',
    'Carambola', 'Cereja', 'Coco', 'Damasco', 'Framboesa', 'Goiaba', 'Mamao'
]

objeto = [
    'Balao', 'Bandeira', 'Bateria', 'Bicicleta', 'Bacia', 'balança', 'Dado',
    'dardo', 'dedal', 'envelope', 'Faca', 'Sabonete'
]

def iniciar_jogo():
    # Limpa todos os widgets da janela
    for widget in tela.winfo_children():
        widget.destroy()

    # Seleciona um dos conjuntos
    conjTodos = [animal, fruta, objeto]
    conjSorteado = random.choice(conjTodos)

    # Seleciona uma palavra dentro do conjunto sorteado
    if conjSorteado == animal:
        palavSorteada = str(random.choice(animal))
        dicaConj = 'Animal'
    elif conjSorteado == fruta:
        palavSorteada = str(random.choice(fruta))
        dicaConj = 'Fruta'
    else:
        palavSorteada = str(random.choice(objeto))
        dicaConj = 'Objeto'

    # Separa e esconde a palavra sorteada
    palavSorteada = palavSorteada.lower()
    escon = str(palavSorteada.replace(palavSorteada, '-' * len(palavSorteada)))

    # Transforma a palavra escondida em uma lista
    esconl = list(escon)

    # Variáveis de controle
    letrasRepetidas = []
    chances = 10
    partidaOFF = False

    # Função para verificar a letra inserida
    def verificar_letra():
        nonlocal chances, partidaOFF
        n = letra.get().lower()
        letra.delete(0, END)

        if not n.isalpha() or len(n) != 1:
            resultado.config(text="Por favor, digite uma letra válida.")
            return

        if n in letrasRepetidas:
            resultado.config(text="Essa letra já foi escolhida!")
            return

        letrasRepetidas.append(n)
        letrasusad.config(text=f"Letras utilizadas: {' - '.join(letrasRepetidas)}")

        if n in palavSorteada:
            for k in range(len(palavSorteada)):
                if palavSorteada[k] == n:
                    esconl[k] = n
            resultado.config(text=f"Boa! A letra '{n}' está na palavra.")
            forcaforma(chances)
        else:
            chances -= 1
            resultado.config(text=f"A letra '{n}' não está na palavra. Você ainda tem {chances} chances.")
            forcaforma(chances)

        escon.config(text=''.join(esconl))

        if ''.join(esconl) == palavSorteada:
            resultado.config(text=f"Você ganhou! A palavra era: {palavSorteada}")
            partidaOFF = True
            botao.config(state=DISABLED)
        elif chances == 0:
            resultado.config(text=f"Você perdeu! A palavra era: {palavSorteada}")
            partidaOFF = True
            botao.config(state=DISABLED)
        if partidaOFF:
            botaoReiniciar = Button(tela, text="recomeçar", bg='pink', fg='white', command=iniciar_jogo)
            botaoReiniciar.pack(pady=20)

    # Widgets do jogo da forca
    escon = Label(tela, text=''.join(esconl), bg='pink', fg='black', font=('Helvetica', 24))
    escon.pack(pady=20)

    letra= Entry(tela, font=('Helvetica', 16))
    letra.pack(pady=10)

    botao = Button(tela, text="Enviar", bg='pink', fg='black', command=verificar_letra)
    botao.pack(pady=10)

    resultado = Label(tela, text="", bg='pink', fg='black')
    resultado.pack(pady=10)

    letrasusad = Label(tela, text="Letras utilizadas: ", bg='pink', fg='black')
    letrasusad.pack(pady=10)

def forcaforma(tentativas):
    if tentativas == 9:
        forca = Label(tela, text='''
                            
                            
                            
                            
                          ===''', bg='pink', fg='black')
        forca.pack(pady=20)
    elif tentativas == 8:
        forca = Label(tela, text='''
                            
                           |
                           |
                           |
                          ===''', bg='pink', fg='black')
        forca.pack(pady=20)
        forca.destroy()
        if tentativas == 7:
            forca = Label(tela, text='''
                           +---+
                               |
                               |
                               |
                              ===''', bg='pink', fg='black')
            forca.pack(pady=20)
        if tentativas == 6:
            forca = Label(tela, text='''
                           +---+
                               |
                               |
                               |
                              ===''', bg='pink', fg='black')
            forca.pack(pady=20)

# Inicialização da janela principal
tela = Tk()

# Configuração da janela
tela.title("                         jogo da forca")
tela.geometry("680x500")  # Largura x Altura
tela.configure(bg='pink')  # Definindo a cor de fundo

# Adicionando um rótulo à janela
texto = Label(tela, text="Clique no botão para começar o jogo", bg='pink', fg='black')
texto.pack(pady=20)

# Adicionando um botão à janela
botao = Button(tela, text="começar", bg='pink', fg='white', command=iniciar_jogo)
botao.pack(pady=20)

# Executando o loop principal da janela
tela.mainloop()

