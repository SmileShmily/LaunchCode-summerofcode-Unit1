class cat:
    '''This is the cat class'''
def _init_(self,name,color,fur_type):
    self.color=color
    self.fur_type=fur_type
    self.name=name
    self.awake=True
    self.age=1
def meow(self):
    '''make the cat meow'''
    if self.awake:
        print(self.name,
              self.age,
              self.color,
              self.fur_type,)
def sleep(self):
    '''make the cat sleep'''
    self.awake=False
def birthday(self):
    '''age the cat one year'''
    self.age+=1
'''snickers=cat('Snickers','orange','mangy')
snickers.meow()
snickers.birthday()
snickers.meow()
'''
