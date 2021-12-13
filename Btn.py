import pygame
# Inspirat de: https://github.com/russs123/pygame_tutorials


class Btn:
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		position = pygame.mouse.get_pos()
		if self.rect.collidepoint(position):  # Hover + if clicked
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:  # [0] = click stanga, [1] = click pe
				# rotita, [2] = click dreapta
				self.clicked = True
				action = True
		if pygame.mouse.get_pressed()[0] == 0:  # [0] = click stanga, [1] = click pe rotita, [2] = click dreapta
			self.clicked = False
		surface.blit(self.image, (self.rect.x, self.rect.y))  # Desenam butonul
		return action
