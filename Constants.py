import os

TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')

football_headers = {
	"X-RapidAPI-Key": os.environ.get('X-RapidAPI-Key(footballAPI)'),
	"X-RapidAPI-Host": os.environ.get('X-RapidAPI-Host(footballAPI)')
}

# PORT = int(os.environ.get('PORT', 8443))