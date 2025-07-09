import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float


def load_fuel_price_from_config() -> float:
    config_path = Path(__file__).parent / "config.json"

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

        fuel_price = config["FUEL_PRICE"]

        return fuel_price
