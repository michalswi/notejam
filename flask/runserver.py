from notejam import app
from notejam.config import DevelopmentConfig
import os

APP_PORT = os.environ.get("APP_PORT", 5000)

app.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=APP_PORT)
