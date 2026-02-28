import sys


def test_commands(args):
    lenght = len(args)
    print("=== Command Quest ===")
    if lenght == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {lenght - 1}")
        for i in range(1, lenght):
            print(f"Argument {i}: {args[i]}")
    print(f"Total argument: {lenght}")


if __name__ == "__main__":
    test_commands(sys.argv)
