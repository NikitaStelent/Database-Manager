from datetime import datetime

def make_log(func):
    def wrapper(*args, **kwargs):
        with open('logs/log.csv', 'a', encoding='utf-8') as log:
            log.writelines(
                f'{datetime.now().strftime("%d-%m-%Y %H:%M")} ; {func.__name__} ; {func.__doc__}\n')
        return func(*args, **kwargs)
    return wrapper
