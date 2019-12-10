class Yatzy:
    def __init__(self, *dados):
        self.dados = list(dados)
        
    @staticmethod
    def chance(*dados):
        total = 0
        for num in dados:
            total += num
        return total

    @staticmethod
    def yatzy(*dados):
        if dados.count(dados[0]) != 5:
            return 0 
        return 50
    
    @staticmethod
    def ones(*dados):
        uno = 1
        return dados.count(uno) * uno

    @staticmethod
    def twos(*dados):
        dos = 2 
        return dados.count(dos) * dos
    
    @staticmethod
    def threes(*dados):
        tres = 3
        return dados.count(tres) * tres


    def fours(self):
        cuatro = 4
        return self.dados.count(cuatro) * cuatro
    

    def fives(self):
        cinco = 5
        return self.dados.count(cinco) * cinco
    

    def sixes(self):
        seis = 6
        return self.dados.count(seis) * seis
    
    @staticmethod
    def score_pair(*dados):
        par = 2
        for numero in range(6, 0, -1):
            if dados.count(numero) >= par:
                return par * numero
        return 0
    
    @staticmethod
    def two_pair(*dados):
        par = 2
        pares = 0
        total = 0
        numero = 1
        while pares < 2 and numero <= 6:
            if dados.count(numero) >= 2:
                pares += 1
                total += par * numero
            numero += 1
        if pares == 2:
            return total
        else:
            return 0
 
    @staticmethod
    def three_of_a_kind(*dados):
        tres = 3
        for numero in range(6, 0, -1):
            if dados.count(numero) >= tres:
                return tres * numero
        return 0

    @staticmethod
    def four_of_a_kind(*dados):
        cuatro = 4
        for numero in range(6, 0, -1):
            if dados.count(numero) >= cuatro:
                return cuatro * numero
        return 0
    
    @staticmethod
    def smallStraight(*dados):
        for numero in range(1, 6):
            if dados.count(numero) != 1:
                return 0
        return Yatzy.chance(*dados)

    @staticmethod
    def largeStraight(*dados):
        for numero in range(2, 7):
            if dados.count(numero) != 1:
                return 0
        return Yatzy.chance(*dados)
    

    @staticmethod
    def fullHouse(*dados):
        if Yatzy.__par_bajo(*dados) and Yatzy.three_of_a_kind(*dados):
            return Yatzy.__par_bajo(*dados) + Yatzy.three_of_a_kind(*dados)
        else:
            return 0
    
    @staticmethod
    def __par_bajo(*dados):
        par = 2
        for numero in range(6, 0, -1):
            if dados.count(numero) == par:
                return par * numero
        return 0


        
