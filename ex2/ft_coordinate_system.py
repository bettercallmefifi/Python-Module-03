import math


def creat_3D_positions(x: int, y: int, z: int) -> tuple[int, int, int]:
    return (x, y, z)


def distance_3D(p1, p2) -> int:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )


def parse_coordinates(cooredinae_str):
    try:
        parts = cooredinae_str.split(",")
        pos = (int(parts[0])), int(parts[1]), (int(parts[2]))
        return pos
    except Exception as e:
        print("Error parsing coordinates:", e)
        print(
            "Error details - Type:", type(e).__name__, ",Args", e.args
        )
        return None


def unpack_position(pos):
    x, y, z = pos
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main():
    print("=== Game Coordinate System ===\n")
    pos1 = creat_3D_positions(10, 20, 5)
    print("Position created:", pos1)
    print(
        "Distance between (0, 0, 0) and "
        f"{pos1}: {distance_3D((0, 0, 0), pos1):.2f}\n"
    )

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    pos2 = parse_coordinates(coord_str)

    if pos2:
        print("Parsed position:", pos2)
        print(
            "Distance between (0, 0, 0) and "
            f"{pos2}: {distance_3D((0, 0, 0), pos2):.1f}\n"
        )
    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    parse_coordinates(invalid_str)
    print()

    if pos2:
        unpack_position(pos2)


if __name__ == "__main__":
    main()
