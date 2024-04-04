from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Date and Time</title>
        </head>
        <body>
            <h1>Current Date and Time:</h1>
            <p>{current_time}</p>
            <button onclick="getData()">Get Data</button>

            <script>
                function getData() {{
                    // Here you can add your JavaScript code to fetch data or perform any other action
                    alert("You clicked the 'Get Data' button!");
                }}
            </script>
        </body>
        </html>
        """

        self.wfile.write(html_content.encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
