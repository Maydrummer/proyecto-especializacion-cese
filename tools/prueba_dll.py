import ctypes
import time
import os

SEND_TYPE = 2  # UDP nSendType[in]
IP_ADDRESS = "192.168.100.253"  # pStrParams[in] 
PORT = 6101
GUID = None  # pDeviceGUID 
CMD_TYPE = 2  # Para setear valores
nAreaIndex = 0
nValue = 4
nDecimaValue = 0
SUCCESS = 0
PROGRAMA_ANDEN = 1
PROGRAMA_TIMER = 2
#PARAMETERS FOR TIMER
SUSPEND = 4
START = 3
RESET = 5
try:
    dll_path = os.path.abspath("tools/dll_panel/HDSDK.dll")
    hdsdk = ctypes.WinDLL(dll_path)
    print("DLL cargado correctamente.")
except OSError as e:
    print(f"Error al cargar el DLL: {e}")


def switch_program(n_program:int)->int:
    hdsdk.Cmd_SwitchProgram.argtypes = [
        ctypes.c_int,       # nSendType
        ctypes.c_void_p,    # pStrParams (puntero a string)
        ctypes.c_int,       # nProgramIndex
        ctypes.c_void_p     # pDeviceGUID
    ]

    hdsdk.Cmd_SwitchProgram.restype = ctypes.c_int  
    strParams = ctypes.create_unicode_buffer(f"{IP_ADDRESS}:{PORT}")
    result = hdsdk.Cmd_SwitchProgram(
        SEND_TYPE,  
        ctypes.cast(strParams, ctypes.c_void_p),  # Convertir el string en puntero void*
        n_program,
        GUID  
    )
    return result


def set_value_anden(n_anden:int)->int:
    hdsdk.Cmd_SetDigitState.argtypes = [
        ctypes.c_int,       # nSendType
        ctypes.c_void_p,    # pStrParams (puntero a string)
        ctypes.c_int,       # nAreaIndex
        ctypes.c_int,       # nCmdType
        ctypes.c_int,       # nValue
        ctypes.c_int,       # nDecimaValue
        ctypes.c_void_p     # pDeviceGUID
    ]

    hdsdk.Cmd_SetDigitState.restype = ctypes.c_int  
    strParams = ctypes.create_unicode_buffer(f"{IP_ADDRESS}:{PORT}")
    result = hdsdk.Cmd_SetDigitState(
        SEND_TYPE,  # UDP
        ctypes.cast(strParams, ctypes.c_void_p),  # Convertir el string en puntero void*
        nAreaIndex,
        CMD_TYPE,
        n_anden,
        0,
        GUID  
    )
    return result

def start_time()->int:
    hdsdk.Cmd_SetCountState.argtypes = [
        ctypes.c_int,       # nSendType
        ctypes.c_void_p,    # pStrParams (puntero a string)
        ctypes.c_int,       # nAreaIndex
        ctypes.c_int,       # nCmdType
        ctypes.c_void_p     # pDeviceGUID
    ]

    hdsdk.Cmd_SetCountState.restype = ctypes.c_int  
    strParams = ctypes.create_unicode_buffer(f"{IP_ADDRESS}:{PORT}")
    result = hdsdk.Cmd_SetCountState(
        SEND_TYPE,  
        ctypes.cast(strParams, ctypes.c_void_p),  # Convertir el string en puntero void*
        0,
        START,
        GUID  
    )
    return result

def pause_time()->int:
    hdsdk.Cmd_SetCountState.argtypes = [
        ctypes.c_int,       # nSendType
        ctypes.c_void_p,    # pStrParams (puntero a string)
        ctypes.c_int,       # nAreaIndex
        ctypes.c_int,       # nCmdType
        ctypes.c_void_p     # pDeviceGUID
    ]

    hdsdk.Cmd_SetCountState.restype = ctypes.c_int  
    strParams = ctypes.create_unicode_buffer(f"{IP_ADDRESS}:{PORT}")
    result = hdsdk.Cmd_SetCountState(
        SEND_TYPE,  
        ctypes.cast(strParams, ctypes.c_void_p),  # Convertir el string en puntero void*
        0,
        SUSPEND,
        GUID  
    )
    return result


def reset_time()->int:
    hdsdk.Cmd_SetCountState.argtypes = [
        ctypes.c_int,       # nSendType
        ctypes.c_void_p,    # pStrParams (puntero a string)
        ctypes.c_int,       # nAreaIndex
        ctypes.c_int,       # nCmdType
        ctypes.c_void_p     # pDeviceGUID
    ]

    hdsdk.Cmd_SetCountState.restype = ctypes.c_int  
    strParams = ctypes.create_unicode_buffer(f"{IP_ADDRESS}:{PORT}")
    result = hdsdk.Cmd_SetCountState(
        SEND_TYPE,  
        ctypes.cast(strParams, ctypes.c_void_p),  # Convertir el string en puntero void*
        0,
        RESET,
        GUID  
    )
    return result

def reset_card()->int:
    hdsdk.Cmd_RestartCard.argtypes = [
        ctypes.c_int,       # nSendType
        ctypes.c_void_p,    # pStrParams (puntero a string)
        ctypes.c_void_p     # pDeviceGUID
    ]

    hdsdk.Cmd_RestartCard.restype = ctypes.c_int  
    strParams = ctypes.create_unicode_buffer(f"{IP_ADDRESS}:{PORT}")
    result = hdsdk.Cmd_RestartCard(
        SEND_TYPE,  
        ctypes.cast(strParams, ctypes.c_void_p),  # Convertir el string en puntero void*
        GUID  
    )
    return result

def iniciar_conteo(tiempo_seg: int):
    pause_time()
    time.sleep(1)
    reset_time()
    time.sleep(1)
    start_time()
    time.sleep(tiempo_seg)
    pause_time()
    



#Example of use 
# SET NUMBER OF ANDEN
# set_value_anden(5)
# contador 
# iniciar_conteo(10)


# El area de un programa solo se actualiza cuando esta en el programa actual
# caso contrario hay bug, poor lo tanto
# en una pantalla dejare el nombre del anden
# y en otra pantalla el contador
