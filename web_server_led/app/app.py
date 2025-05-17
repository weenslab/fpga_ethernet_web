from pynq import Overlay, MMIO
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def program_fpga():
    global gpio_obj
    overlay = Overlay('/home/xilinx/workspace/gpio_led.bit')
    gpio_obj = MMIO(0x41200000, 0x10000)
    gpio_obj.write(0x0, 0x0)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def led_control():
    state = request.get_json(force=True)['state']
    print(state)

    if state == 'on':
        gpio_obj.write(0x0, 0xf)
    elif state == 'off':
        gpio_obj.write(0x0, 0x0)

    response = {
        'state': state
    }
    return jsonify(response)

@app.route('/status', methods=['GET'])
def get_status():
    if gpio_obj.read(0x0) == 0:
        state = 'off'
    else:
        state = 'on'

    response = {
        'state': state
    }
    return jsonify(response)

print(" * Programming the FPGA...")
program_fpga()
print(" * FPGA programming done")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
