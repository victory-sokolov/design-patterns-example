from copy import deepcopy

class Prototype:

    def __init__(self):
        self.objects = {}

    def register_object(self, name, obj):
        """Register object"""
        self.objects[name] = obj

    def unregister_object(self, name):
        """Unregister object"""
        del self.objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = deepcopy(self.objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:

    def __init__(self, model, color, engine):
        self.model = model
        self.color = color
        self.engine = engine

    def __str__(self):
        return str(
            f"Model: {self.model}, Color: {self.color}, Engine: {self.engine}"
        )


car = Car(model="BMW", color="black", engine="V8")
proto = Prototype()
proto.register_object('bmw', car)

car2 = proto.clone('bmw', model="Audi", color="blue", engine="V6")

print(car)
print(car2)
