from abc import ABC, abstractmethod

from app.domain.entities.user import UserAuthCodeEntity, UserEntity
from app.domain.events.user import (
    UserAuthCodeCreatedEvent,
    UserAuthCodeUpdatedEvent,
    UserCreatedEvent,
    UserUpdatedEvent,
)
from app.domain.repositories.user import UserAuthCodeRepository, UserRepository


class UserUseCases(ABC):
    @abstractmethod
    def __init__(
        self,
        user_repository: UserRepository,
        user_created_event: UserCreatedEvent,
        user_updated_event: UserUpdatedEvent,
    ):
        self.user_repository = user_repository
        self.user_created_event = user_created_event
        self.user_updated_event = user_updated_event

    @abstractmethod
    def users_catalog(self) -> list[UserEntity]:
        raise NotImplementedError

    @abstractmethod
    def user_detail(self, id: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def register_user(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user: UserEntity) -> UserEntity:
        raise NotImplementedError


class UserAuthCodeUseCases(ABC):
    @abstractmethod
    def __init__(
        self,
        user_auth_code_repository: UserAuthCodeRepository,
        user_auth_code_created_event: UserAuthCodeCreatedEvent,
        user_auth_code_updated_event: UserAuthCodeUpdatedEvent,
    ):
        self.user_auth_code_repository = user_auth_code_repository
        self.user_auth_code_created_event = user_auth_code_created_event
        self.user_auth_code_updated_event = user_auth_code_updated_event

    @abstractmethod
    def user_auth_codes_catalog(self) -> list[UserAuthCodeEntity]:
        raise NotImplementedError

    @abstractmethod
    def user_auth_code_detail(self, id: str) -> UserAuthCodeEntity:
        raise NotImplementedError

    @abstractmethod
    def register_user_auth_code(
        self,
        user_auth_code: UserAuthCodeEntity,
    ) -> UserAuthCodeEntity:
        raise NotImplementedError

    @abstractmethod
    def update_user_auth_code(
        self,
        user_auth_code: UserAuthCodeEntity,
    ) -> UserAuthCodeEntity:
        raise NotImplementedError
