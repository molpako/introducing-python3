# Pythonは全ての属性とメソッドが公開であり
# プログラマーが行儀よく振る舞うのが前提になっているので
# getter, setter を書く必要がない.
# 属性を非公開にしたい場合は、プロパティを使う

class Duck(object):
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    
    name = property(get_name, set_name)

# get_name()が呼ばれる
fowl = Duck('Howard')
fowl.name

# 通常通り呼べる
fowl.get_name()

fowl.name = 'Daffy'
fowl.name


# プロパティは、デコレータで定義することができる
class DecoDuck(object):
    def __init__(self, input_name):
        self.hidden_name = input_name
    
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidde_name = input_name
    
fowl = DecoDuck('Howard')
fowl.name = 'Donale'
fowl.name


class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
c.radius

c.diameter
# @diameteer.setter を実装してないので設定できない
c.diameter = 20