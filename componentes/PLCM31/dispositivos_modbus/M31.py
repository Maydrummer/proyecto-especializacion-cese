import time, traceback

from bsp.common.Config import Config

from bsp.v3.modbus_generic import ReadDiscreteInputs_02, ModbusDeviceBase, WriteMultipleCoils_15, ReadInputRegisters_04, ReadCoils_01

from dataclasses import dataclass, field

from typing import Union, List

# Endianess
# >         big endian
# <         little endian

# Format    C Type  Standard    size
# c         char                1
# b         signed char         1
# B         unsigned char       1
# ?         _Bool               1
# h         short               2
# H         unsigned short      2
# i         int                 4
# I         unsigned int        4
# l         long                4
# L         unsigned long       4
# q         long  long          8
# Q         unsigned long long  8
# f         float               4
# d         double              8

ENDIANESS = ">"


@dataclass
class DI_registers:
    DIGITAL_INPUT_1: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(0, 1)
    DIGITAL_INPUT_2: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(1, 1)
    DIGITAL_INPUT_3: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(2, 1)
    DIGITAL_INPUT_4: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(3, 1)
    DIGITAL_INPUT_5: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(4, 1)
    DIGITAL_INPUT_6: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(5, 1)
    DIGITAL_INPUT_7: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(6, 1)
    DIGITAL_INPUT_8: ReadDiscreteInputs_02 = ReadDiscreteInputs_02(7, 1)


@dataclass
class DOC_registers:
    DIGITAL_OUTPUT_COIL_1: ReadCoils_01 = ReadCoils_01(0, 1)
    DIGITAL_OUTPUT_COIL_2: ReadCoils_01 = ReadCoils_01(1, 1)
    DIGITAL_OUTPUT_COIL_3: ReadCoils_01 = ReadCoils_01(2, 1)
    DIGITAL_OUTPUT_COIL_4: ReadCoils_01 = ReadCoils_01(3, 1)
    DIGITAL_OUTPUT_COIL_5: ReadCoils_01 = ReadCoils_01(4, 1)
    DIGITAL_OUTPUT_COIL_6: ReadCoils_01 = ReadCoils_01(5, 1)
    DIGITAL_OUTPUT_COIL_7: ReadCoils_01 = ReadCoils_01(6, 1)
    DIGITAL_OUTPUT_COIL_8: ReadCoils_01 = ReadCoils_01(7, 1)
    DIGITAL_OUTPUT_COIL_9: ReadCoils_01 = ReadCoils_01(8, 1)
    DIGITAL_OUTPUT_COIL_10: ReadCoils_01 = ReadCoils_01(9, 1)
    DIGITAL_OUTPUT_COIL_11: ReadCoils_01 = ReadCoils_01(10, 1)
    DIGITAL_OUTPUT_COIL_12: ReadCoils_01 = ReadCoils_01(11, 1)
    DIGITAL_OUTPUT_COIL_13: ReadCoils_01 = ReadCoils_01(12, 1)
    DIGITAL_OUTPUT_COIL_14: ReadCoils_01 = ReadCoils_01(13, 1)
    DIGITAL_OUTPUT_COIL_15: ReadCoils_01 = ReadCoils_01(14, 1)
    DIGITAL_OUTPUT_COIL_16: ReadCoils_01 = ReadCoils_01(15, 1)


