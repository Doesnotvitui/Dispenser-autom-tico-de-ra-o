import machine
import time
from machine import Pin, SoftI2C, sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from hx711 import HX711
from servo import Servo

# Criando o objeto Display LED
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = SoftI2C(scl=Pin(23), sda=Pin(22), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Criando o objeto Amplificador de carga 
capteur_hx711 = HX711(16, 17, 1)

# Criando o objeto Button
botao_verde = Pin(25, Pin.IN, Pin.PULL_DOWN)

# Criando o objeto Servo-motor
servo = Servo(19)

# Criando o objeto Led
led = Pin(26, Pin.OUT)

# conectividade
# botao_online = 0
# def mensagem_recebida(topico, valor):
#     botao_online = 1

# servidor = IoTDataHub(
#     "Wokwi-GUEST",
#     "",
#     "aihaghauoghwjfnkbaAGG8714-GE",
#     #verbose = True
# )

# servidor.subscribe("botao_remoto")

# Função para calcular o peso
def calcula_peso():
    capteur_hx711.power_on()

    # Aguarda o sensor estar pronto
    while not capteur_hx711.is_ready():
        pass

    # Realiza a medição
    mesure = capteur_hx711.read(False)
    mesure = capteur_hx711.read(True)

    # Ajuste do valor
    mesure = mesure / 420 * 1000
    time.sleep(1)
    return mesure


# Função para detectar quantas vezes o botão foi pressionado com debounce
def tempo_b():
    lcd.putstr(" Aperte o botao       agora")
    tempo_espera = 0
    quantidade = 0
    tempo_inicio = time.time()
    debounce_delay = 0.3  # Adicionando debounce de 300ms
    
    while True:
        if botao_verde.value() == 1:
            quantidade += 1
            tempo_inicio = time.time()
            time.sleep(debounce_delay)  # Debounce para evitar múltiplas leituras rápidas

        if tempo_espera > 3:
            break
        
        tempo_fim = time.time()
        tempo_espera = tempo_fim - tempo_inicio
        time.sleep(.1)

    return quantidade


# Função principal
while True:
    lcd.putstr("  Aperte 1 vez   Porte pequeno")
    time.sleep(1)
    lcd.clear()
    lcd.putstr("  Aperte 2 vezes   Porte medio")
    time.sleep(1)
    lcd.clear()
    lcd.putstr("  Aperte 3 vezes   Porte grande")
    time.sleep(1)
    lcd.clear()
    
    # Captura a escolha do usuário
    while True:
        lcd.clear()
        duracao = tempo_b()
        peso = calcula_peso()
        
        if peso > 70 and duracao == 1:
            lcd.clear()
            lcd.putstr("Ja tem racao no pote")
            time.sleep(1.5)
            break
        elif peso > 110 and duracao == 2:
            lcd.clear()
            lcd.putstr("Ja tem racao no pote")
            time.sleep(1.5)
            break
        elif peso > 200 and duracao == 3:
            lcd.clear()
            lcd.putstr("Ja tem racao no pote")
            time.sleep(1.5)
            break
        elif duracao == 1:
            # Porte pequeno
            while peso < 70:
                peso = calcula_peso()
                lcd.clear()
                lcd.putstr(" Porte pequeno")
                servo.set(0)
                led.on()
                time.sleep(.5)
            servo.set(90)
            led.off()
            break         
        elif duracao == 2:
            # Porte médio
            while peso < 110:
                peso = calcula_peso()
                lcd.clear()
                lcd.putstr(" Porte   medio")
                servo.set(0)
                led.on()
                time.sleep(.5)
            servo.set(90)
            led.off()
            break           
        elif duracao == 3:
            # Porte grande
            while peso < 200:
                peso = calcula_peso()
                lcd.clear()
                lcd.putstr(" Porte   grande")
                servo.set(0)
                led.on()
                time.sleep(.5)
            servo.set(90)
            led.off()
            break
        else:
            lcd.clear()
            lcd.putstr(" Opcao invalida")
            time.sleep(1.5)
    
    lcd.clear()
    lcd.putstr(" Racao liberada")
    time.sleep(2)  # Adiciona uma pausa final antes de reiniciar o loop
