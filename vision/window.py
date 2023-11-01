from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from control import controleOrdenacao, controleBusca, controleHash
import random

class MyWindow(App):

    def build(self):
        Window.title = "Projeto_Analise_de_Algoritmos"
        Config.set('graphics', 'multisamples', '0')
        Window.size = (1280, 1000)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        size_input = TextInput(hint_text="Tamanho da Tabela Hash", multiline=False, size_hint_y=None, height=44, write_tab=False)
        layout.add_widget(size_input)
        init_button = Button(text="Inicializar Hash", size_hint_y=None, height=44)
        init_button.bind(on_release=lambda instance: self.init_hash(size_input.text))
        layout.add_widget(init_button)
        dropdown = DropDown()

        dropdown_actions = DropDown()
        options = ["Adicionar", "Remover", "Imprimir"]
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn, x=option: dropdown_actions.select(x))
            dropdown_actions.add_widget(btn)

        self.actions_button = Button(
            text="Ações na Tabela Hash", size_hint_y=None, height=44
        )
        self.actions_button.bind(on_release=dropdown_actions.open)

        dropdown_actions.bind(on_select=lambda instance, x: self.handle_dropdown_option(x))
        layout.add_widget(self.actions_button)

        # Crie uma instância do controlador da tabela hash
        self.hash_controller = None

        # Adicione uma caixa de entrada para chave e valor
        self.key_input = TextInput(hint_text="Chave", multiline=False, size_hint_y=None, height=44, write_tab=False)
        self.value_input = TextInput(hint_text="Valor", multiline=False, size_hint_y=None, height=44, write_tab=False)
        layout.add_widget(self.key_input)
        layout.add_widget(self.value_input)

        self.result_label = Label(text="Resultado: ", size_hint_y=None, height=44)
        layout.add_widget(self.result_label)

        self.operations_button = Button(
            text="Aplicar Operação", size_hint_y=None, height=44
        )
        self.operations_button.bind(on_release=lambda instance: self.handle_operations())
        layout.add_widget(self.operations_button)

        options = ["Mergesort","Quicksort", "Heapsort"]
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn, x=option: dropdown.select(x))
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
        self.apply_button = Button(text="Aplicar", size_hint_y=None, height=44, opacity=0)
        self.apply_button.bind(on_release=self.generate_auto)
        self.apply_button2 = Button(text="Aplicar", size_hint_y=None, height=44, opacity=0)
        self.apply_button2.bind(on_release=self.generate_manual)
        self.search_button = Button(text='Buscar chave', size_hint_y=None, height=44)
        self.search_button.bind(on_release=self.search)
        self.run_button = Button(text="Rodar Algoritmo", size_hint_y=None, height=44)
        self.run_button.bind(on_release=self.run_alg)

        self.manual_input = TextInput(
            hint_text="Digite dessa forma: valor nome1 valor nome2 valor nome3...", multiline=False, size_hint_y=None, height=44, write_tab=False, opacity=0
        )
        self.auto_input = TextInput(
            hint_text="Insira o tamanho do vetor", multiline=False, size_hint_y=None, height=44, write_tab=False, opacity=0
        )

        self.search_input = TextInput(
            hint_text="Insira o elemento a ser buscado", multiline=False, size_hint_y=None, height=44, write_tab=False
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
        layout.add_widget(self.search_input)
        layout.add_widget(self.search_button)

        return layout

    # Métodos de manipulação da Tabela Hash
    def init_hash(self, size):
        try:
            size = int(size)
            if size > 0:
                # Crie uma instância do HashTableController com o tamanho escolhido
                self.hash_controller = controleHash.HashTableController(size)
                self.result_label.text = f"Tabela hash inicializada com tamanho {size}."
            else:
                self.result_label.text = "Tamanho inválido. Deve ser maior que zero."
        except ValueError:
            self.result_label.text = "Digite um número válido para o tamanho."

    def handle_dropdown_option(self, option):
        selected_option = option
        if selected_option == "Adicionar":
            self.add_to_hash()
        elif selected_option == "Remover":
            self.remove_from_hash()
        elif selected_option == "Imprimir":
            self.print_hash()

    def add_to_hash(self):
        key = self.key_input.text
        value = self.value_input.text
        if self.hash_controller is not None:
            self.hash_controller.add(key, value)
            self.result_label.text = f"Chave '{key}' e Valor '{value}' adicionados à tabela hash."
        else:
            self.result_label.text = "Inicialize a tabela hash primeiro."

    def remove_from_hash(self):
        key = self.key_input.text
        if self.hash_controller is not None:
            self.hash_controller.remove(key)
            self.result_label.text = f"Chave '{key}' removida da tabela hash."
        else:
            self.result_label.text = "Inicialize a tabela hash primeiro."

    def print_hash(self):
        if self.hash_controller is not None:
            hash_content = self.hash_controller.print_table()
            if hash_content is not None:
                self.result_label.text = hash_content
            else:
                self.result_label.text = "Tabela hash vazia."
        else:
            self.result_label.text = "Inicialize a tabela hash primeiro."

    # Outros métodos
    def handle_operations(self):
        selected_option = self.mainbutton.text
        if selected_option == "Mergesort" or selected_option == "Quicksort" or selected_option == "Heapsort":
            x = controleOrdenacao.process_sorting(self.mainbutton.text, self.result_dict)
            self.result_label.text = str(x)
        else:
            self.result_label.text = "Selecione um método de ordenação."

    def generate_auto(self, instance):
        try:
            size = int(self.auto_input.text)
            if size > 0:
                nomes = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Isabel", "Jack"]
                if size > 1000:
                    self.result_label.text = "Tamanho inválido. O número deve ser no máximo 1000."
                else:
                    numeros_unicos = random.sample(range(1, 1001), size)
                    shuffled_nomes = [random.choice(nomes) for _ in range(size)]
                    self.result_dict = {numero: nome for numero, nome in zip(numeros_unicos, shuffled_nomes)}
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
                value = int(name_value_pairs[i])
                key = name_value_pairs[i+1]
                self.result_dict[key] = value

            self.user_data = self.result_dict

            result_text = "Resultado: " + str(self.result_dict) + "\n" + f"Tamanho do vetor: {len(self.result_dict)}"
            self.result_label.text = result_text
        except (ValueError, IndexError):
            self.result_label.text = "Digite chaves válidas de chave e valor (ex: 1 nome1 2 nome2)."

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
        selected_option = self.mainbutton.text
        if selected_option == "Mergesort" or selected_option == "Quicksort" or selected_option == "Heapsort":
            x = controleOrdenacao.process_sorting(self.mainbutton.text, self.result_dict)
            self.result_label.text = str(x)
        else:
            self.result_label.text = "Selecione um método de ordenação."

    def search(self, instance):
        print('buscando chave...')
        x = controleBusca.processing_search(self.result_dict, int(self.search_input.text))
        if x is not None:
            self.result_label.text = "Resultado da busca => " + "Índice: " + str(x) + f" Nome: {self.result_dict[x]}"
        else:
            self.result_label.text = "Índice não encontrado."

if __name__ == '__main__':
    MyWindow().run()
