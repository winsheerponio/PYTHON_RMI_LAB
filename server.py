from Pyro5.api import Daemon, locate_ns

from product import Product


HOST = "127.0.0.1"
NAME_SERVER_PORT = 9090
OBJECT_PORT = 9000

PRODUCTS = {
    "laptop": Product("Laptop", "Lenovo laptop", 800000.0),
    "mobile": Product("Mobile", "MI 9 mobile", 24000.0),
    "bag": Product("Bag", "Branded bag", 800.0),
    "charger": Product("Charger", "MI Charger", 230.0),
}


def main() -> None:
    daemon = Daemon(host=HOST, port=OBJECT_PORT)
    name_server = locate_ns(host=HOST, port=NAME_SERVER_PORT)

    try:
        for product_id, product in PRODUCTS.items():
            uri = daemon.register(product, objectId=f"product.{product_id}")
            name_server.register(product_id, uri)

        print(f"Product server listening at {HOST}:{OBJECT_PORT}")
        print(f"Registered products: {', '.join(PRODUCTS)}")
        daemon.requestLoop()
    except KeyboardInterrupt:
        print("\nProduct server shutting down.")
    finally:
        name_server._pyroRelease()
        daemon.close()


if __name__ == "__main__":
    main()
