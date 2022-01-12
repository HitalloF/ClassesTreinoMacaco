class macacos:
    def __init__(self, nome, cor, comendo=False, andando=False, galho=False ):

        self.nome = nome
        self.cor = cor
        self.comendo = comendo
        self.andando = andando
        self.galho = galho

    def comer(self, alimento):
        if self.comendo:
            print(f'O Macaco {self.nome} ja esta comendo')
            return
        if self.andando:
            print(f"O Macaco {self.nome} esta andando, nao pode comer agora")
            return
        if self.galho:
            print(f"O Macaco {self.nome} esta muito alto, tem medo de derrubar sua comida, descar do galho para comer")
        print(f'O Macaco {self.nome} comecou a comer {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'O Macaco {self.nome} nao esta comendo')
            return
        print(f'O Macaco {self.nome} parou de comer')
        self.comendo = False

    def andar(self):
        if self.comendo:
            print(f"O Macaco {self.nome} esta comendo, ele nao quer andar")
            return

        if self.andando:
            print(f" o Macaco {self.nome} ja ta andando")
            return

        print(f"O Macaco {self.nome} comecou a andar")
        self.andando = True

    def parar_andar(self):
        if not self.andando:
            print(f'O Macaco {self.nome} esta parado')
            return
        print(f"O Macaco {self.nome} cansou, esta parado")
        self.andando = False
    def subir_galho(self):
        if self.galho:
            print(f"O Macaco {self.nome} ja esta em um galho")
            return
        if self.comendo:
            print(f" O Macaco {self.nome} nao quer derrubar a sua comida")
            return
        if self.andando:
            print(f'O Macaco {self.nome} tem que parar antes de subir em um galho')
            return
        print(f"O Macaco {self.nome} subiu em um galho")
        self.galho = True
    def descer_galho(self):
        if not self.galho:
            print(f'O Macaco {self.nome} nao esta em cima de uma arvore.')
            return
        print(f'O Macaco {self.nome} desceu da arvore')
        self.galho = False