@dataclass
class DO_registers:
    DIGITAL_OUTPUT_1_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "10000000000000000000")
    DIGITAL_OUTPUT_2_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "01000000000000000000")
    DIGITAL_OUTPUT_3_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00100000000000000000")
    DIGITAL_OUTPUT_4_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00010000000000000000")
    DIGITAL_OUTPUT_5_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00001000000000000000")
    DIGITAL_OUTPUT_6_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000100000000000000")
    DIGITAL_OUTPUT_7_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000010000000000000")
    DIGITAL_OUTPUT_8_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000001000000000000")
    DIGITAL_OUTPUT_9_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000100000000000")
    DIGITAL_OUTPUT_10_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000010000000000")
    DIGITAL_OUTPUT_11_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000001000000000")
    DIGITAL_OUTPUT_12_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000000100000000")
    DIGITAL_OUTPUT_13_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000000010000000")
    DIGITAL_OUTPUT_14_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000000001000000")
    DIGITAL_OUTPUT_15_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000000000100000")
    DIGITAL_OUTPUT_16_UP: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000000000010000")

    DIGITAL_OUTPUT_ALL_FALSE: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "00000000000000000000")
    DIGITAL_OUTPUT_ALL_TRUE: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "11111111111111111111")
    DIGITAL_OUTPUT_ALTERNATIVE1: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "10101010101010101010")
    DIGITAL_OUTPUT_ALTERNATIVE2: WriteMultipleCoils_15 = WriteMultipleCoils_15(0, "01010101010101010101")

    # DIGITAL_OUTPUT_ONLY_NUMBER_1: WriteSingleCoil_05 = WriteSingleCoil_05(0, True)
    # DIGITAL_OUTPUT_ONLY_NUMBER_2: WriteSingleCoil_05 = WriteSingleCoil_05(1, True)
    # DIGITAL_OUTPUT_ONLY_NUMBER_3: WriteSingleCoil_05 = WriteSingleCoil_05(2, True)
    # DIGITAL_OUTPUT_ONLY_NUMBER_4: WriteSingleCoil_05 = WriteSingleCoil_05(3, True)


