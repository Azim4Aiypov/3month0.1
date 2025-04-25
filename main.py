import flet as ft
from datetime import datetime
import random

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text("Hello world!")

    HISTORY_FILE = "history.txt"
    greeting_history = []
    history_visible = True
    random_names = ["Алексей", "Мария", "Иван", "Ольга", "Наталья", "Дмитрий", "Светлана", "Егор", "Анна"]

    def load_history():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    name = line.strip()
                    if name:
                        greeting_history.append(name)
                history_text.value = 'История приветствий:\n' + "\n".join(greeting_history)
                page.update()
        except FileNotFoundError:
            pass

    def save_history():
        with open(HISTORY_FILE, 'w', encoding='utf-8') as file:
            for name in greeting_history:
                file.write(name + "\n")

    history_text = ft.Text("История приветствий:", size="bodyMedium")

    def set_greeting_color():
        hour = datetime.now().hour
        if 6 <= hour < 12:
            greeting_text.color = ft.colors.YELLOW
        elif 12 <= hour < 18:
            greeting_text.color = ft.colors.ORANGE
        elif 18 <= hour < 24:
            greeting_text.color = ft.colors.RED
        else:
            greeting_text.color = ft.colors.BLUE

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            greeting_text.value = f"Привет, {name}!"
            greet_button.text = "Поздороваться снова"
            name_input.value = ""

            greeting_history.append(name)
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            save_history()
            set_greeting_color()
        else:
            greeting_text.value = 'Пожалуйста, введите имя ❌'
            greeting_text.color = ft.colors.BLACK

        page.update()

    name_input = ft.TextField(
        label="Введите имя",
        autofocus=True,
        on_submit=on_button_click
    )

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def insert_random_name(_):
        name_input.value = random.choice(random_names)
        page.update()

    def toggle_history(_):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        toggle_history_button.text = "Скрыть историю" if history_visible else "Показать историю"
        page.update()

    theme_button = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_6,
        tooltip='Сменить тему',
        on_click=toggle_theme
    )

    greet_button = ft.ElevatedButton(
        'Поздороваться',
        on_click=on_button_click,
        icon=ft.icons.HANDSHAKE
    )

    clear_button = ft.TextButton(
        "Очистить историю",
        icon=ft.icons.DELETE_SWEEP,
        on_click=clear_history
    )

    clear_button_2 = ft.IconButton(
        icon=ft.icons.DELETE,
        tooltip='Очистить историю',
        on_click=clear_history
    )

    random_name_button = ft.ElevatedButton(
        "Случайное имя",
        icon=ft.icons.SHUFFLE,
        on_click=insert_random_name
    )

    toggle_history_button = ft.TextButton(
        text="Скрыть историю",
        icon=ft.icons.HISTORY,
        on_click=toggle_history
    )

    load_history()

    page.add(
        ft.Row([theme_button, clear_button, clear_button_2], alignment=ft.MainAxisAlignment.CENTER),
        greeting_text,
        name_input,
        ft.Row([greet_button, random_name_button], alignment=ft.MainAxisAlignment.CENTER),
        toggle_history_button,
        history_text
    )

ft.app(main)
