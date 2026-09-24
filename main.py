from curl_cffi import requests
from pathlib import Path
import pandas as pd

url = "https://dados.ons.org.br/api/3/action/package_show?id=cvu-usitermica"
SOURCE_RAW_PATH = Path("data/cvu-usitermica/source_raw")
RAW_PATH = Path("data/cvu-usitermica/raw")


def extract() -> list[Path]:
    ...


def transform(paths: list[Path]):
    ...


def load(df, file_path: Path) -> Path:
    ...


def split_by_subsystem(df: pd.DataFrame):
    ...


def validate(df) -> None:
    ...


def main() -> None:
    ...


if __name__ == '__main__':
    main()