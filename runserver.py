import os
from flashcard import app

if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_HOST', '5555'))
    except:
        PORT = 5555
    app.run(HOST, PORT)