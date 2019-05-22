LOG_SETTINGS = {
    'version': 1,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'stream': 'sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/var/log/jarvis.log',
            'mode': 'a',
            'maxBytes': 10000000,
            'backupCount': 3,
        },
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    }
}


# General assistant settings
GENERAL_SETTINGS = {
    'assistant_name': 'Jarvis',
    'response_in_speech': False,
    'response_in_text': True
}

# Trigger words
TRIGGERING_WORDS = {
    'enable_jarvis': {'command': 'enable_jarvis', 'triggering_words': ['start', 'hi', 'jarvis']},
    'disable_jarvis': {'command': 'disable_jarvis', 'triggering_words': ['stop', 'shut down']},
    'open_browser': {'command': 'open_browser', 'triggering_words': ['open', 'do']},
    'tell_time': {'command': 'tell_time', 'triggering_words': ['time']},
    'tell_about': {'command': 'tell_about', 'triggering_words': ['about']},
    'current_weather': {'command': 'current_weather', 'triggering_words': ['weather']},
}

# Google API Speech recognition settings
# SpeechRecognition: https://pypi.org/project/SpeechRecognition/2.1.3
SPEECH_RECOGNITION = {
    'ambient_duration': 0.1,
    'pause_threshold': 1,  # minimum length silence (in seconds) at the end of a sentence
    'energy_threshold': 4000,  # microphone sensitivity, for loud places, the energy level should be up to 4000
    'dynamic_energy_threshold': False  # For unpredictable noise levels
}

# Google text to speech API settings
GOOGLE_SPEECH = {
    'lang': "en"
}

# Open weather map API conf settings
WEATHER_API = {
    'unit': 'celsius',
    'key': '2e63db2f8df7cc9ebd13a441d8b2eb8a'
}