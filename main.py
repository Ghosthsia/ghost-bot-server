from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/encrypt', methods=['GET'])
def encrypt():
    input_id = request.args.get('id')
    encrypted_id = Encrypt_ID(input_id)
    return jsonify({'encrypted_id': encrypted_id})

if __name__ == '__main__':
    app.run(debug=True)
