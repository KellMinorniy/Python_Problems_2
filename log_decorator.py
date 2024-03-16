import time
import os
import functools

def function_logger(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not os.path.exists(log_file_path):
                with open(log_file_path, 'w') as file:
                    pass
            
            start_time = time.time()
            with open(log_file_path, 'a') as file:
                file.write(f"{func.__name__}\n")
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"{args}\n")
            
            result = func(*args, **kwargs)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            with open(log_file_path, 'a') as file:
                file.write(f"{result}\n")
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"{elapsed_time:.2f} seconds\n\n")
            
            return result
        return wrapper
    return decorator

@function_logger('test.log')
def greeting_format(name):
    return f'Hello {name}!'

print(greeting_format('Artem'))