from core.common.exceptions import ServiceException

from dataclasses import dataclass

@dataclass(eq=False)
class TaskTypeError(ServiceException):
    
    @property
    def message(self):
        return 'Type error'