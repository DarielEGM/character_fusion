class Pj:
    def __init__(self, name, power, speed):
        self.name=name
        self.power=power
        self.speed=speed
    
    def __repr__(self):
        return f'{self.name} (Power: {self.power},Speed: {self.speed})'
    
    def __add__(self,other_pj):
        new_name = self.name +"-"+ other_pj.name
        new_power = round(((self.power + other_pj.power)/2)**1.34)
        new_speed = round(((self.speed + other_pj.speed)/2)**1.34)
        return Pj(new_name,new_power,new_speed)
    

pj1 = Pj("Goku", 100,100)
pj2 = Pj("Vegeta", 99,99)
pj3 = Pj("Jiren",130,140)

pj4 = pj1 + pj2 + pj3

print(pj4)