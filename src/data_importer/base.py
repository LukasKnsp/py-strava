from abc import ABC, abstractmethod
from typing import List

from stravalib.model import Activity, Athlete


class Importer(ABC):

    @abstractmethod
    def get_activities() -> List[Activity]:
        NotImplementedError

    @abstractmethod
    def get_athlete() -> Athlete:
        NotImplementedError

    
