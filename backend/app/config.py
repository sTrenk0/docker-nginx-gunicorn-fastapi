from typing import Literal

from pydantic.fields import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        case_sensitive=False,
    )
    proxy_prefix: str = "/api/"
    site_domain: str
    sub_domains: list[str] = Field(default_factory=list)
    stage: Literal["dev", "prod"] = "prod"


config = Config()
