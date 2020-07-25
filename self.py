class Person():
    def __init__(self,name,age,address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello,self.name))

brook = Person('브룩',26,'강북구')
brook.greeting()

print('이름: ',brook.name)
print('나이: ',brook.age)
print('주소: ',brook.address)