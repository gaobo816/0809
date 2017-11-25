class Person:

    def __init__(self,name,life_value,gre):
        self.name = name
        self.gre = gre
        self.life_value = life_value

    def attack(self,emy):
        emy.life_value = emy.life_value -self.gre

        return self.life_value

class Dog:

    def __init__(self,name,dlife_vale,dagres):
        self.name = name
        self.dlife_value = dlife_vale
        self.dagres = dagres

    def d_bite(self, person_o):
        person_o.life_value = person_o.life_value - self.dagres

        return person_o.life_value


agg = Person("egon",2000,88)
alex = Person("alex",1000,55)
dog_g = Dog("旺财",500,100)

print(alex.life_value)

agg.attack(alex)#1000 -88
print(alex.life_value)

print(agg.life_value)
dog_g.d_bite(agg) #2000 - 100
print(agg.life_value)




# print(agg.age)
# print(agg.life_value)

#
# class Dog:
#
#     def __init__(self,name,dlife_vale,dagres):
#         self.name = name
#         self.dlife_value = name
#         self.dagres = dagres
#
#     def d_bite(self, emy):
#         self.life_value = self.life_value - emy.gre
#
#         return self.life_value




