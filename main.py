import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f"Game exited. Your score: {score}")
                return

        screen.fill("black")
        dt = clock.tick(60) / 1000
        for thing in drawable:
            thing.draw(screen)
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print(f"Game over! Your score: {score}")
                sys.exit(0)
            for shot in shots:
                if asteroid.check_collision(shot):
                    score += asteroid.split()
                    shot.kill()
                    print(f"Debug: score is now {score}")

        pygame.display.flip()


if __name__ == "__main__":
    main()
