import time, traceback
from PLCM31.bsp.v3.modbus_generic import AddressTCP, ReadDiscreteInputs_02, ModbusDeviceBase, WriteSingleCoil_05
from PLCM31.bsp.common.my_pymodbus.sync import ModbusTcpClient
from PLCM31.bsp.common.Config import Config
from dataclasses import dataclass, field

ENDIANESS = ">"

@dataclass
class InputRegistersBase(ReadDiscreteInputs_02):
    signal_name: str
    status: bool

@dataclass
class OutputWriteRegisterBase(WriteSingleCoil_05):
    signal_name: str

@dataclass
class PLC(ModbusDeviceBase):
    digital_input_list: list
    digital_output_list: list
    client: ModbusTcpClient = field(init=False)
    digital_inputs_registers: list = None
    digital_output_registers: list = None
    def __post_init__(self):
        retry = Config.RETRY
        while retry > 0:
            try:
                with self.get_client() as client:
                    self.client = client
                    self.slave = self.address.slave
                    self.status = "OK"
                    lista = []
                    for i in self.digital_input_list:
                        reg = self.digital_input_list.index(i)
                        input_register_i = InputRegistersBase(signal_name=i, reg=reg, len=1, status=False)
                        lista.append(input_register_i)
                        self.digital_inputs_registers = lista
                    lista2= []
                    for i in self.digital_output_list:
                        reg = self.digital_input_list.index(i)
                        output_register_i = OutputWriteRegisterBase(signal_name=i, reg=reg, bit=True)
                        lista2.append(output_register_i)
                        self.digital_output_registers = lista2
                    return True
            except Exception as e:
                retry -= 1
                time.sleep(Config.TIME_WAIT_EXCEPTION)
                self.status = traceback.format_exc()

    def get_input_states(self):
        for i in self.digital_inputs_registers:
            status = i.get_value(self.client, self.slave)
            i.status = status

    def set_output(self, output_name):
        reg = self.digital_output_list.index(output_name)
        output_register_i = OutputWriteRegisterBase(signal_name=output_name, reg=reg, bit=True)
        output_register_i.get_value(self.client,self.slave)

    def reset_output(self, output_name):
        reg = self.digital_output_list.index(output_name)
        output_register_i = OutputWriteRegisterBase(signal_name=output_name, reg=reg, bit=False)
        output_register_i.get_value(self.client,self.slave)

