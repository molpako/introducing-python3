class Car(object):
    def exclaim(self):
        print("I'm Car!")

# carオブジェクトのクラス(Car)を探す
# Carクラスのexclaim()にself引数としてcarオブジェクト渡す
car = Car()
car.exclaim()

# こうかける
Car.exclaim(car)