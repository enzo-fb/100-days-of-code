'''Jogo de RPG de Texto'''
import random
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, outro):
        dano = random.randint(1, self.ataque)
        outro.vida -= dano
        print(f"{self.nome} ataca {outro.nome} causando {dano} de dano!")

    def esta_vivo(self):
        return self.vida > 0
class JogoRPG:  
    def __init__(self):
        self.jogador = Personagem("Herói", 100, 20)
        self.inimigo = Personagem("Monstro", 80, 15)

    def iniciar(self):
        print("Bem-vindo ao Jogo de RPG!")
        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():
            self.turno()
        if self.jogador.esta_vivo():
            print("Você venceu!")
        else:
            print("Você foi derrotado!")

    def turno(self):
        print(f"\nVida do Herói: {self.jogador.vida}, Vida do Monstro: {self.inimigo.vida}")
        acao = input("Escolha sua ação (atacar/curar): ").strip().lower()
        if acao == "atacar":
            self.jogador.atacar(self.inimigo)
            if self.inimigo.esta_vivo():
                self.inimigo.atacar(self.jogador)
        elif acao == "curar":
            cura = random.randint(5, 15)
            self.jogador.vida += cura
            print(f"{self.jogador.nome} se cura por {cura} pontos de vida!")
            self.inimigo.atacar(self.jogador)
        else:
            print("Ação inválida!")
def main():
    jogo = JogoRPG()
    jogo.iniciar()

if __name__ == "__main__":
    main()