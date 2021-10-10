import pygame


class Sprite(object):
    def __init__(self, image_path: str):
        self.image = pygame.image.load(image_path).convert()

    def get_sprites(self, rectangle, cannon=False) -> pygame.Surface:
        rect = pygame.Rect(rectangle)
        if cannon:
            temp_rect = rect.copy()
            temp_rect.width = temp_rect.width * 2
            image = pygame.Surface(temp_rect.size).convert()
            image.blit(self.image, (temp_rect.width // 2, 0), rect)
        else:
            image = pygame.Surface(rect.size).convert()
            image.blit(self.image, (0, 0), rect)

        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def get_sheet(self) -> pygame.Surface:
        return self.image
