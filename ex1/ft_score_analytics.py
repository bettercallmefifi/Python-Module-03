import sys


def ft_score_analytics(args):
    print("=== Player Score Analytics ===")
    lenght = len(args)
    score = []

    if len(args) == 0:
        print(
            "No scores provided. Usage: python3"
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return

    try:
        averange = 0
        totale_score = 0

        i = 1
        while i < lenght:
            num = int(args[i])
            score.append(num)
            averange += num
            totale_score += num
            i += 1

        averange /= (len(score))
        maxscore = max(score)
        minscore = min(score)
        score_range = maxscore - minscore

        print(f"Scores processed: {score}")
        print(f"Total players: {lenght - 1}")
        print(f"Total score: {totale_score}")
        print(f"Average score: {averange:.1f}")
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
