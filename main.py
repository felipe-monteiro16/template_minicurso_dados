from curl_cffi import requests
from pathlib import Path
import pandas as pd

url = "https://dados.ons.org.br/api/3/action/package_show?id=cvu-usitermica"
SOURCE_RAW_PATH = Path("data/cvu-usitermica/source_raw")
PROCESSED_PATH = Path("data/cvu-usitermica/processed")
REQUIRED_COLS = {"dat_iniciosemana", "id_subsistema", "nom_usina", "val_cvu"}


def extract() -> list[Path]:
    ...


def transform(paths: list[Path]) -> pd.DataFrame:
    ...


def validate(df) -> None:
    ...


def load(df, file_path: Path) -> Path:
    ...


def split_by_subsystem(df: pd.DataFrame):
    ...


def main() -> None:
    paths = extract()
    df = transform(paths)
    validate(df)
    split_by_subsystem(df)


if __name__ == '__main__':
    main()