#App creada con Kivy, se requiere 
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
#Para Graficar se requiere
import matplotlib.pyplot as plt
import numpy as np

#CREO LISTAS PARA ALMACENAR DATOS
guardarm1 = []
guardarm2 = []
guardarvel = []
guardarvele = []



class Generator (App):


    def build(self):
        
        self.window = GridLayout()
        self.window.cols = 3
        self.window.size_hint = (0.5, 0.6)
        self.window.spacing= 15
        self.window.padding= 10
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}


        #PRIMERA DATO, VELOCIDAD MASICA
        self.user = Label(
                        text='Velocidad Masica: ',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #INGRESAR DATO DE VELOCIDAD

        self.velocidadm = TextInput(
                    multiline=True,
                    input_filter = 'float',
                    write_tab = False,
                    padding_y = (10,10),
                    size_hint = (1.5, 0.2),
                    font_size = (20),
                    background_color = '#F59C22',
                    hint_text_color = [0.5, 0.5, 0.5, 1.0],
                    halign = 'center'
                    )
                    
        self.window.add_widget(self.velocidadm) 
        
        #UNIDADES 
        self.user = Label(
                        text='''<--Dato Principal
Kg/h''',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)   
        
        #PRIMERA DATO, ENERGIA CINETICA
        self.user = Label(
                        text='Energia Cinetica: ',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #INGRESAR DATO ENERGIA CINETICA

        self.energiac = TextInput(
                    multiline=True,
                    input_filter = 'float',
                    write_tab = False,
                    padding_y = (10,10),
                    size_hint = (1.5, 0.2),
                    font_size = (20),
                    background_color = '#F59C22',
                    hint_text_color = [0.5, 0.5, 0.5, 1.0],
                    halign = 'center'
                    )
                    
        self.window.add_widget(self.energiac)
        
        #UNIDADES
        self.user = Label(
                        text='''<--Ingresar 0 
si no existe''',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user) 
        
        #PRIMERA DATO, ENERGIA POTENCIAL
        self.user = Label(
                        text='Energia Potencial: ',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #INGRESAR DATO ENERGIA POTENCIAL

        self.energiap = TextInput(
                    multiline=True,
                    input_filter = 'float',
                    write_tab = False,
                    padding_y = (10,10),
                    size_hint = (1.5, 0.2),
                    font_size = (20),
                    background_color = '#F59C22',
                    hint_text_color = [0.5, 0.5, 0.5, 1.0],
                    halign = 'center'
                    )
                    
        self.window.add_widget(self.energiap) 
        
        #UNIDADES
        self.user = Label(
                        text='''<--Ingresar 0 
si no existe''',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user) 
        
        #VER RESULTADO M1
        self.user = Label(
                        text='Resultado M1',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #VER DATO M1

        self.resultado = TextInput(
                    multiline=True,
                    input_filter = 'float',
                    write_tab = False,
                    padding_y = (10,10),
                    size_hint = (1.5, 0.2),
                    font_size = (20),
                    background_color = '#00ff15',
                    hint_text_color = [0.5, 0.5, 0.5, 1.0],
                    halign = 'center'
                    )
                    
        self.window.add_widget(self.resultado)
        
        
        #UNIDADES M1
        self.user = Label(
                        text='Kg/h',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user) 
        
        
        #VER RESULTADO M2
        self.user = Label(
                        text='Resultado M2',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #VER DATO M2

        self.resultado1 = TextInput(
                    multiline=True,
                    input_filter = 'float',
                    write_tab = False,
                    padding_y = (10,10),
                    size_hint = (1.5, 0.2),
                    font_size = (20),
                    background_color = '#00ff15',
                    hint_text_color = [0.5, 0.5, 0.5, 1.0],
                    halign = 'center'
                    )
                    
        self.window.add_widget(self.resultado1)

        #UNIDADES M2
        self.user = Label(
                        text='Kg/h',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #VER RESULTADO VELOCIDAD FLUJO VOLUMETRICO
        self.user = Label(
                        text='Vel. Flujo Vol.',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #VER DATO VELOCIDAD FLUJO VOLUMETRICO

        self.resultado2 = TextInput(
                    multiline=True,
                    input_filter = 'float',
                    write_tab = False,
                    padding_y = (10,10),
                    size_hint = (1.5, 0.2),
                    font_size = (20),
                    background_color = '#00ff15',
                    hint_text_color = [0.5, 0.5, 0.5, 1.0],
                    halign = 'center'
                    )
                    
        self.window.add_widget(self.resultado2)
        
        #UNIDADES
        self.user = Label(
                        text='m3/h',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)        

        #VER RESULTADO CUANDO SE INGRESA ENERGIA CINETICA Y POTENCIAL
        self.user = Label(
                        text='Res. con Energia',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #VER DATO CUANDO SE INGRESA ENERGIA CINETICA Y POTENCIAL

        self.resultado3 = TextInput(
                    multiline=True,
                    input_filter = 'float',
                    write_tab = False,
                    padding_y = (10,10),
                    size_hint = (1.5, 0.2),
                    font_size = (20),
                    background_color = '#4D87DC',
                    hint_text_color = [0.5, 0.5, 0.5, 1.0],
                    halign = 'center'
                    )
                    
        self.window.add_widget(self.resultado3)

        #UNIDADES
        self.user = Label(
                        text='Kg/h',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)  

        #OPCION DE SOLUCION
        
        self.user = Label(
                        text='Ver Resultado: ',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #SOLUCION
        self.button = Button(
                        text='Solucionar',
                        font_size = 35,
                        size_hint = (0.5, 0.5),
                        bold = True,
                        background_color = '#00FFCE'
                        )

        self.button.bind(on_press=self.Balance_General)
        self.window.add_widget(self.button)
        
        #UNIDADES
        self.user = Label(
                        text='Dar clic',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)  
        
         #OPCION DE GUARDAR
        
        self.user = Label(
                        text='Guardar datos: ',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #GUARDAR
        self.button = Button(
                        text='Guardar',
                        font_size = 35,
                        size_hint = (0.5, 0.5),
                        bold = True,
                        background_color = '#00FFCE'
                        )

        self.button.bind(on_press=self.Guardar_Borrar)
        self.window.add_widget(self.button)
        
        #UNIDADES
        self.user = Label(
                        text='Dar clic',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user) 

        #OPCION DE GRAFICAR
        
        self.user = Label(
                        text='Ver Grafica: ',
                        font_size = 25,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user)
        
        #GRAFICAR
        self.graficar = Button(
                        text='Graficar',
                        font_size = 35,
                        size_hint = (0.5, 0.5),
                        bold = True,
                        background_color = '#00FFCE'
                        )

        self.graficar.bind(on_press=self.Graficar)
        self.window.add_widget(self.graficar)
        
        #UNIDADES
        self.user = Label(
                        text='Dar clic',
                        font_size = 15,
                        color = '#F59C22',
                        halign = 'center'
                        )
                    
        self.window.add_widget(self.user) 

        return self.window
    #DEFINIMOS LA FUNCION DEL BOTON SOLUCIONAR
    def Balance_General(self, instance):
        
        presion_1 = 3.11
        H_1 = 2676
        m1 = 1
        Temperatura_1 = 400
        H_2 = 3278
        m2 = 1
        Temperatura_2 = 300
        H_3 = 3074
        
        x = float(self.velocidadm.text)
        y = float(self.energiac.text) + float(self.energiap.text)
        Ecuacion_BalanceG = (x * H_1) - (H_3 * x)
        
        Resultado_Balance = Ecuacion_BalanceG / ((m1 * H_3) - (m1 * H_2)) # Resultado de m1
        Resultado_BalanceAgua = Resultado_Balance + x # Resultado de m2
        SegundoResultado = Resultado_Balance * presion_1 # Resultado Velocidad volumetrico
        Resultado_Con_Energias = Resultado_Balance + y
        
        xy = Resultado_Balance, Resultado_BalanceAgua, SegundoResultado
    
        self.resultado.text = str(Resultado_Balance)
        self.resultado1.text = str(Resultado_BalanceAgua)
        self.resultado2.text = str(SegundoResultado)
        self.resultado3.text = str(Resultado_Con_Energias)

    #DEFINIMOS LA FUNCION DEL BOTON SOLUCIONAR
    def Guardar_Borrar(self, instance):
        
        resultado_balance = float(self.resultado.text)
        resultado_balance_agua = float(self.resultado1.text)
        resultado_velocidad = float(self.resultado2.text)
        resultado_con_energias = float(self.resultado3.text)

        guardarm1.append(resultado_balance)
        guardarm2.append(resultado_balance_agua)
        guardarvel.append(resultado_velocidad)
        guardarvele.append(resultado_con_energias)

        self.resultado.text = ''
        self.resultado1.text = ''
        self.resultado2.text = ''
        self.resultado3.text = ''
        self.velocidadm.text = ''
        self.energiac.text = ''
        self.energiap.text = ''
        
        
        #DEFINIMOS LA FUNCION DEL BOTON SOLUCIONAR
    
    def Graficar(self, instance):
        
        plt.subplot(2, 1, 1)
        plt.plot(guardarm1, guardarvel, 'g--', linewidth=3, color=(0.2, 0.1, 0.4))
        plt.gca().set_prop_cycle(None)
        plt.plot(guardarm2, guardarvel, 'g--', linewidth=2, color='g')
        plt.xlabel('M1 - M2')
        plt.ylabel('VEL')
        plt.title('Grafico 1: M1 M2 - VEL')
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.plot(guardarm1, guardarvele, 'g--', linewidth=3, color=(0.2, 0.1, 0.4))
        plt.gca().set_prop_cycle(None)
        plt.plot(guardarm2, guardarvele, 'g--', linewidth=2, color='g')
        plt.xlabel('M1 - M2')
        plt.ylabel('VELE')
        plt.title('Grafico 2: M1 M2 - VEL con EnergiaC.,P.')
        plt.grid()

        plt.tight_layout()
        plt.show()

        

if __name__ == "__main__":
    Generator().run()
