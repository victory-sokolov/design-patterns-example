from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer):
        raise NotImplementedError

    @abstractmethod
    def notify(self):
        raise NotImplementedError

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        raise NotImplementedError

class WeatherStation(Subject):

    def __init__(self):
        self._observers = []

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: int):
        self._temperature = temperature
        self.notify()

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """Detach an observer from the subject."""
        for observer in self._observers:
            if observer == observer:
                self._observers.remove(observer)

    def notify(self):
        """Notify all observers about an event."""
        for observer in self._observers:
            observer.update(self._temperature)


class TempInfo(Observer):
    def __init__(self, weather_station: Subject):
        self.weather_station = weather_station
        self.weather_station.attach(self)

    def update(self, temperature: int):
        print("Temperature: I need to update my display.")


class Fan(Observer):
    def __init__(self, weather_station: Subject):
        self.weather_station = weather_station
        self.weather_station.attach(self)

    def update(self, temperature: int):
        if(temperature > 25):
            print("Fan: it's hot here, turning myself on..")
        else:
            print("Fan: it's nice and cool, turning myself off..")


weather_station = WeatherStation()

temp_display = TempInfo(weather_station)
fan = Fan(weather_station)

weather_station.temperature = 20
weather_station.temperature = 40
