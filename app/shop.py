import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Shop:
    name: str
    location: list
    products: dict


def create_shop(shops_data: dict) -> Shop:
    shop = Shop(
        name=shops_data["name"],
        location=shops_data["location"],
        products=shops_data["products"]
    )
    return shop


def load_shops_from_config() -> list[Shop]:
    config_path = Path(__file__).parent / "config.json"

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        shops = []

        if "shops" in config:
            for shop_data in config["shops"]:
                shop = create_shop(shop_data)
                shops.append(shop)
        return shops
