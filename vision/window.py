from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from control import controleOrdenacao
import random
import itertools


class MyWindow(App):

    def build(self):
        Window.title = "Projeto_Analise_de_Algoritmos"
        Config.set('graphics', 'multisamples', '0')

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        dropdown = DropDown()
        options = ["Mergesort","Quicksort", "Heapsort"]
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        self.mainbutton = Button(
            text="Métodos de Ordenação", size_hint_y=None, height=44
        )
        self.mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x) or setattr(self, 'method', x))
        layout.add_widget(self.mainbutton)

        auto_button = Button(text="Gerar Automaticamente", size_hint_y=None, height=44)
        manual_button = Button(text="Gerar Manualmente", size_hint_y=None, height=44)
        auto_button.bind(on_release=self.toggle_auto_input)
        manual_button.bind(on_release=self.toggle_manual_input)
        self.apply_button = Button(text="Aplicar",size_hint_y=None, height=44,opacity=0)
        self.apply_button.bind(on_release=self.generate_auto)
        self.apply_button2 = Button(text="Aplicar",size_hint_y=None, height=44,opacity=0)
        self.apply_button2.bind(on_release=self.generate_manual)
        self.run_button = Button(text="Rodar Algoritmo",size_hint_y=None,height=44)
        self.run_button.bind(on_release=self.run_alg)

        self.manual_input = TextInput(
            hint_text="Digite dessa forma: chave1 10 chave2 15 chaveN N...", multiline=False, size_hint_y=None, height=44, write_tab=False, opacity=0
        )
        self.auto_input = TextInput(
            hint_text="Insira o tamanho do vetor", multiline=False, size_hint_y=None, height=44, write_tab=False, opacity=0
        )
        layout.add_widget(manual_button)
        layout.add_widget(self.manual_input)
        layout.add_widget(self.apply_button2) #adicionei aqui para ficar embaixo do text field
        layout.add_widget(auto_button)
        layout.add_widget(self.auto_input)
        layout.add_widget(self.apply_button)
        self.result_label = Label(text="Resultado: ", size_hint_y=None, height=44)
        layout.add_widget(self.result_label)
        layout.add_widget(self.run_button)

        return layout

    def generate_auto(self, instance):
        nomes = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Isabel", "Jack"]
        try:
            size = int(self.auto_input.text)
            if size > 0:
                # Crie um iterador infinito dos nomes
                nome_generator = itertools.cycle(nomes)
                self.result_dict = {next(nome_generator): random.randint(1, size) for _ in range(size)}
                self.result_label.text = "Resultado: " + str(self.result_dict)
            else:
                self.result_label.text = "Tamanho inválido."
        except ValueError:
            self.result_label.text = "Digite um número válido."

           

    def generate_manual(self, instance):
        input_text = self.manual_input.text
        name_value_pairs = input_text.split()
        
        try:
            self.result_dict = {}
            for i in range(0, len(name_value_pairs), 2):
                key = name_value_pairs[i]
                value = int(name_value_pairs[i + 1])
                self.result_dict[key] = value
            
            # Você pode adicionar o resultado a uma estrutura de dados, por exemplo, um dicionário de classe
            self.user_data = self.result_dict

            result_text = "Resultado: " + str(self.result_dict) + "\n" + f"Pares inseridos manualmente: {len(self.result_dict)}"
            self.result_label.text = result_text
        except (ValueError, IndexError):
            self.result_label.text = "Digite pares válidos de chave e valor (ex: chave1 10 chave2 20)."


    def toggle_manual_input(self, instance):
        if self.manual_input.opacity == 0 and self.apply_button2.opacity == 0:
            self.manual_input.opacity = 1
            self.apply_button2.opacity = 1
        else:
            self.manual_input.opacity = 0
            self.apply_button2.opacity = 0

    def toggle_auto_input(self, instance):
        if self.auto_input.opacity == 0 and self.apply_button.opacity == 0:
            self.auto_input.opacity = 1
            self.apply_button.opacity = 1
        else:
            self.auto_input.opacity = 0
            self.apply_button.opacity = 0

    def run_alg(self, instance):
       print(self.mainbutton.text)
       x = controleOrdenacao.process_sorting(self.mainbutton.text, self.result_dict)
       self.result_label.text = str(x)


