# abstract classes : exists to ensure that the subclasses of it, follow a particular protocol laid by the abstract class
from abc import ABC, abstractmethod
class Shape(ABC):

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass