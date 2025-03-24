import os


class JogoDaForca:
    def __init__(self):
        self.palavras = ['dragao de komodo', 'jacare', 'paralelepipedo']
        self.palavra_escolhida = ''
        self.letras_tentadas = []

    def ocultar_palavra(self, palavra):
            if ' ' in palavra:
                palavra = palavra.split()
                palavra = list(map(lambda x: '-' * len(x), palavra))
                return ' '.join(palavra)
            else:
                return '-' * len(palavra)

    def boceco(self, valor):
        if valor == 6:
            print(r'''
|----------|
|          |
|          
|         
|         
|
 ''', end='')
        if valor == 5:
            print(r'''
|----------|
|          |
|          ◯
|         
|         
|
 ''', end='')
        if valor == 4:
            print(r'''
|----------|
|          |
|          ◯
|         /
|
|
 ''', end='')
        if valor == 3:
            print(r'''
|----------|
|          |
|          ◯
|         /|
|         
|
 ''', end='')
        if valor == 2:
            print(r'''
|----------|
|          |
|          ◯
|         /|\
|         
|
 ''', end='')
        if valor == 1:
            print(r'''
|----------|
|          |
|          ◯
|         /|\
|         /
|
 ''', end='')
        if valor == 0:
            print(r'''
|----------|
|          |
|          ◯
|         /|\
|         / \
|
 ''',end='')

    def jogo(self):
        os.system('cls')
        while self.palavras:
            self.palavra_escolhida = self.palavras[0]
            self.palavras.pop(0)

            palavra_oculta = self.ocultar_palavra(self.palavra_escolhida)
            tracos = list(palavra_oculta)
            vida = 6
            print('\n')
            self.boceco(vida)
            print(palavra_oculta)
            while not vida == 0:
                print(f'Sua vida: {vida}')
                if ''.join(tracos) == self.palavra_escolhida:
                    print('Voce acertou a palavra! Voce venceu!')
                    escolha = str(input('Voce deseja continuar o jogo com outra palavra? [s/n]: ').lower())
                    if escolha == 's':
                        os.system('cls')
                        continue

                    else:
                        exit()

                letra = str(input('\nDigite uma letra: '))
                os.system('cls')
                if len(letra) == 1:
                    if letra not in self.letras_tentadas:
                        self.letras_tentadas.append(letra)
                        if letra in self.palavra_escolhida:
                            index_letra = []
                            for chave, valor in enumerate(self.palavra_escolhida):
                                if letra == valor:
                                    index_letra.append(chave)
                            for i in index_letra:
                                tracos[i] = letra
                            print('\n')
                            self.boceco(vida)
                            print(''.join(tracos))

                        else:
                            vida -= 1
                            print('Não há essa letra.\n')
                            self.boceco(vida)
                            print(''.join(tracos))

                            if vida == 0:
                                print(f'Voce perdeu. A palavra era: {self.palavra_escolhida}')
                                escolha = str(input('Voce deseja continuar o jogo com outra palavra? [s/n]: ').lower())
                                if escolha == 's':
                                    os.system('cls')
                                    continue

                                else:
                                    exit()
                    else:
                        print('Voce ja tentou essa letra.')
                        print('')
                        self.boceco(vida)
                        print(''.join(tracos))

a = JogoDaForca()
a.jogo()
