import pygame
import random
import numpy as np
import time

arrayLength = int(input("Enter the length of the array: "))
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithm Visualizer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 24)

def generate_array(size):
    return random.choices(range(10, height - 10), k=size)

def draw_array(arr, red_bars=None, time_elapsed=0, iterations=0):
    screen.fill(WHITE)
    bar_width = width // len(arr)
    for i, value in enumerate(arr):
        color = RED if red_bars and i in red_bars else BLACK
        pygame.draw.rect(screen, color, (i * bar_width, height - value, bar_width, value))
    time_text = font.render(f"Time: {time_elapsed:.2f}s", True, BLACK)
    iter_text = font.render(f"Iterations: {iterations}", True, BLACK)
    screen.blit(time_text, (10, 10))
    screen.blit(iter_text, (10, 40))
    pygame.display.flip()

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    iterations = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                iterations += 1
                time_elapsed = time.time() - start_time
                draw_array(arr, [j, j + 1], time_elapsed, iterations)
                pygame.time.delay(10)

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def bogosort(arr):
    start_time = time.time()
    iterations = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        iterations += 1
        time_elapsed = time.time() - start_time
        draw_array(arr, time_elapsed=time_elapsed, iterations=iterations)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.time.delay(10)
    pygame.time.delay(100)

def main():
    array = generate_array(arrayLength)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_array(array)
        pygame.time.delay(500)
        bubble_sort(array)
        if not pygame.get_init():
            break
        pygame.time.delay(1000)
        array = generate_array(arrayLength)
    pygame.quit()

if __name__ == "__main__":
    main()
