import pygame
import time

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temporizador Pomodoro")

# Colores
RED = (200, 50, 50)
GREEN = (50, 200, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

# Fuente
font = pygame.font.Font(None, 48)
button_font = pygame.font.Font(None, 36)

# Estados del temporizador
WORK_TIME = 25 * 60  # 25 minutos
BREAK_TIME = 5 * 60  # 5 minutos
time_left = WORK_TIME
running = False
is_break = False
last_time = time.time()

# Definir botones (x, y, ancho, alto)
start_button = pygame.Rect(50, 200, 140, 50)
reset_button = pygame.Rect(210, 200, 140, 50)

def format_time(seconds):
    """Convierte los segundos en formato MM:SS."""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def draw_button(rect, text, color):
    """Dibuja un botón con texto."""
    pygame.draw.rect(screen, color, rect, border_radius=10)
    text_surface = button_font.render(text, True, BLACK)
    screen.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2,
                               rect.y + (rect.height - text_surface.get_height()) // 2))

# Loop principal
running_program = True
while running_program:
    screen.fill(GREEN if is_break else RED)

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_program = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start_button.collidepoint(x, y):
                running = not running  # Iniciar/Pausar
                last_time = time.time()  # Reiniciar tiempo base para evitar saltos
            if reset_button.collidepoint(x, y):
                time_left = WORK_TIME
                is_break = False
                running = False

    # Lógica del temporizador
    if running:
        current_time = time.time()
        elapsed = current_time - last_time
        last_time = current_time  # Actualizar el tiempo de referencia
        time_left -= int(elapsed)

        if time_left <= 0:
            is_break = not is_break
            time_left = BREAK_TIME if is_break else WORK_TIME
            pygame.mixer.Sound("alert.wav").play()  # Reproducir sonido de alerta

    # Renderizar tiempo
    text = font.render(format_time(time_left), True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Dibujar botones
    draw_button(start_button, "Iniciar" if not running else "Pausar", GRAY)
    draw_button(reset_button, "Reiniciar", GRAY)

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
