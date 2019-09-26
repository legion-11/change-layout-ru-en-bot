import os
from app import app, bot

print(1)
if __name__ == "__main__":
    print(0)
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
