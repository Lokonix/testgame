import pygame
import asyncio
# Inicjalizacja Pygame
# pygame.init()

# Ustawienia okna
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Niebieskie tło w Pygame")

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

        # Aktualizacja ekranu
        pygame.display.update()
        asyncio.sleep(0)
    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
