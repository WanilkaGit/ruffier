"""Імпорта"""
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from instr import*

Window.clearcolor = (0.1, 0.0, 0.0, 0.8)

"""ЗМІНННІ"""
name = ""
age = ""
puls = ""
work = "Вище середнього"

"""Класи"""
class FirstScreen(Screen):# тут прописаний перший клас/екран
    global name, age
    def __init__(self, **kwargs):# тут можна писати скільки хочеш аргументів
        super().__init__(**kwargs)# копіюємо кістяк супер класу також
        introduce = Label(text=txt_instruction)#споочатку створюємо обєкти першого екрану першим буде надпис привітальна інструкція

        name_lbl = Label(text="Введіть своє ім'я")# тут робимо підсказку для людей
        self.name_input = TextInput(multiline=False)# тут робимо поле для вводу
        name = self.name_input.text
        
        age_lbl = Label(text="Введіть ваш вік >=7")# тут щоб люди змогли вписати вік підсказка
        self.age_input = TextInput(multiline=False)#можливість вводу
        age = self.age_input.text

        self.btn_start = Button(text="Почати", size_hint=(1, 0.1), pos_hint={"center_x": 0.5}, background_color=(1, 0.0, 0.28, 1))#тут прописуємо кнопку
        self.btn_start.on_press = self.next# щоб працювала функції при натискані та відношення до функції переходу на наступний екран "некст"

        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")# створюємо лінії для роозміщення
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")# то була для розміщення підсказки  та можливості вводу імені ця для віку

        line1.add_widget(name_lbl)# тут розміщаємо полініях підсказку
        line1.add_widget(self.name_input)# тут поле вводу

        line2.add_widget(age_lbl)#тут так само але для віку
        line2.add_widget(self.age_input)

        line3 = BoxLayout(orientation="vertical", padding=10, spacing=50)# настраюємо лінію орієнтацію вертикальну та відступи між кнопками та лініями та так щоб вджети були як меньша коробка в більшій
        line3.add_widget(introduce)# додаємо все інше тут текст
        line3.add_widget(line1)# тут лінію імя
        line3.add_widget(line2)#тут лінію віку
        line3.add_widget(self.btn_start)#ту кнопку додаємо

        self.add_widget(line3)# тут на екран додаємо цб третю лінію

    def next(self):# прописуємо фунцію що буде працювати при нажатті на кнопку
        self.manager.current = "second"# вона має робити переключення на інший екран

class SecondScreen(Screen):# тут створюємо другий екран
    def __init__(self, **kwargs):#створюємо кістяк класу
        super().__init__(**kwargs)# копіюємо кістяк супер класу
        txt_rul = Label(text=txt_test1, size_hint=(1, 1), pos_hint={"center": 0.5})# пишемо інструкцію до другого екрану

        txt_time = Label(text="Прошло секунд: ", pos_hint={"center": 0.5})# знову текст що буде допомагати скільки ще потрібно працювати

        res_txt = Label(text="Введіть результат: ", pos_hint={"center": 0.5})# тут підскзку для того щоб людинка розумілла що там вводити
        self.res_input = TextInput(multiline=False, pos_hint={"center": 0.5})# те місце де потрібно вводити
        self.res_input.set_disabled(True)
        puls = self.res_input.text

        self.btn_next = Button(text="Далі", size_hint=(1, 0.191), background_color=(1, 0.0, 0.28, 1))# створюємо кнопочку
        self.btn_next.on_press = self.next#а також функцію нажимання на кнопку

        self.btn_before = Button(text="Назад", size_hint=(1, 0.191), background_color=(1, 0.0, 0.28, 1))# тут ще одна кнопка
        self.btn_before.on_press = self.before# що буде якщо нажати на неї


        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")# створюємо першу лінію
        line1.add_widget(res_txt)# розміщаємо підсказку що вводити
        line1.add_widget(self.res_input)# даємо поле вводу

        line2 = BoxLayout(padding = 1)#створюємо другу лінію
        line2.add_widget(self.btn_before)
        line2.add_widget(self.btn_next)


        line3 = BoxLayout(orientation="vertical", padding=10, spacing=10)# створюємо третю лінію
        line3.add_widget(txt_rul)
        line3.add_widget(txt_time)
        line3.add_widget(line1)
        line3.add_widget(line2)
        self.add_widget(line3)

    def next(self):# прописуємо фунції для двох кнопок
        self.manager.current = "third"# ереключення на натсупний екран

    def before(self):#переключення на минулий еккран
        self.manager.current = "first"# на минулий екран



