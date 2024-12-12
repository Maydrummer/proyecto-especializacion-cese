import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from bsp.common.util import asdict
from bsp.v3.modbus_generic import AddressTCP
from dispositivos_modbus.M31 import PLC_M31
import pprint, time, json
import paho.mqtt.client as paho_mqtt
# Configuracion MQTT
broker_address = '10.10.36.50'
# Configuracion Modbus
ip_modbus = '192.168.3.7'
puerto_modbus = 502
eslave_modbus = 1
modbus_module = AddressTCP(aplicacion= 'Tablero', ip= ip_modbus,port= puerto_modbus, slave= eslave_modbus)
control_module = PLC_M31(address=modbus_module)
while True:
    try:
        result_dict = control_module.get_input()
        result_dict = asdict(result_dict)
        pprint.pprint(result_dict, compact=True)
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
