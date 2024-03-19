class EatingCompetition:
    FOOD_POINTS = {
        "chickenwings": 5,
        "hamburgers": 3,
        "hotdogs": 2
    }

    def __init__(self, participants):
        self.participants = participants

    def calculate_score(self, participant):
        score = 0
        for food, points in self.FOOD_POINTS.items():
            if food in participant:
                score += points * participant[food]
        return score

    def generate_scoreboard(self):
        scoreboard = []
        for participant in self.participants:
            score = self.calculate_score(participant)
            scoreboard.append({"name": participant["name"], "score": score})

        scoreboard.sort(key=lambda x: (-x["score"], x["name"]))
        return scoreboard


participants = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

competition = EatingCompetition(participants)
scoreboard = competition.generate_scoreboard()
print(scoreboard)