class ThirdScreen(Screen):# класи для інших еранів
    def __init__(self, **kwargs):#створюємо кістяк класу
        super().__init__(**kwargs)# копіюємо кістяк супер класу
        half_sit_lbl = Label(text=txt_sits)
        self.next_btn = Button(text="Далі", size_hint=(1, 0.11), pos_hint={"center": 0.5}, background_color=(1, 0.0, 0.28, 1))
        self.next_btn.on_press = self.next
        self.before_btn = Button(text="Назад", size_hint=(1, 0.11), pos_hint={"center": 0.5}, background_color=(1, 0.0, 0.28, 1))
        self.before_btn.on_press = self.before

        line_for_btns = BoxLayout(padding=15)
        line_for_btns.add_widget(self.before_btn)
        line_for_btns.add_widget(self.next_btn)


        line1 = BoxLayout(orientation="vertical")
        line1.add_widget(half_sit_lbl)
        line1.add_widget(line_for_btns)
        self.add_widget(line1)

    def next(self):# прописуємо фунції для двох кнопок
        self.manager.current = "fourth"# ереключення на натсупний екран

    def before(self):#переключення на минулий еккран
        self.manager.current = "second"# на минулий екран

class FourthScreen(Screen):
    def __init__(self, **kwargs):# тут можна писати скільки хочеш аргументів
        super().__init__(**kwargs)# копіюємо кістяк супер класу також
        introduce = Label(text=txt_test3)#споочатку створюємо обєкти першого екрану першим буде надпис привітальна інструкці
        
        txt_puls = Label(text="Рахуйте пульс")
        txt_sec = Label(text="Пройшло секунд: ")

        result_lbl = Label(text="Введіть своє ім'я")# тут робимо підсказку для людей
        self.result = TextInput(multiline=False)# тут робимо поле для вводу
        
        
        result_aft_rest_lbl = Label(text="Введіть ваш вік >=7")# тут щоб люди змогли вписати вік підсказка
        self.result_aft_rest= TextInput(multiline=False)#можливість вводу
        

        self.btn_next = Button(text="Далі", size_hint=(1, 0.07), background_color=(1, 0.0, 0.28, 1))# створюємо кнопочку
        self.btn_next.on_press = self.next#а також функцію нажимання на кнопку

        self.btn_before = Button(text="Назад", size_hint=(1, 0.07), background_color=(1, 0.0, 0.28, 1))# тут ще одна кнопка
        self.btn_before.on_press = self.before# що буде якщо нажати на неї

        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")# створюємо лінії для роозміщення
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")# то була для розміщення підсказки  та можливості вводу імені ця для віку

        line1.add_widget(result_lbl)# тут розміщаємо полініях підсказку
        line1.add_widget(self.result)# тут поле вводу

        line2.add_widget(result_aft_rest_lbl)#тут так само але для віку
        line2.add_widget(self.result_aft_rest)

        line4 = BoxLayout()
        line4.add_widget(self.btn_before)
        line4.add_widget(self.btn_next)

        line3 = BoxLayout(orientation="vertical", padding=10, spacing=50)# настраюємо лінію орієнтацію вертикальну та відступи між кнопками та лініями та так щоб вджети були як меньша коробка в більшій
        line3.add_widget(introduce)# додаємо все інше тут текст
        line3.add_widget(txt_puls)
        line3.add_widget(txt_sec)
        line3.add_widget(line1)# тут лінію імя
        line3.add_widget(line2)# тут лінію віку
        line3.add_widget(line4)
        self.add_widget(line3)# тут на екран додаємо цб третю лінію

    def next(self):# прописуємо фунції для двох кнопок
        self.manager.current = "result"# ереключення на натсупний екран

    def before(self):#переключення на минулий еккран
        self.manager.current = "third"# на минулий екран
class ResultScreen(Screen):
    def __init__(self, **kwargs):# тут можна писати скільки хочеш аргументів
        super().__init__(**kwargs)# копіюємо кістяк супер класу також
        name_lbl = Label(text="ghjkl")
        result_text = Label(text="zsdfvzx")
        for_result_lbl = Label(text="zxcv")
        how_good_lbl = Label(text="xcvbdfg")
        ans_how_good_lbl = Label(text="zxcv")

        row1 = BoxLayout()
        row1.add_widget(result_text)
        row1.add_widget(for_result_lbl)

        col1 = BoxLayout(orientation="vertical",size_hint=(0.3, 0.2))
        col1.add_widget(name_lbl)
        col1.add_widget(row1)
        col1.add_widget(how_good_lbl)
        col1.add_widget(ans_how_good_lbl)

        main_layout = AnchorLayout(anchor_x="center", anchor_y="center")
        main_layout.add_widget(col1)
        self.add_widget(main_layout)


class HeartCheck(App):# тут прописуємо клас менеджер та клас запуску програми
    def build(self):# функція має бути в класі полюбе або пас
        sm = ScreenManager()# тут створюємо менеджера скрінів
        sm.add_widget(FirstScreen(name="first"))# дамо кожному класу імя яке буде полегшувати переходи
        sm.add_widget(SecondScreen(name="second"))
        sm.add_widget(ThirdScreen(name="third"))
        sm.add_widget(FourthScreen(name="fourth"))
        sm.add_widget(ResultScreen(name="result"))
        return sm

app = HeartCheck()# це створюєм об"єкт з класу що створили для запуску цього всього
app.run()# і визиваєм метод ран що запускає програму