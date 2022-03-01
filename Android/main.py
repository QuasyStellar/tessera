# -*- coding: utf-8 -*-
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
import random
from kivy.config import Config
import string
import bcrypt
from random import randint
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from android.permissions import request_permissions, Permission
import pyAesCrypt
import os



rdir = "/mnt/sdcard/tessera"
if not os.path.isdir(rdir):
    os.mkdir(rdir)
if not os.path.isdir(rdir+"/assets"):
    os.mkdir(rdir+"/assets")
if not os.path.isdir(rdir+"/assets/passwords"):
    os.mkdir(rdir+"/assets/passwords")
f = open(rdir+"/assets/database.txt", 'a')
f.close()

files = open("/data/data/org.zhu.tessera/files/app/passwords_list.txt", "r")
file = files.read()
auth = "Не авторизован"
currentuser = " "
usepunctuation = 0
usenums = 0
randlenght = 0
usetall = 0
usesmall = 0

Builder.load_string("""
#: import Factory kivy.factory.Factory
<Passwordpop>:
    title: "Сохраненные пароли:"
    auto_dismiss: False
    pop: pop
    pop1: pop1
    size_hint:.85,.9
    BoxLayout:
        id: pop
        orientation: "vertical"
        on_parent: root.newbutton()
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            GridLayout:
                size_hint_y: None
                row_default_height: root.height*0.2
                height: self.minimum_height
                cols: 1
                id: pop1
        Button:
            size_hint: 1, .2
            font_size: 20
            text:"Вернуться"
            on_press: root.dismiss()

<acess@Popup>:
    title: "Подтверждение"
    size_hint: .8,.6
    BoxLayout:
        orientation: "vertical"
        Label:
            text:"Вы уверены, что хотите удалить все ваши сохраненные пароли?"
            font_size: 15
        Button:
            text: "Да"
            on_press: root.delete()
        Button:
            text: "Нет"
            on_press: root.dismiss()
            
<ResultPop@Popup>:
    title: "Результат:"
    size_hint: .8,.6
 
    
    

<LoginScreen>:
    password: password
    login: login
    BoxLayout:

        orientation: 'vertical'
        Button:
            text: 'Вернуться'

            on_press: root.manager.current = 'log'
            color: (1, 0, 0, 1)
            font_size: 30
            size_hint:1, .4
            
        Label:
            color: (1, 1, 1, 1)
            font_size: 32
            text: "Введите логин:"
            size_hint: 1, .4

        TextInput:
            foreground_color: (1, 1, 1, 1)
            multiline: False
            write_tab: False
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            background_color:(1,1,1,.4)
            focus: True
            on_text_validate: password.focus = True
            size_hint: 1, .3
            id: login
            font_size: 50

        
        Label:
            color: (1, 1, 1, 1)
            font_size: 32
            text: "Введите пароль:"
            size_hint: 1, .4
        TextInput:
            foreground_color: (1, 1, 1, 1)
            multiline: False
            id: password
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            write_tab: False
            on_text_validate: root.gainAccess()
            password: True
            font_size: 50
            background_color:(1,1,1,.4)
            size_hint: 1, .3
        
        Button:
            text: 'Войти'
            on_release: root.gainAccess()
            on_press: root.password.text =""
            color:  (0, 65, 0, 1)
            size_hint:
            font_size: 40

        
<Login>:
    currentuser: currentuser
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Вернуться'
            on_press: root.manager.current = 'logs'
            color: (1, 0, 0, 1)
            font_size: 32
        Button:
            id: currentuser
            text: 'Войти'
            on_press: root.manager.current = 'logsc'
            color: (1, 1, 1, 1)
            font_size: 32
        Button:
            text: 'Зарегистрироваться'
            on_press: root.manager.current = 'reg'
            color: (1, 1, 1, 1)
            font_size: 32
        

<Register>:
    reg: reg
    login: login
    password: password
    password1: password1
    BoxLayout:

        orientation: "vertical"
        Button:
            text: 'Вернуться'
            on_press: root.manager.current = 'log'
            color: (1, 0, 0, 1)
            font_size: 30
        Label:
            color: (1, 1, 1, 1)
            font_size: 30
            text: "Введите логин:"
            size_hint: 1,.4

        TextInput:
            foreground_color: (1, 1, 1, 1)
            multiline: False
            write_tab: False
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            background_color:(1,1,1,.4)
            on_text_validate: password.focus = True
            id: login
            font_size: 50
            size_hint: 1,.4
        Label:
            color: (1, 1, 1, 1)
            font_size: 30
            text: "Введите пароль:"
            size_hint: 1,.4

        TextInput:
            foreground_color: (1, 1, 1, 1)
            multiline: False
            write_tab: False
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            background_color:(1,1,1,.4)
            on_text_validate: password1.focus = True
            id: password
            password: True
            font_size: 50
            size_hint: 1,.4
        Label:
            color: (1, 1, 1, 1)
            font_size: 30
            text: "Подтвердите пароль:"
            size_hint: 1,.4

        TextInput:
            foreground_color: (1, 1, 1, 1)
            multiline:False
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            write_tab: False
            id: password1
            background_color:(1,1,1,.4)
            on_text_validate: root.register()
            font_size: 50
            password: True
            size_hint: 1,.4
        Button:
            id: reg
            text: 'Зарегистрироваться'
            on_release: root.register()
            on_press: root.password.text=""
            on_press: root.password1.text=""
            color: (0, 60, 0, 1)
            font_size: 40
    
    
    
<LoginS>:
    BoxLayout:
        orientation: 'vertical'


        Button:
            text: 'Войти/Зарегистрироваться'
            on_press: root.manager.current = 'log'
            color:  (1, 1, 1, 1)
            font_size: 35
      
    
        Button:
            text: '''Войти без авторизации'''
            on_press: root.manager.current = 'mainmenu' 
            on_press: root.non()
            color:  (1, 1, 1, 1)
            font_size: 35
<MainMenu>:
    BoxLayout:
        orientation: 'vertical'   
        Button:
            text: "Выйти"
            on_press: root.manager.current = 'logs'
            color: (1, 0, 0, 1)
            font_size: 40

        Button:
            id: text
            text: 'Проверить пароль'
            on_press: 
                root.manager.current="check"
            color:  (1, 1, 1, 1)
            font_size: 40
        Button:
            text: 'Сгенерировать пароль'
            on_press: root.manager.current = 'create'
            color:  (1, 1, 1, 1)
            font_size: 40
        Button:
            text: 'Сохраненные пароли'
            on_press: 
                Factory.Passwordpop().open()
            color:  (1, 1, 1, 1)
            font_size: 40
        

            





            
<PassWordCreate>:
    comm: comm
    colors: colors
    slideit: slider
    buttontall: ButtonTall
    buttonsmall: ButtonSmall
    buttonrand: ButtonRand
    buttonnu: ButtonNu
    buttonpu: ButtonPu
    label_widget1: label1
    BoxLayout:


        orientation: 'vertical'

        Button:
            text: 'Вернуться'
            on_press: root.manager.current = 'mainmenu'
            color: (1, 0, 0, 1)
            font_size: 20
        Label:
            id: label1
            color: (1, 1, 1, 1)
            font_size: 20

            text: "Напишите комментарий к паролю в строку ниже:"
            font_size: 20

        TextInput:
            foreground_color: (1, 1, 1, 1)
            id: comm
            background_color:(1,1,1,.4)
            font_size: 50
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            multiline: False
        Button:
            id: ButtonPu
            text: 'Использовать спец. символы'
            on_release: root.usepunctuations()
            color: (1, 1, 1, 1)
            font_size: 20
        Button:
            id: ButtonNu
            text: 'Использовать цифры'
            on_release: root.usenumss()
            color: (1, 1, 1, 1)
            font_size: 20
        Button:
            id: ButtonSmall
            text: 'Использовать строчные буквы'
            on_release: root.usesmall()
            color: (1, 1, 1, 1)
            font_size: 20
        Button:
            id: ButtonTall
            text: 'Использовать прописные буквы'
            on_release: root.usetall()
            color: (1, 1, 1, 1)
            font_size: 20
        Button:
            id: ButtonRand
            text: 'Случайная длина пароля'
            on_release: root.randlenghts()
            color: (1, 1, 1, 1)
            font_size: 20
        
        Label:
            id: colors
            color: (0, 100, 0, 1)
            font_size: 20
            
            text: "Длина пароля: "+str(slider.value)

        Slider:
            id: slider
            min: 8
            max: 30
            step: 1
            background_color:  (0,0,0,.85)


            
    
        TextInput:
            id: label1
            foreground_color: (1, 1, 1, 1)
            font_size: 20
            background_color:(1,1,1,.4)
            readonly: True
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            text: "Сгенерированный пароль будет здесь"
            size_hint: 1,.9
            font_size: 50

        Button:
            font_size: 18
            color: (0, 65, 0, 1)
            text: "Сохранить пароль(Сохраненный пароль нельзя удалить!)"
            on_release:
                root.savepassword()
        Button:
            text: 'Cгенерировать'
            on_press: root.password_creator()
            color: (0,65,0,1)
            font_size: 20



<Button@Button>:
    background_color:(0,0,0,1)
    background_normal: ""
    border_radius:[18]
    font_name: "/data/data/org.zhu.tessera/files/app/san.ttf"
    canvas.before:
        Color:
            rgba:(0,0,0,2)
        RoundedRectangle:
            size: self.width-30, self.height-30
            pos: self.x+15, self.y+15
<Label@Label>:
    background_color:(0,0,0,0)
    background_normal: ""
    font_name: "/data/data/org.zhu.tessera/files/app/san.ttf"
    border_radius:[18]
    canvas.before:
        Color:
            rgba:(1,1,1,.2)
        RoundedRectangle:
            size: self.width-30, self.height-30
            pos: self.x+15, self.y+15


        
            
        
<PassWordChecker>:
    password: text_input
    label_widget: label
    BoxLayout:


        orientation: 'vertical'
        Button:
            text: 'Вернуться'
            on_press: root.manager.current = 'mainmenu'
            color: (1, 0, 0, 1)
            font_size: 35
        TextInput:
            foreground_color: (1, 1, 1, 1)
            multiline: False
            padding_x:
                [self.center[0] - self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached) / 2.0,0] if self.text else [self.center[0], 0]
            padding_y: 
                [self.height / 2.0 - (self.line_height / 2.0) * len(self._lines), 0]
            background_color:(1,1,1,.4)
            on_text_validate: root.change_text()
            id: text_input
            font_size: 50
            
            
        Label:
            id: label
            text: 'Введите пароль в строку выше и нажмите "Проверить"'
            font_size: 35
            background_color: (0,0,0,.2)
            canvas.before:
                Color:
                    rgba: self.background_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
        Button:
            text: 'Проверить'
            on_press:
                root.change_text()
            color: (0, 65, 0, 1)
            font_size: 35

  
""")