@dataclass
class AI_registers:
    ANALOG_INPUT_1: ReadInputRegisters_04 = ReadInputRegisters_04(0, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_2: ReadInputRegisters_04 = ReadInputRegisters_04(1, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_3: ReadInputRegisters_04 = ReadInputRegisters_04(2, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_4: ReadInputRegisters_04 = ReadInputRegisters_04(3, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_5: ReadInputRegisters_04 = ReadInputRegisters_04(4, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_6: ReadInputRegisters_04 = ReadInputRegisters_04(5, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_7: ReadInputRegisters_04 = ReadInputRegisters_04(6, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_8: ReadInputRegisters_04 = ReadInputRegisters_04(7, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_9: ReadInputRegisters_04 = ReadInputRegisters_04(8, 1, 6, ENDIANESS, "h")
    ANALOG_INPUT_10: ReadInputRegisters_04 = ReadInputRegisters_04(9, 1, 6, ENDIANESS, "h")

@dataclass
class PLC_M31(ModbusDeviceBase):
    i1: bool = field(init=False)
    i2: bool = field(init=False)
    i3: bool = field(init=False)
    i4: bool = field(init=False)
    i5: bool = field(init=False)
    i6: bool = field(init=False)
    i7: bool = field(init=False)
    i8: bool = field(init=False)

    # ai1: bool = field(init=False)
    # ai2: bool = field(init=False)
    # ai3: bool = field(init=False)
    # ai4: bool = field(init=False)
    # ai5: bool = field(init=False)
    # ai6: bool = field(init=False)
    # ai7: bool = field(init=False)
    # ai8: bool = field(init=False)
    #
    # oc1: bool = field(init=False)
    # oc2: bool = field(init=False)
    # oc3: bool = field(init=False)
    # oc4: bool = field(init=False)
    # oc5: bool = field(init=False)
    # oc6: bool = field(init=False)
    # oc7: bool = field(init=False)
    # oc8: bool = field(init=False)
    # oc9: bool = field(init=False)
    # oc10: bool = field(init=False)
    # oc11: bool = field(init=False)
    # oc12: bool = field(init=False)
    # oc13: bool = field(init=False)
    # oc14: bool = field(init=False)
    # oc15: bool = field(init=False)
    # oc16: bool = field(init=False)

    def __post_init__(self):
        retry = Config.RETRY
        while retry > 0:
            try:
                with self.get_client() as client:
                    self.client = client
                    self.slave = self.address.slave
                    self.status = "OK"
                    return True
            except Exception as e:
                retry -= 1
                time.sleep(Config.TIME_WAIT_EXCEPTION)

                self.status = traceback.format_exc()

    def get_input(self):
        self.i1 = DI_registers.DIGITAL_INPUT_1.get_value(self.client, self.slave)
        self.i2 = DI_registers.DIGITAL_INPUT_2.get_value(self.client, self.slave)
        self.i3 = DI_registers.DIGITAL_INPUT_3.get_value(self.client, self.slave)
        self.i4 = DI_registers.DIGITAL_INPUT_4.get_value(self.client, self.slave)
        self.i5 = DI_registers.DIGITAL_INPUT_5.get_value(self.client, self.slave)
        self.i6 = DI_registers.DIGITAL_INPUT_6.get_value(self.client, self.slave)
        self.i7 = DI_registers.DIGITAL_INPUT_7.get_value(self.client, self.slave)
        self.i8 = DI_registers.DIGITAL_INPUT_7.get_value(self.client, self.slave)

        # self.ai1 = AI_registers.ANALOG_INPUT_1.get_value(self.client, self.slave)
        # self.ai2 = AI_registers.ANALOG_INPUT_2.get_value(self.client, self.slave)
        # self.ai3 = AI_registers.ANALOG_INPUT_3.get_value(self.client, self.slave)
        # self.ai4 = AI_registers.ANALOG_INPUT_4.get_value(self.client, self.slave)
        # self.ai5 = AI_registers.ANALOG_INPUT_5.get_value(self.client, self.slave)
        # self.ai6 = AI_registers.ANALOG_INPUT_6.get_value(self.client, self.slave)
        # self.ai7 = AI_registers.ANALOG_INPUT_7.get_value(self.client, self.slave)
        # self.ai8 = AI_registers.ANALOG_INPUT_8.get_value(self.client, self.slave)
        #
        # self.oc1 = DOC_registers.DIGITAL_OUTPUT_COIL_1.get_value(self.client, self.slave)
        # self.oc2 = DOC_registers.DIGITAL_OUTPUT_COIL_2.get_value(self.client, self.slave)
        # self.oc3 = DOC_registers.DIGITAL_OUTPUT_COIL_3.get_value(self.client, self.slave)
        # self.oc4 = DOC_registers.DIGITAL_OUTPUT_COIL_4.get_value(self.client, self.slave)
        # self.oc5 = DOC_registers.DIGITAL_OUTPUT_COIL_5.get_value(self.client, self.slave)
        # self.oc6 = DOC_registers.DIGITAL_OUTPUT_COIL_6.get_value(self.client, self.slave)
        # self.oc7 = DOC_registers.DIGITAL_OUTPUT_COIL_7.get_value(self.client, self.slave)
        # self.oc8 = DOC_registers.DIGITAL_OUTPUT_COIL_8.get_value(self.client, self.slave)
        # self.oc9 = DOC_registers.DIGITAL_OUTPUT_COIL_9.get_value(self.client, self.slave)
        # self.oc10 = DOC_registers.DIGITAL_OUTPUT_COIL_10.get_value(self.client, self.slave)
        # self.oc11 = DOC_registers.DIGITAL_OUTPUT_COIL_11.get_value(self.client, self.slave)
        # self.oc12 = DOC_registers.DIGITAL_OUTPUT_COIL_12.get_value(self.client, self.slave)
        # self.oc13 = DOC_registers.DIGITAL_OUTPUT_COIL_13.get_value(self.client, self.slave)
        # self.oc14 = DOC_registers.DIGITAL_OUTPUT_COIL_14.get_value(self.client, self.slave)
        # self.oc15 = DOC_registers.DIGITAL_OUTPUT_COIL_15.get_value(self.client, self.slave)
        # self.oc16 = DOC_registers.DIGITAL_OUTPUT_COIL_16.get_value(self.client, self.slave)

        return self
    def get_output(self):
        DO_registers.DIGITAL_OUTPUT_ALL_TRUE.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_1_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_2_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_3_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_4_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_5_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_6_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_7_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_8_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_9_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_10_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_11_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_12_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_13_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_14_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_15_UP.get_value(self.client, self.slave)
        time.sleep(1)
        DO_registers.DIGITAL_OUTPUT_16_UP.get_value(self.client, self.slave)

        return self
