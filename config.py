from dataclasses import dataclass

from environs import Env


@dataclass
class Database:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class Bot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    bot: Bot
    db: Database


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env()

    return Config(
        bot=Bot(
            token=env("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMIN_IDS"))),
        ),
        db=Database(
            database=env("DATABASE"),
            db_host=env("DB_HOST"),
            db_user=env("DB_USER"),
            db_password=env("DB_PASSWORD"),
        ),
    )
