from dataclasses import dataclass

from src.datalayer.base import RepositoryInterface


@dataclass
class ServiceBase:
    repository: RepositoryInterface