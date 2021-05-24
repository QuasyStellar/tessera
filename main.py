from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
import random
import string
from random import randint

Builder.load_string("""
<MainMenu>:
    BoxLayout:
        Button:
            text: 'Проверить пароль на надежность'
            on_press: root.manager.current = 'check'
            background_color: (2.5, 2.5, 0, 1)
            color: (0, 0, 0, 1)
        Button:
            text: 'Создать случайный пароль'
            on_press: root.manager.current = 'create'
            background_color: (2.5, 2.5, 0, 1)
            color: (0, 0, 0, 1)
<PassWordCreate>:
    label_widget1: label1
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Вернуться'
            on_press: root.manager.current = 'mainmenu'
            background_color: (2.5, 2.5, 0, 1)
            color: (0, 0, 0, 1)
        Button:
            text: 'Создать пароль со спец. символами'
            on_press: 
                root.password_creator()
            background_color: (2.5, 2.5, 0, 1)
            color: (0, 0, 0, 1)
        Button:
            text: 'Создать пароль без спец. символов'
            on_press: 
                root.password_creator1()
            background_color: (2.5, 2.5, 0, 1)
            color: (0, 0, 0, 1)
        Label:
            id: label1
            text: " "

<PassWordChecker>:
    password: text_input
    label_widget: label
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Вернуться'
            on_press: root.manager.current = 'mainmenu'
            background_color: (2.5, 2.5, 0, 1)
            color: (0, 0, 0, 1)
        TextInput:
            id: text_input
        Label:
            id: label
            text: 'Введите пароль в строку выше и нажмите "Проверить"'
            background_color: (0, 0, 0, 1)
            canvas.before:
                Color:
                    rgba: self.background_color
                Rectangle:
                    size: self.size
                    pos: self.pos
        Button:
            text: 'Проверить'
            on_press:
                root.change_text()
            background_color: (2.5, 2.5, 0, 1)
            color: (0, 0, 0, 1)
""")


class MainMenu(Screen):
    pass


class PassWordCreate(Screen):
    def password_creator1(self):
        password = string.ascii_letters + string.digits
        a = "".join(random.choice(password) for i in range(randint(8, 16)))
        self.label_widget1.text = a

    def password_creator(self):
        password = string.ascii_letters + string.digits + string.punctuation
        a = "".join(random.choice(password) for i in range(randint(8, 16)))
        self.label_widget1.text = a

    pass


class PassWordChecker(Screen):
    def change_text(self):
        file = open("passwords_list.txt", "r")
        text = file.read()
        if self.password.text in text:
            self.label_widget.text = 'Это пароль был найден в списке паролей. Придумайте новый или воспользуйтесь генератором паролей'
            self.label_widget.background_color = (1, 0, 0, 1)
            self.label_widget.color = (0, 0, 0, 1)
        else:
            self.label_widget.text = "Пароль не найден в списке популярных паролей, доп. действий не требуется."
            self.label_widget.background_color = (0, 1, 0, 1)
            self.label_widget.color = (0, 0, 0, 1)

    pass


class TestApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='mainmenu'))
        sm.add_widget(PassWordCreate(name='create'))
        sm.add_widget(PassWordChecker(name='check'))

        return sm


if __name__ == '__main__':
    TestApp().run()