class ResultPop(Popup):
    pass

class acess(Popup):
    def delete(self):
        os.remove(rdir+"/assets/passwords"+"/"+currentuser+".txt.crp")
        self.dismiss()
        show = ResultPop(title="Результат:", content=Label(text="Успешно!"))
        show.open()

    pass

class newbuttons(TextInput):
    pass

class button(Button):
    pass



class Passwordpop(Popup):
    def newbutton(self):
        global auth
        if auth == "Не авторизован":
            self.pop1.add_widget(Button(text = "Пароли отсутсвуют либо вы не авторизованы"), index=1)
        else:
            try:
                walking_by_dirs1(rdir+"/assets/passwords", password)
                file = open(rdir+"/assets/passwords" + "/" + currentuser + ".txt", 'r')
                f = file.readlines()
                for line in f:
                    butt = newbuttons(text=line.strip(), readonly=True)
                    self.pop1.add_widget(butt, index=1)
                buttn = button(text="Удалить весь список паролей", background_color=(230,0,0,1), color=(0,0,0,1))
                buttn.bind(on_press=self.result)
                self.pop1.add_widget(buttn, index=0)
                file.close()
                walking_by_dirs(rdir+"/assets/passwords", password)
            except:
                self.pop1.add_widget(Button(text = "Пароли отсутсвуют либо вы не авторизованы"))
    pass

    def delete(self, event):
        os.remove(rdir+"/assets/passwords"+"/"+currentuser+".txt.crp")
        self.dismiss()

    def result(self, event):
        show = acess(title="Подтверждение")
        show.open()
        self.dismiss()

