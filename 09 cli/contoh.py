import typer

def main():
    """ CLI program """
    hello = "Hello"
    name = input("What is your name? ")

    print(f"{hello}, {name}!")

if __name__ == "__main__":
    typer.run(main)