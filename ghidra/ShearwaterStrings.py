#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 

import ghidra.app.script.GhidraScript
import ghidra.program.model.listing

DEFAULT_START = 0x8072860
STRING_SIZE = 0x1C
STRING_NUMBER_END = 0x032D

def handle_string_container(address):

    listing = currentProgram.getListing()
    listing.clearCodeUnits(address, address.add(2 * STRING_SIZE), False)

    string_number = createWord(address)
    address = address.add(2)
    uk1 = createByte(address)
    address = address.add(1)
    uk2 = createByte(address)
    address = address.add(1)
    uk3 = createByte(address)
    address = address.add(1)
    uk4 = createByte(address)
    address = address.add(1)
    raw_string = createAsciiString(address, 0)
    address = address.add(raw_string.getLength())

    padding_len = STRING_SIZE - 6 - raw_string.getLength()
    for b in range(0,padding_len):
        if(getByte(address) != 0):
            print("Padding is not 0 at address: " + hex(address.getOffset()).rstrip("L") + " for string: " + raw_string.getValue())

        createByte(address)
        address = address.add(1)

    return raw_string.getValue().encode('ascii', 'ignore'), string_number.getValue().getValue()



f = open('ShearwaterStrings.txt', 'w')
address = askAddress("Strings Bank Starting Address", "Address (0 for default):")
if(address.getOffset() == 0):
    address = address.add(DEFAULT_START)

while(True):
    string, number = handle_string_container(address)
    f.write(hex(number).rstrip("L") + ";" + string + '\n')
    address = address.add(STRING_SIZE)
    if (number == STRING_NUMBER_END):
        exit()
