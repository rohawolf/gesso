from abc import ABC, abstractmethod

from app.domain.entities.file import FileEntity
from app.domain.events.file import FileCreatedEvent, FileUpdatedEvent
from app.domain.repositories.file import FileRepository


class FileUseCases(ABC):
    @abstractmethod
    def __init__(
        self,
        file_repository: FileRepository,
        file_created_event: FileCreatedEvent,
        file_updated_event: FileUpdatedEvent,
    ):
        self.file_repository = file_repository
        self.file_created_event = file_created_event
        self.file_updated_event = file_updated_event

    @abstractmethod
    def files_catalog(self) -> list[FileEntity]:
        raise NotImplementedError

    @abstractmethod
    def file_detail(self, id: str) -> FileEntity:
        raise NotImplementedError

    @abstractmethod
    def register_file(self, file: FileEntity) -> FileEntity:
        raise NotImplementedError

    @abstractmethod
    def update_file(self, file: FileEntity) -> FileEntity:
        raise NotImplementedError