password = currentuser


def encrypt(file, password):
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    os.remove(file)


def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                encrypt(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)


def decrypt(file, password):
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    os.remove(file)


def walking_by_dirs1(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decrypt(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

    # walking_by_dirs1("passwords", password)

    # walking_by_dirs("passwords", password)


class LoginScreen(Screen):
    def gainAccess(self, Username=None, Password=None):
        Username = self.login.text
        Password = self.password.text
        global currentuser
        global auth

        if not len(Username or Password) < 1:
            if True:
                db = open(rdir+"/assets/database.txt", "r")
                d = []
                f = []
                for i in db:
                    a, b = i.split(",")
                    b = b.strip()
                    c = a, b
                    d.append(a)
                    f.append(b)
                    data = dict(zip(d, f))
                try:
                    if Username in data:
                        hashed = data[Username].strip('b')
                        hashed = hashed.replace("'", "")
                        hashed = hashed.encode('utf-8')

                        try:
                            if bcrypt.checkpw(Password.encode(), hashed):
                                auth = "Авторизован"
                                self.show_pop6()
                                currentuser = self.login.text
                                self.manager.current = 'mainmenu'

                            else:
                                self.show_pop5()

                        except:
                            self.show_pop4()
                    else:
                        self.show_pop3()
                except:
                    self.show_pop2()
            else:
                self.show_pop1()

        else:
            self.show_pop()

    def show_pop(self):
        show = ResultPop(title="Результат:", content=Label(text="Произошла ошибка проверьте правильность данных"))
        show.open()

    def show_pop1(self):
        show = ResultPop(title="Результат:", content=Label(text="Произошла ошибка проверьте правильность данных"))
        show.open()

    def show_pop2(self):
        show = ResultPop(title="Результат:", content=Label(text="Пароля или логина нет в системе"))
        show.open()

    def show_pop3(self):
        show = ResultPop(title="Результат:", content=Label(text="Логин отсутсвует в системе"))
        show.open()

    def show_pop4(self):
        show = ResultPop(title="Результат:", content=Label(text="Неправильный пароль или логин"))
        show.open()

    def show_pop5(self):
        show = ResultPop(title="Результат:", content=Label(text="Неправильный пароль"))
        show.open()

    def show_pop6(self):
        show = ResultPop(title="Результат:", content=Label(text="Успешный вход!"))
        show.open()

    pass


class Register(Screen):
    def register(self, Username=None, Password1=None, Password2=None):
        Username = self.login.text
        Password1 = self.password.text
        Password2 = self.password1.text
        global auth
        global file
        global currentuser
        db = open(rdir+"/assets/database.txt", "r")
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            c = a, b
            d.append(a)
            f.append(b)
            data = dict(zip(d, f))
        if not len(Password1) < 8:
            db = open(rdir+"/assets/database.txt", "r")
            if not Username == None:
                if len(Username) < 1:
                    self.show_pop5()

                elif Username in d:
                    self.show_pop4()

                else:
                    if self.password.text in file:
                        self.show_pop3()

                    else:
                        if Password1 == Password2:
                            Password1 = Password1.encode('utf-8')
                            Password1 = bcrypt.hashpw(Password1, bcrypt.gensalt())

                            db = open(rdir+"/assets/database.txt", "a")
                            db.write(Username + ", " + str(Password1) + "\n")
                            self.show_pop2()
                            currentuser = Username
                            auth = "Авторизован"
                            self.manager.current = "mainmenu"

                        else:
                            self.show_pop1()


        else:
            self.show_pop()

    def show_pop(self):
        show = ResultPop(title="Результат:", content=Label(text="Пароль слишком короткий"))
        show.open()

    def show_pop1(self):
        show = ResultPop(title="Результат:", content=Label(text="Пароли не совпадают"))
        show.open()

    def show_pop2(self):
        show = ResultPop(title="Результат:",
                         content=Label(text="Вы успешно зарегистрировались!\nВход выполнен!"))
        show.open()

    def show_pop3(self):
        show = ResultPop(title="Результат:", content=Label(text="Пароль не является надежным"))
        show.open()

    def show_pop4(self):
        show = ResultPop(title="Результат:", content=Label(text="Логин уже зарегистрирован"))
        show.open()

    def show_pop5(self):
        show = ResultPop(title="Результат:", content=Label(text="Введите логин"))
        show.open()

    pass


class Login(Screen):
    pass


class LoginS(Screen):
    def non(self):
        global auth
        auth = "Не авторизован"

    pass


class MainMenu(Screen):
    pass


class PassWordCreate(Screen):

    def usepunctuations(self):
        global usepunctuation
        if usepunctuation == 0:
            self.buttonpu.color = (0, 100, 0, 1)
            usepunctuation += 1
        else:
            self.buttonpu.color = (1, 1, 1, 1)
            usepunctuation -= 1

    def usenumss(self):
        global usenums
        if usenums == 0:
            self.buttonnu.color = (0, 100, 0, 1)
            usenums += 1
        else:
            self.buttonnu.color = (1, 1, 1, 1)
            usenums -= 1

    def randlenghts(self):
        global randlenght
        if randlenght == 0:
            self.buttonrand.color = (0, 100, 0, 1)
            randlenght += 1
            self.colors.color = (1, 1, 1, 1)
            self.slideit.disabled = True
        else:
            self.buttonrand.color = (1, 1, 1, 1)
            randlenght -= 1
            self.colors.color = (0,100,0,1)
            self.slideit.disabled = False

    def usesmall(self):
        global usesmall
        if usesmall == 0:
            self.buttonsmall.color = (0, 100, 0, 1)
            usesmall += 1
        else:
            self.buttonsmall.color = (1, 1, 1, 1)
            usesmall -= 1

    def usetall(self):
        global usetall
        if usetall == 0:
            self.buttontall.color = (0, 100, 0, 1)
            usetall += 1
        else:
            self.buttontall.color = (1, 1, 1, 1)
            usetall -= 1


    def password_creator(self, password=""):

        global usepunctuation
        global usenums
        global randlenght
        global usetall
        global usesmall
        if usepunctuation == 0 and usenums == 0 and usetall == 0 and usesmall == 0:
            self.label_widget1.text = """Выберите хотя бы один параметр, 
влияющий на содержание пароля!"""
        else:
            if usepunctuation == 1:
                password += string.punctuation
            else:
                pass
            if usenums == 1:
                password += string.digits
            else:
                pass
            if usetall == 1:
                password += string.ascii_uppercase
            else:
                pass
            if usesmall == 1:
                password += string.ascii_lowercase
            else:
                pass
            if randlenght == 1:
                passw = "".join(random.SystemRandom().choice(password) for i in range(randint(8, 16)))
                self.label_widget1.text = passw

            else:
                passw = "".join(random.SystemRandom().choice(password) for i in range(self.slideit.value))
                self.label_widget1.text = passw

    def savepassword(self):
        global auth
        if "Не авторизован" == auth:
            self.label_widget1.text = "Вы не авторизованы, войдите чтобы сохранять пароли"
        else:
            if self.label_widget1.text == "Сгенерированный пароль будет здесь":
                self.label_widget1.text = """Выберите хотя бы один параметр, 
влияющий на содержание пароля!"""
            elif self.label_widget1.text == """Выберите хотя бы один параметр, 
влияющий на содержание пароля!""":
                self.label_widget1.text = """Выберите хотя бы один параметр, 
влияющий на содержание пароля!"""
            elif self.label_widget1.text == "Пароль сохранен":
                self.label_widget1.text = "Пароль сохранен"
            elif self.label_widget1.text == "Вы не авторизованы, войдите чтобы сохранять пароли":
                self.label_widget1.text = "Вы не авторизованы, войдите чтобы сохранять пароли"

            else:
                try:
                    walking_by_dirs1(rdir+"/assets/passwords", password)
                    file = open(rdir+"/assets/passwords" + "/" + currentuser + ".txt", 'r')
                    text = file.read()
                    if self.label_widget1.text in text:
                        self.label_widget1.text = "Пароль сохранен"
                    else:
                        file = open(rdir+"/assets/passwords" + "/" + currentuser + ".txt", 'a+')
                        file.write("\n" + "Комментарий: " + self.comm.text + " Пароль: " + self.label_widget1.text)
                        self.label_widget1.text = "Пароль сохранен"
                        file.close()
                        walking_by_dirs(rdir+"/assets/passwords", password)
                except:
                    file = open(rdir+"/assets/passwords" + "/" + currentuser + ".txt", 'w+')
                    file.write("Комментарий: " + self.comm.text + " Пароль: " + self.label_widget1.text)
                    self.label_widget1.text = "Пароль сохранен"
                    file.close()
                    walking_by_dirs(rdir+"/assets/passwords", password)

    pass


class PassWordChecker(Screen):
    def change_text(self):
        global file
        if self.password.text in file:
            self.label_widget.text = '''Это пароль был найден в базе уязвимых паролей.
Придумайте новый 
или 
воспользуйтесь генератором паролей'''
            self.label_widget.background_color = (1, 0, 0, 1)
            self.label_widget.color = (0, 0, 0, 1)
        else:
            self.label_widget.text = """Пароль не найден в базе уязвимых паролей"""
            self.label_widget.background_color = (0, 1, 0, 1)
            self.label_widget.color = (0, 0, 0, 1)

    pass


class TestApp(App):

    def build(self):
        Window.clearcolor = (0,0,0,1)
        sm = ScreenManager()
        sm.add_widget(LoginS(name='logs'))
        sm.add_widget(LoginScreen(name='logsc'))
        sm.add_widget(Register(name='reg'))
        sm.add_widget(Login(name='log'))
        sm.add_widget(MainMenu(name='mainmenu'))
        sm.add_widget(PassWordCreate(name='create'))
        sm.add_widget(PassWordChecker(name='check'))
        return sm


if __name__ == '__main__':
    TestApp().run()

