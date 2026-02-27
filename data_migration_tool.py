import json
import os


def migrate_orders(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)

    transformed = [float(item["amount"]) for item in data]

    output_path = "migrated_orders.json"

    with open(output_path, "w") as f:
        json.dump(transformed, f)

    print("Migration completed.")


if __name__ == "__main__":
    migrate_orders("orders.json")