
from typing import Union


class Car:
    '''The Product'''
    def __init__(self):
        self.model: Union[str, None] = None
        self.tires: Union[int, None] = None
        self.engine: Union[str, None] = None

    def __str__(self) -> str:
        return str(
            f"Model: {self.model}, Tires: {self.tires}, Engine: {self.engine}"
        )


class AbstractBuilder:
    '''Abstract Builder Interface'''
    def __init__(self):
        self.car = None

    def create_car(self):
        self.car = Car()


class CarBuilder(AbstractBuilder):

    def set_model(self, model: str):
        self.car.model = model

    def set_engine(self, engine: str):
        self.car.engine = engine

    def set_tires(self, tires: int):
        self.car.tires = tires


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self, model, tires, engine):
        self.builder.create_car()
        self.builder.set_engine(engine)
        self.builder.set_tires(tires)
        self.builder.set_model(model)
        return self.builder.car


builder = CarBuilder()
director = Director(builder)

model1 = director.construct_car(model="BMW", engine="V8", tires=4)
model2 = director.construct_car(model="Audi", engine="V8", tires=4)
print(model1)
print(model2)
