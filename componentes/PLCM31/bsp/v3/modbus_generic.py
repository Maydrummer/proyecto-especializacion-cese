import struct
from dataclasses import dataclass,field
from PLCM31.bsp.common.my_pymodbus.sync import ModbusTcpClient
from pymodbus.transaction import ModbusSocketFramer
from PLCM31.bsp.common.Config import Config




@dataclass
class AddressTCP:
    aplicacion: str
    ip: str
    port: int
    slave: int



# used to umpack data
def get_value(stream: list, len: int, dec: int, endianness: str, to_umpack: str):
    bytes_stream = struct.pack(endianness + "%sH" % len, *stream)
    value = struct.unpack(endianness + to_umpack, bytes_stream)[0]

    if dec == 0:
        return value

    return value / (10 ** dec)


@dataclass
class ReadCoils_01:
    reg: int
    len: int

    def get_value(self, modbus_client: ModbusTcpClient, slave: int):
        r = modbus_client.read_coils(self.reg, self.len, unit=slave)
        if self.len == 1:
            return r.bits[0]
        else:
            return r.bits


@dataclass
class ReadDiscreteInputs_02:
    reg: int
    len: int

    def get_value(self, modbus_client: ModbusTcpClient, slave: int):
        r = modbus_client.read_discrete_inputs(self.reg, self.len, unit=slave)
        if self.len == 1:
            return r.bits[0]
        else:
            return r.bits


@dataclass
class ReadInputRegisters_04:
    reg: int
    len: int
    dec: int
    endianness: str
    to_umpack: str

    def get_value(self, modbus_client: ModbusTcpClient, slave: int):
        r = modbus_client.read_input_registers(self.reg, self.len, unit=slave)
        stream = r.registers

        return get_value(stream=stream,
                         len=self.len,
                         dec=self.dec,
                         endianness=self.endianness,
                         to_umpack=self.to_umpack)


@dataclass
class WriteSingleCoil_05:
    reg: int
    bit: bool

    def get_value(self, modbus_client: ModbusTcpClient, slave: int):
        r = modbus_client.write_coil(self.reg, self.bit, unit=slave)
        if r.isError():
            return f"Error: {r}"
        else:
            return bool(self.bit)


@dataclass
class WriteMultipleCoils_15:
    reg: int
    bits: str

    def get_value(self, modbus_client: ModbusTcpClient, slave: int):
        boolean_list = [bit == '1' for bit in self.bits]
        r = modbus_client.write_coils(self.reg, boolean_list, unit=slave)
        if r.isError():
            return f"Error: {r}"
        else:
            return boolean_list


# commonly used in modbus tcp because there is no problem reading each register each time
@dataclass
class RegisterModBus:
    reg: int
    len: int
    dec: int
    endianness: str
    to_umpack: str

    def get_value(self, modbus_client: ModbusTcpClient, slave: int):
        r = modbus_client.read_holding_registers(self.reg, self.len, unit=slave)
        stream = r.registers

        return get_value(stream=stream,
                         len=self.len,
                         dec=self.dec,
                         endianness=self.endianness,
                         to_umpack=self.to_umpack)


# commonly used in modbus serial because it is better read multiple registers
@dataclass
class RegistersModbus:
    reg: int
    len: int

    def get_registers(self, modbus_client: ModbusTcpClient, slave: int):
        r = modbus_client.read_holding_registers(self.reg, self.len, unit=slave)
        stream = r.registers

        return stream


@dataclass
class ModbusDeviceBase:
    address: AddressTCP
    status: str = field(init=False)

    def get_client(self) -> ModbusTcpClient:
        client = None

        client = ModbusTcpClient(host=self.address.ip,
                                 port=self.address.port,
                                 framer=ModbusSocketFramer,
                                 timeout=Config.TIMEOUT_MODBUS)

        return client

