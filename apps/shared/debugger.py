def debugger(func):
    from django.db import connection

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("-" * 30)
        for query in connection.queries:
            print(query["sql"])
        print("-" * 30)
        return result

    return wrapper
