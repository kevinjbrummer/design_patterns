from abc import ABC, abstractclassmethod

class FlyingBehavior(ABC):
  @abstractclassmethod
  def fly(self):
    pass

class CanFly(FlyingBehavior):
  def fly(self):
    print('I can fly!')

class CannotFly(FlyingBehavior):
  def fly(self):
    print("I can't fly!")

class RocketFly(FlyingBehavior):
  def fly(self):
    print('Rocket powered flight!')
    
class QuackBehavior(ABC):
  @abstractclassmethod
  def quack(self):
    pass

class CanQuack(QuackBehavior):
  def quack(self):
    print('Quack!')

class CannotQuack(QuackBehavior):
  def quack(self):
    print('<-- SILENCE -->')

class Squeak(QuackBehavior):
  def quack(self):
    print('Squeak!')

class Duck:
  def setQuackBehavior(self, quackBehavior):
    self.quackBehavior = quackBehavior
    
  def setFlyBehavior(self, flyBehavior):
    self.flyBehavior = flyBehavior
    
  def quack(self):
    self.quackBehavior.quack()

  def fly(self):
    self.flyBehavior.fly()

  def swim(self):
    print('I can swim!')

class Mallord(Duck):
  def __init__(self):
    self.flyBehavior = CanFly()
    self.quackBehavior = CanQuack()

class RubberDuck(Duck):
  def __init__(self):
    self.flyBehavior = CannotFly()
    self.quackBehavior = Squeak()

if __name__ == '__main__':
  mallord = Mallord()
  rubberDuck = RubberDuck()

  mallord.quack()
  mallord.fly()
  rubberDuck.quack()
  rubberDuck.setQuackBehavior(CanQuack())
  rubberDuck.quack()