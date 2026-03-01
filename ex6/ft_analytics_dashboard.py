players_data = [
    {
        "name": "alice",
        "score": 2300,
        "achievements": ["first_kill", "level_10", "boss_slayer"],
        "region": "north",
    },
    {
        "name": "bob",
        "score": 1800,
        "achievements": ["first_kill", "level_5"],
        "region": "east",
    },
    {
        "name": "charlie",
        "score": 2150,
        "achievements": ["level_10", "boss_slayer", "treasure_hunter"],
        "region": "central",
    },
    {
        "name": "diana",
        "score": 2050,
        "achievements": ["first_kill", "level_10", "speed_runner"],
        "region": "north",
    },
]


print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")

high_scorers = [p["name"] for p in players_data if p["score"] > 2000]
print("High scorers (>2000):", high_scorers)

scores_doubled = [p["score"] * 2 for p in players_data]
print("Scores doubled:", scores_doubled)

active_players = [
    p["name"]
    for p in players_data
    if len(p["achievements"]) > 0
]
print("Active players:", active_players)
print()

print("=== Dict Comprehension Examples ===")

player_scores = {p["name"]: p["score"] for p in players_data}
print("Player scores:", player_scores)

score_categories = {
    "high": len([p for p in players_data if p["score"] > 2100]),
    "medium": len([p for p in players_data if 2000 <= p["score"] <= 2100]),
    "low": len([p for p in players_data if p["score"] < 2000]),
}
print("Score categories:", score_categories)

achievement_counts = {p["name"]: len(p["achievements"]) for p in players_data}
print("Achievement counts:", achievement_counts)
print()

print("=== Set Comprehension Examples ===")

unique_players = {p["name"] for p in players_data}
print("Unique players:", unique_players)

unique_achievements = {ach for p in players_data for ach in p["achievements"]}
print("Unique achievements:", unique_achievements)

active_regions = {p["region"] for p in players_data}
print("Active regions:", active_regions)
print()

print("=== Combined Analysis ===")

total_players = len(unique_players)
total_achievements = len(unique_achievements)
average_score = sum(p["score"] for p in players_data) / total_players

top_performer = max(players_data, key=lambda p: p["score"])

print("Total players:", total_players)
print("Total unique achievements:", total_achievements)
print(f"Average score: {average_score:.1f}")
print(
    f"Top performer: {top_performer['name']} "
    f"({top_performer['score']} points, "
    f"{len(top_performer['achievements'])} achievements)"
)
