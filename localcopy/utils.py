import hashlib


def translate_path(path, query):
    query = hashlib.md5(query.encode()).hexdigest()
    path = path.split("/")
    path.append(path[-1])
    path[-2] = query
    return "/".join(path)