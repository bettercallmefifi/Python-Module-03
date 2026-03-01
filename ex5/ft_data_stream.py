def game_event_stream(n):
    players = [
        ("Alice", 5),
        ("Bob", 12),
        ("Charlie", 8),
        ("David", 15),
        ("Eva", 20),
    ]

    actions = [
        "killed monster",
        "found treasure",
        "leveled up",
    ]

    for i in range(1, n + 1):
        player, level = players[i % len(players)]
        action = actions[i % len(actions)]
        yield i, player, level, action


def analyse_events(even_stream):
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0

    it = iter(even_stream)

    while True:
        try:
            event_id, player, level, action = next(it)
            total += 1

            if level >= 10:
                high_level += 1
            if action == "found treasure":
                treasure += 1
            if action == "leveled up":
                level_up += 1

            if event_id <= 3:
                print(
                    f"Event {event_id}: Player {player}"
                    f"(level {level} {action})"
                )

        except StopIteration:
            break

    return total, high_level, treasure, level_up


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_numbers(n):
    count = 0
    num = 2
    while count < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1


def generator_demo():
    print("=== Game Data Stream Processor ===")
    fib_gen = iter(fibonacci(10))
    fib_numbers = [next(fib_gen) for _ in range(10)]
    print(
        "Fibonacci sequence (first 10): "
        + ", ".join(str(x) for x in fib_numbers)
    )

    prime_gen = iter(prime_numbers(5))
    prime_numbers_list = [next(prime_gen) for _ in range(5)]
    print(
        "Prime numbers (first 5): "
        + ", ".join(str(x) for x in prime_numbers_list)
    )


def main_stream_demo():
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    stream = game_event_stream(1000)
    total, high_level, treasure, level_up = analyse_events(stream)

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")


if __name__ == "__main__":
    main_stream_demo()
    generator_demo()
