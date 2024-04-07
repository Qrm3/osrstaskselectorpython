from enum import Enum
from datetime import datetime

class TaskCategory(Enum):
    UNIQUE = 1
    REPEATABLE = 2
    PASSIVE = 3

class Task:
    def __init__(self, category: TaskCategory, name: str, description: str, time_created: datetime) -> None:
        self.category = category
        self.name = name
        self.description = description
        self.time_created = time_created
        self.time_completed = []
        self.completion_count = 0
    
    def mark_complete(self) -> None:
        if self.category == TaskCategory.UNIQUE:
            self.completion_count = 1
        else:
            self.completion_count += 1
        
        self.time_completed.append(datetime.now())
        
    def update_description(self, description: str) -> None:
        self.description = description
        
    def times_completed(self) -> int:
        if self.category == TaskCategory.UNIQUE:
            return 1

        return self.completion_count
