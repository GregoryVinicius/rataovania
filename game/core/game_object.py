from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, name: str = "GameObject"):
        self.name = name
        self.enabled = True
        
    @abstractmethod
    def Update(self):
        pass
        
    @abstractmethod
    def Draw(self):
        pass