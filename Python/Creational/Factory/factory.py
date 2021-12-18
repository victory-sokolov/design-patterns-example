from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, Union


class LoggerMedium(Enum):
    MEMORY = "MEMORY"
    FILE = "FILE"
    DB = "DB"


class ILogger(ABC):
    @abstractmethod
    def log(self, message: str):
        raise NotImplementedError


class InMemoryLog(ILogger):
    def log(self, message: str) -> str:
        return f"Logging to Memory: {message}"


class FileLog(ILogger):
    def log(self, message: str) -> str:
        return f"Logging to File: {message}"


class DBLog(ILogger):
    def log(self, message: str) -> str:
        return f"Logging to Database: {message}"


class LoggerFactory:

    def getInstance(self, loggerMedium: LoggerMedium) -> ILogger:
        if loggerMedium == LoggerMedium.MEMORY:
            return InMemoryLog()
        elif loggerMedium == LoggerMedium.FILE:
            return FileLog()
        elif loggerMedium == LoggerMedium.DB:
            return DBLog()

        raise TypeError(f"{loggerMedium} is not valid Logger type.")


logger = LoggerFactory()
inst = logger.getInstance(LoggerMedium.FILE)
print(inst.log("My message"))
