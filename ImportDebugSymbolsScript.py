# Use before any analysis!

from ghidra.program.model.address import Address
from ghidra.program.model.symbol import SourceType

def import_debug_symbols(file_path):
    current_program = getCurrentProgram()
    symbol_table = current_program.getSymbolTable()

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 3:
                address_str, _, symbol_name = parts[:3]
                address = current_program.getAddressFactory().getAddress(address_str)
                
                # Check if the symbol already exists
                existing_symbol = symbol_table.getPrimarySymbol(address)
                if existing_symbol is None:
                    # Create a new symbol
                    new_symbol = symbol_table.createLabel(address, symbol_name, SourceType.USER_DEFINED)
                    print("Imported symbol: {} at {}".format(symbol_name, address))
                else:
                    print("Symbol already exists: {} at {}".format(symbol_name, address))

# Change the file path to the location of your text file
file_path = "/path/to/your/debug_symbols.txt"
import_debug_symbols(file_path)
