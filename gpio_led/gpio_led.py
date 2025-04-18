from pynq import Overlay
from pynq import MMIO

# Program bitstream to FPGA
overlay = Overlay('/home/xilinx/workspace/gpio_led.bit')

# Access to memory map of the AXI GPIO
ADDR_BASE = 0x41200000
ADDR_RANGE = 0x10000
gpio_obj = MMIO(ADDR_BASE, ADDR_RANGE)

# Write data to AXI GPIO
gpio_obj.write(0x0, 6)
