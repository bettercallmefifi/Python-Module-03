import sys


def test_commands(args):
    length = len(args)
    print("=== Command Quest ===")
    if length == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
    else:
        print(f"Program name: {args[0]}")
        print(f"Arguments received: {length - 1}")
        for i in range(1, length):
            print(f"Argument {i}: {args[i]}")
    print(f"Total arguments: {length}")


if __name__ == "__main__":
    test_commands(sys.argv)
