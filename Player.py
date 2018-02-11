import numpy as np

class Player:
	def __init__(self):
		self.scores = []

	def addScore(self, score):
		self.scores.append(score)

	def averageScore(self):
		return np.mean(self.scores)

	def timesPlayed(self):
		return len(self.scores)