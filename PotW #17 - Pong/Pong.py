#The bulk of this code is sourced from:
#https://www.geeksforgeeks.org/create-a-pong-game-in-python-pygame/


import pygame
pygame.init()


font = pygame.font.Font('freesansbold.ttf', 18)
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_green = (0, 255, 0)
color_red = (255, 0, 0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()	
fps = 30


class Striker:
	def __init__(self, xpos, ypos, width, height, speed, color):
		self.xpos = xpos
		self.ypos = ypos
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		
		self.object_rect = pygame.Rect(xpos, ypos, width, height)
		self.object_blit = pygame.draw.rect(screen, self.color, self.object_rect)

	def display(self):
		self.object_blit = pygame.draw.rect(screen, self.color, self.object_rect)

	def update(self, yfac):
		self.ypos = self.ypos + self.speed*yfac

		if self.ypos <= 0:
			self.ypos = 0
		elif self.ypos + self.height >= screen_height:
			self.ypos = screen_height-self.height

		self.object_rect = (self.xpos, self.ypos, self.width, self.height)

	def displayScore(self, text, score, x, y, color):
		text = font.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x, y)

		screen.blit(text, textRect)

	def getRect(self):
		return self.object_rect


class Ball:
	def __init__(self, xpos, ypos, radius, speed, color):
		self.xpos = xpos
		self.ypos = ypos
		self.radius = radius
		self.speed = speed
		self.color = color
		self.xfac = 0.8
		self.yfac = -0.8
		self.ball = pygame.draw.circle(screen, self.color, (self.xpos, self.ypos), self.radius)
		self.first_time = 1
	
	def display(self):
		self.ball = pygame.draw.circle(screen, self.color, (self.xpos, self.ypos), self.radius)
	
	def update(self):
		self.xpos += self.speed * self.xfac
		self.ypos += self.speed * self.yfac

		if self.ypos <= 0 or self.ypos >= screen_height:
			self.yfac *= -1

		if self.xpos <= 0 and self.first_time:
			self.first_time = 0
			return 1
		elif self.xpos >= screen_width and self.first_time:
			self.first_time = 0
			return -1
		else:
			return 0
	
	def reset(self):
		self.xpos = screen_width // 2
		self.ypos = screen_height // 2
		self.xfac *= -1
		self.first_time = 1
	
	def hit(self):
		self.xfac *= -1

	def getRect(self):
		return self.ball


def main():
	running = True

	player1 = Striker(20, screen_height//2-20, 10, 60, 10, color_white)
	player2 = Striker(screen_width-30, screen_height//2-20, 10, 60, 10, color_white)
	
	ball = Ball(screen_width//2, screen_height//2-20, 10, 10, color_white)

	list_of_players = [player1, player2]

	player1_score = 0
	player2_score = 0
	player1_yfac = 0
	player2_yfac = 0

	while running:
		screen.fill(color_black)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player2_yfac = -1
				if event.key == pygame.K_DOWN:
					player2_yfac = 1
				if event.key == pygame.K_w:
					player1_yfac = -1
				if event.key == pygame.K_s:
					player1_yfac = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					player2_yfac = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					player1_yfac = 0

		for player in list_of_players:
			if pygame.Rect.colliderect(ball.getRect(), player.getRect()):
				ball.hit()

		player1.update(player1_yfac)
		player2.update(player2_yfac)

		point = ball.update()

		if point == -1:
			player1_score += 1
		elif point == 1:
			player2_score += 1

		if point:
			ball.reset()

		player1.display()
		player2.display()
		ball.display()

		if player1_score > player2_score:
			color_player1 = color_green
			color_player2 = color_red
		elif player1_score < player2_score:
			color_player1 = color_red
			color_player2 = color_green
		else:
			color_player1 = color_white
			color_player2 = color_white

		player1.displayScore("PLAYER #1: ", player1_score, screen_width//2//2, 20, color_player1)
		player2.displayScore("PLAYER #2: ", player2_score, screen_width-screen_width//2//2, 20, color_player2)

		pygame.display.update()
		clock.tick(fps)


if __name__ == "__main__":
	main()
	pygame.quit()
