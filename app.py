from datetime import datetime

def generate_html(current_time):
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
    </body>
    </html>
    """
    return html_content

def main():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    html_content = generate_html(current_time)
    print(html_content)

if __name__ == "__main__":
    main()