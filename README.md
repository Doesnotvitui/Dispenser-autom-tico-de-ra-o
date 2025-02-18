# Projeto de Dosagem Automática de Ração para Animais

Este projeto visa automatizar a dosagem de ração para animais de estimação com base no porte do animal (pequeno, médio ou grande). O sistema utiliza um microcontrolador ESP32 para controlar um servo motor que libera a ração, um sensor de carga (HX711) para medir o peso da ração, um botão para seleção do porte do animal, e um display LCD para fornecer feedback ao usuário. Além disso, o ESP32 permite a funcionalidade remota, possibilitando o controle do sistema via conexão à internet.

## Componentes Utilizados

- **Microcontrolador**: ESP32 (com Wi-Fi integrado)
- **Display LCD**: 16x2 com interface I2C
- **Sensor de Carga**: HX711
- **Servo Motor**: Para liberar a ração
- **Botão**: Para seleção do porte do animal
- **LED**: Para indicar o status do sistema

## Funcionalidades

1. **Seleção do Porte do Animal**:
   - O usuário pode selecionar o porte do animal (pequeno, médio ou grande) pressionando o botão uma, duas ou três vezes, respectivamente.
   - O display LCD exibe as opções e confirma a seleção.

2. **Medição de Peso**:
   - O sensor de carga (HX711) mede o peso da ração no pote.
   - O sistema verifica se a quantidade de ração já é suficiente para o porte selecionado.

3. **Liberação de Ração**:
   - Se a quantidade de ração for insuficiente, o servo motor é acionado para liberar mais ração até que o peso desejado seja atingido.
   - O LED é acionado durante o processo de liberação de ração.

4. **Feedback ao Usuário**:
   - O display LCD informa o status do sistema, como "Ração liberada" ou "Já tem ração no pote".

5. **Funcionalidade Remota**:
   - O ESP32 permite a conectividade com a internet, possibilitando o controle remoto do sistema.
   - O usuário pode enviar comandos via MQTT para liberar ração ou verificar o status do sistema.
   - O sistema pode ser integrado a plataformas IoT para monitoramento e controle em tempo real.

## Código

O código principal está escrito em MicroPython e pode ser encontrado no arquivo `main.py`. Ele inclui a inicialização dos componentes, a lógica de seleção do porte do animal, a medição de peso, o controle do servo motor e a funcionalidade remota via MQTT.

### Estrutura do Código

- **Inicialização dos Componentes**:
  - Display LCD, sensor de carga, botão, servo motor e LED são inicializados.

- **Conectividade**:
  - O ESP32 se conecta a uma rede Wi-Fi e a um servidor MQTT para permitir o controle remoto.

- **Função `calcula_peso()`**:
  - Realiza a leitura do sensor de carga e retorna o peso medido.

- **Função `tempo_b()`**:
  - Detecta quantas vezes o botão foi pressionado com debounce para evitar leituras múltiplas.

- **Loop Principal**:
  - Exibe as opções de porte no display.
  - Captura a escolha do usuário.
  - Verifica o peso atual e libera ração se necessário.
  - Fornece feedback ao usuário através do display LCD.
  - Verifica comandos remotos recebidos via MQTT.

## Como Usar

1. **Conectar os Componentes**:
   - Conecte o display LCD, sensor de carga, botão, servo motor e LED ao ESP32 conforme o esquema de fiação.

2. **Configurar a Conectividade**:
   - Configure as credenciais da rede Wi-Fi e do servidor MQTT no código.

3. **Carregar o Código**:
   - Carregue o código `main.py` no ESP32.

4. **Operação**:
   - Siga as instruções exibidas no display LCD para selecionar o porte do animal e liberar a ração.
   - Utilize uma plataforma IoT ou um cliente MQTT para enviar comandos remotos ao sistema.

## Requisitos

- MicroPython instalado no ESP32.
- Bibliotecas necessárias: `lcd_api`, `i2c_lcd`, `hx711`, `servo`, `umqtt.simple`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias no projeto.
