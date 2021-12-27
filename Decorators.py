from functools import wraps

translation = {
    'samosa':{
        'en':'can you buy me a samosa ?',
        'ta':'எனக்கு சமோசா வாங்கித் தர முடியுமா ?',
        'hi':'क्या तुम मेरे लिए समोसा खरीद सकते हो ?'
    }
}

def transalator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        msg, lang = function(*args, **kwargs)
        return translation[msg][lang]
    return wrapper

@transalator
def say(lang='en'):
    msg = 'samosa'
    return msg, lang

print(say())