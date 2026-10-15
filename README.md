# Python RMI Lab (Pyro5)

A Python translation of the `JAVA_RMI_IV` product example in [nix1947/sunway_dpp](https://github.com/nix1947/sunway_dpp/tree/master/JAVA_RMI_IV). It uses Pyro5 remote objects and a Pyro name server as the registry.

## Java-to-Python mapping

- `client/Product.java` and `server/Product.java` define the remote methods; `product.py` provides the exposed `Product` class with `get_name`, `get_description`, and `get_price`.
- `server/ProductImpl.java` implements the product fields and accessors; that implementation lives in `product.py`.
- `server/Server.java` creates and exports the four products and binds them in the Java RMI registry; `server.py` registers the Pyro5 objects with the name server.
- `client/Client.java` looks up the laptop and calls its methods; `client.py` looks up and displays all four registered products.
- `server/ServerImpl.java` is empty in the referenced Java repository and has no behavior to translate.

## Requirements

Python 3.10 or newer.

## Install

From this directory, in PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Open three terminals in this directory. Start the Pyro name server first:

```powershell
python -m Pyro5.nameserver -n 127.0.0.1 -p 9090
```

In the second terminal, start the product server:

```powershell
python server.py
```

In the third terminal, run the client:

```powershell
python client.py
```

The client prints the name, description, and price returned remotely for the laptop, mobile, bag, and charger. Keep the name server and product server running while the client connects. Use `Ctrl+C` to stop each service.

## Screenshots

For the submission screenshots, run the name server, then the product server and client. Arrange the product-server and client terminals so both outputs are readable in the same capture; the name server can remain in a separate terminal. The server output confirms the registered product names, and the client output shows the returned product data.

## Publish to GitHub

Create a public repository named `PYTHON_RMI_LAB`, then push this folder so the repository contains `product.py`, `server.py`, `client.py`, and `README.md` (and `requirements.txt`). The public repository URL is the link to submit.
