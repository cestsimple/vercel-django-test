# example/views.py
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f'''
    <html>
        <body>
            <h1>Test deploying on vercel success!</h1>
            <p>The current time is {now}.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
