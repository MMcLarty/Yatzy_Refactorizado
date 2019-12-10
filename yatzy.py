class Yatzy:

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
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
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
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        for numero in range(2, 7):
            if dados.count(numero) != 1:
                return 0
        return Yatzy.chance(*dados)
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
