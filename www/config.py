import config_default


class Dict(dict):
    '''
    simply dict but support access as x.y style
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k,v in zip(names,values):
            self[k] = v


    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribut '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def toDict(d):
    D = Dict()
    for k,v in d.items():
        D[k] = toDict(v) if isinstance(v,dict) else v
    return D


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
                # v.update(override[k])
                # r[k] = v
            else:
                r[k] = override[k]
        else:
            r[k] = v

    return r

configs = config_default.configs
#print(configs)
try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass
configs = toDict(configs)
#print(configs)

