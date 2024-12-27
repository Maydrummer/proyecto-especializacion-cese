import time
from bsp.common.util import asdict
from dispositivos_modbus.PLC_M31 import PLC
from bsp.v3.modbus_generic import AddressTCP
import pprint
# Configuracion Modbus
ip_modbus = '192.168.3.7'
puerto_modbus = 502
slave_modbus = 1
modbus_module = AddressTCP(aplicacion='Tesalia', ip= ip_modbus,port= puerto_modbus, slave= slave_modbus)
#Configuracion entradas
lista_de_entradas_digitales = [
    'DI1','DI2','DI3','DI4'
]

#Configuracion salidas
lista_de_salidas_digitales = [
    'DO1','DO2','DO3','DO4'
]
control_plc = PLC(address=modbus_module, digital_input_list=lista_de_entradas_digitales,
                  digital_output_list=lista_de_salidas_digitales)
while True:
    try:
        time.sleep(5)
        control_plc.get_input_states()
        control_plc.set_output(lista_de_salidas_digitales[0])
        time.sleep(5)
        control_plc.reset_output(lista_de_salidas_digitales[0])
        entradas = control_plc.digital_inputs_registers
        print(entradas[1])

    except Exception as e:
        print(f"Error: {e}")
