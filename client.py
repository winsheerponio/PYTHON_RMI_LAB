from Pyro5.api import Proxy, locate_ns


HOST = "127.0.0.1"
NAME_SERVER_PORT = 9090
PRODUCT_IDS = ("laptop", "mobile", "bag", "charger")


def main() -> None:
    name_server = locate_ns(host=HOST, port=NAME_SERVER_PORT)

    try:
        for product_id in PRODUCT_IDS:
            product = Proxy(name_server.lookup(product_id))
            try:
                print(f"Name: {product.get_name()}")
                print(f"Description: {product.get_description()}")
                print(f"Price: {product.get_price():.2f}")
                print()
            finally:
                product._pyroRelease()
    finally:
        name_server._pyroRelease()


if __name__ == "__main__":
    main()
