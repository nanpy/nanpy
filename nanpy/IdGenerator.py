namespaceid = {}

def generate(namespace):
    try:
        namespaceid[namespace] = namespaceid[namespace] + 1
        return namespaceid[namespace]
    except KeyError:
        namespaceid[namespace] = 0;
        return namespaceid[namespace];
