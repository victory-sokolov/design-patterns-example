from abc import ABC, abstractmethod

class Korean:
    def __init__(self, name):
        self.name = name

    def speak_korean(self):
        return "An-neyong?"

class British:
    def __init__(self, name):
        self.name = name

    def speak_english(self):
        return "Hello"

class Adapter:

    def __init__(self, object, **adapted_method):
        """Change name of the method"""
        self.object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self.object, attr)


objects = []
korean = Korean("Korean")
british = British("English")

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print(f"{obj.name} says {obj.speak()}")


# Example 2

class IIphone(ABC):
    @abstractmethod
    def use_lighting(self):
        raise NotImplemented

class IGooglePixel(ABC):
    @abstractmethod
    def use_micro_usb(self):
        raise NotImplemented


class IPhone7(IIphone):
    def use_lighting(self):
        print("Using lighting port")

class GooglePixel(IGooglePixel):
    def use_micro_usb(self):
        print("Using micro usb")

class LightingToMicroUsbAdapter(IGooglePixel):

    def __init__(self, iphone: IIphone):
        self.iphone = iphone

    def use_micro_usb(self):
        print("Want to use micro usb, converting to lighting")
        self.iphone.use_lighting()

iphone = IPhone7()
charge_adapter = LightingToMicroUsbAdapter(iphone)
charge_adapter.use_micro_usb()
