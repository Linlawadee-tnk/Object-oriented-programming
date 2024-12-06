class Cat :
    def ___init___(self,name,color):
        self.Name = name
        self.Color = color
        self.fish = 0
    def cry(self):
        print(f"{self.Name} ร้องเมี๊ยว")
    def eat(self,fish):
        self.fish += fish
        self.cry()
Cat1 = Cat('ศรีทอง','สีส้ม')
Cat2 = Cat('ศรีเงิน','สีขาว')

Cat2.eat(5)
print(Cat2.fish)