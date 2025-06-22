#!/usr/bin/env python3
"""Production server runner without file watcher."""

import os
from main import create_app

if __name__ == "__main__":
    app, socketio = create_app()
    # Run without debug mode to avoid file watcher restarts
    socketio.run(app, debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5002)))
