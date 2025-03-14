import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    
   
    greeting_text = ft.Text("Привет, мир!")

  
    greeting_history = []

    history_text = ft.Text("История приветствий:", style='bodyMedium')

   
    def get_greeting(name):
        
        current_hour = datetime.now().hour

        
        if 6 <= current_hour < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= current_hour < 18:
            return f"Добрый день, {name}!"
        elif 18 <= current_hour < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"

   
    def on_button_click(e):
        name = name_input.value.strip()

        if name:
          
            greeting_text.value = get_greeting(name)
            greet_button.text = 'Поздороваться снова'
            name_input.value = ''

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp}: {greeting_text.value}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"

        page.update()

   
    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True, on_submit=on_button_click)

 
    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()
    
   
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

   
    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)
    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)
    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистить", on_click=clear_history)

   
    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)

    
    page.add(
        ft.Row([theme_button, clear_button, clear_button_icon], alignment=ft.MainAxisAlignment.CENTER), 
        greeting_text, 
        name_input, 
        greet_button,
        history_text
    )

    
    page.update()

ft.app(target=main)