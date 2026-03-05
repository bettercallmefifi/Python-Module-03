import sys


def ft_score_analytics(args):
    print("=== Player Score Analytics ===")
    lenght = len(args)
    score = []

    if lenght <= 1:
        print(
            "No scores provided. Usage: python3"
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return

    try:
        average = 0
        total_score = 0

        i = 1
        while i < lenght:
            num = int(args[i])
            score.append(num)
            average += num
            total_score += num
            i += 1

        average /= (len(score))
        maxscore = max(score)
        minscore = min(score)
        score_range = maxscore - minscore

        print(f"Scores processed: {score}")
        print(f"Total players: {lenght - 1}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average:.1f}")
        print(f"High score: {maxscore}")
        print(f"Low score: {minscore}")
        print(f"Score range: {score_range}")

    except (ValueError, ZeroDivisionError):
        print(
            "No scores provided. Usage: python3"
            "ft_score_analytics.py <score1> <score2> ..."
        )


if __name__ == "__main__":
    ft_score_analytics(sys.argv)
