from datetime import datetime

def sample_responses(input_text):
    user_massage = str(input_text).lower()

    if user_massage in ("hello", "hi", "sup"):
        return "Hey! How's it going?"
    
    elif user_massage in ("who are you", "who are you?"):
        return "I am ABC bot!"

    elif user_massage in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Sorry, I dont understand"
