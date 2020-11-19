from app import app


HOST = '127.0.0.1'
PORT = 8094


if __name__ == '__main__':
    app.run(HOST, port=PORT, debug=True)
