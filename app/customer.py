import json
from pathlib import Path
from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car


def create_customer(customer_data: dict) -> Customer:
    car_data = customer_data["car"]
    car = Car(
        brand=car_data["brand"],
        fuel_consumption=car_data["fuel_consumption"],
    )

    customer = Customer(
        name=customer_data["name"],
        product_cart=customer_data["product_cart"],
        location=customer_data["location"],
        money=customer_data["money"],
        car=car,
    )
    return customer


def load_customers_from_config() -> list[Customer]:
    config_path = Path(__file__).parent / "config.json"

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

        customers = []
        if "customers" in config:
            for customer_data in config["customers"]:
                customer = create_customer(customer_data)
                if customer:
                    customers.append(customer)
        return customers
