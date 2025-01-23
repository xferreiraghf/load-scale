from flask import Flask, jsonify
import os
import subprocess

app = Flask(__name__)
filename = 'C:/balanca/PesoBal.BAL'
vbs_file = 'script.vbs'
exe_file = 'C:/balanca/vbpBalanca.exe'  

@app.route('/load-scale')
def read_file():

    subprocess.run([exe_file], shell=True)
    
    subprocess.run(['cscript.exe', vbs_file], shell=True)

    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read().rstrip('\n')
            file.close()
        return jsonify({'unit': "kg", 'value': data})
    else:
        return jsonify({'error': 'Arquivo nao encontrado'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
