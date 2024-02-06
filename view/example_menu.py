import pygame
import pygame_menu

pygame.init()

# Fenstergröße festlegen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menü am oberen Rand")

# Funktionen für Menüaktionen
def on_start_selected():
    print("Spiel starten")

def on_options_selected():
    print("Optionen anzeigen")

def on_quit_selected():
    pygame.quit()
    exit()

# Hauptmenü erstellen
menu_theme = pygame_menu.themes.THEME_BLUE.copy()
menu_theme.title_offset = (5, -2)
menu_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
menu_theme.widget_offset = (0, 0.1)

main_menu = pygame_menu.Menu('', screen_width, 100, theme=menu_theme, column_min_width=screen_width / 3, rows=1, columns=3)

# Menüpunkte hinzufügen
main_menu.add.button('Spiel starten', on_start_selected)
main_menu.add.button('Optionen', on_options_selected)
main_menu.add.button('Beenden', on_quit_selected)

# Das Menü am oberen Rand des Fensters zeichnen
main_menu._menubar.set_position(0, 0)

# Hauptschleife
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    screen.fill((40, 40, 40))  # Hintergrundfarbe des Fensters

    main_menu.update(events)
    main_menu.draw(screen)

    pygame.display.flip()