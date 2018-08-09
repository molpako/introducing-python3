class Duck(object):
    def __init__(self, input_name):
        self.__name = input_name
    
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name
    
fowl = Duck('Howard')
fowl.name
fowl.name = 'Donld'
fowl.name

# アクセスできない
fowl.__name

# 属性が非公開になるわけではなく、マングリングする
fowl._Duck__name