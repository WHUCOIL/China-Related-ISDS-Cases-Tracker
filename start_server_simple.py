#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple HTTP server - Alternative version
"""

import http.server
import socketserver
import os

PORT = 8000

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n{'='*60}")
        print(f"Server started successfully!")
        print(f"{'='*60}")
        print(f"\nServer running at: http://localhost:{PORT}")
        print(f"\nOpen in browser:")
        print(f"  http://localhost:{PORT}/case_data.html")
        print(f"\nPress Ctrl+C to stop the server\n")
        print(f"{'='*60}\n")
        
        httpd.serve_forever()
except OSError as e:
    if e.errno == 10048:
        print(f"\n❌ Error: Port {PORT} is already in use!")
        print(f"\nTry one of these solutions:")
        print(f"1. Close other applications using port {PORT}")
        print(f"2. Use a different port (edit PORT in this script)")
        print(f"3. Find and close the process:")
        print(f"   Windows: netstat -ano | findstr :{PORT}")
    else:
        print(f"\n❌ Error: {e}")
except KeyboardInterrupt:
    print("\n\n✓ Server stopped.")
except Exception as e:
    print(f"\n❌ Unexpected error: {e}")
    import traceback
    traceback.print_exc()


