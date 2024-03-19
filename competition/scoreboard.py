class EatingCompetition:
    FOOD_POINTS = {
        "chickenwings": 5,
        "hamburgers": 3,
        "hotdogs": 2
    }

    def __init__(self, participants):
        """
        Initialize the EatingCompetition object with a list of participants.
        """
        self.participants = participants

    def calculate_score(self, participant):
        """
        Calculate the score for a given participant based on the amount of different foods consumed.
        Returns:
            int: The calculated score for the participant.
        """
        score = 0
        for food, points in self.FOOD_POINTS.items():
            if food in participant:
                score += points * participant[food]
        return score

    def generate_scoreboard(self):
        """
        Generate a scoreboard for the competition.
        """
        scoreboard = []
        for participant in self.participants:
            score = self.calculate_score(participant)
            scoreboard.append({"name": participant["name"], "score": score})

        scoreboard.sort(key=lambda x: (-x["score"], x["name"]))
        return scoreboard


# Test case where two participants have equal scores and are sorted alphabetically
participants = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11},
    {"name": "Alice", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11}
]

# Create an instance of the EatingCompetition class
competition = EatingCompetition(participants)

# Generate the scoreboard
scoreboard = competition.generate_scoreboard()

# Print the scoreboard
print(scoreboard)
