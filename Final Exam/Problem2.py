# Roy Aad

class AUBFL:
    def __init__(self, Teams):
        assert type(Teams) is list, "Invalid Input!"
        
        for element in Teams:
            assert type(element) is str, "Invalid Input!"

        self.Points = {team: 0 for team in Teams}

    def __str__(self):
        s = ""
        for team, points in self.Points.items():
            s += f"{team}: {points}\n"
        return s

    def play(self, team1, team2, score1, score2):
        assert team1 in self.Points, "Invalid Input!"
        assert team2 in self.Points, "Invalid Input!"

        assert type(score1) is int, "Invalid Input!"
        assert type(score2) is int, "Invalid Input!"

        if score1 > score2:
            self.Points[team1] += 3
        elif score1 < score2:
            self.Points[team2] += 3
        else:
            self.Points[team1] += 1
            self.Points[team2] += 1

    def add(self, team):
        assert team not in self.Points, "Invalid Input!"
        self.Points[team] = 0

    def winner(self):
        winner_team = "No Winner"
        winner_score = -1
        for team, score in self.Points.items():
            if score > winner_score:
                winner_team = team
                winner_score = self.Points[team]
            elif score == winner_score:
                winner_team = "No Winner"
        return winner_team

League = AUBFL(["CSE", "CIVE", "PremedStudentSociety"])
print(League)
League.play("CSE", "PremedStudentSociety", 3, 2)
print(League)
League.add("OSB")
print(League)
League.play("CIVE", "OSB", 1, 1)
print(League)
League.play("OSB", "CSE", 1, 1)
print(League)
League.play("CIVE", "CSE", 1, 1)
print(League)
League.play("CIVE", "OSB", 2, 1)
print(League)
print("The winner is " + League.winner())