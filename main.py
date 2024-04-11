import pygame
import asyncio
# Inicjalizacja Pygame
# pygame.init()

# Ustawienia okna
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Niebieskie tło w Pygame")
abc = pygame.image.load("img/map_test.png")
# Kolory
BLUE = (0, 0, 255)  # Składniki RGB: czerwony, zielony, niebieski

# Główna pętla gry
async def main():
    running = True
    while running:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Wypełnienie tła kolorem niebieskim
        WINDOW.fill(BLUE)
        WINDOW.blit(abc, (0, 0))
        # Aktualizacja ekranu
        pygame.display.update()
        await asyncio.sleep(0)
    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
