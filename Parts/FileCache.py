import diskcache
import logging
from diskcache import FanoutCache


class FileCache:
    cache: FanoutCache

    def __init__(self, name, namespace="", default_expire: int = 86400):
        self.cache = FanoutCache(directory="./.cache/")
        self.namespace = namespace
        self.key = name
        self.expire = default_expire

    def key_name(self, key):
        return f"{self.namespace}_{key}"

    def set(self, dict_data, expire=None, key=None):
        if expire is None:
            expire = self.expire

        if key is None:
            key = self.key

        set_result = self.cache.set(key=self.key_name(key), value=dict_data, expire=expire)
        logging.info(f"File Cache set: key={key} expire={expire} dict_data={dict_data}")
        return set_result

    def get(self, default=None, key=None):
        if key is None:
            key = self.key

        get_result = self.cache.get(key=self.key_name(key), default=default)
        logging.info(f"File Cache get: default={default} key={key} get_result={get_result}")
        return get_result

    def rm(self, key=None):
        if key is None:
            key = self.key

        del_result = self.cache.delete(key=self.key_name(key))
        logging.info(f"File Cache rm: key={key} del_result={del_result}")
        return del_result

    def get_or_call(self, fun, args: tuple, expire=None, key=None):
        if key is None:
            key = self.key

        cache_hit = True
        data = self.get(default=None)

        if data is None:
            cache_hit = False
            data = fun(*args)
            self.set(data, expire=expire, key=key)

        logging.info(f"File Cache get_or_call: "
                     f"fun={fun.__name__} args={args} key={key} expire={expire} cache_hit={cache_hit} data={data}")
        return data


if __name__ == '__main__':
    fc = FileCache(name="hello", namespace="hihi")
    print(fc.set(dict_data={"aa": "bb"}))
    print(fc.get())
    print(fc.rm())


    def test(a1, a2, a3):
        print("call")
        return {"1": a1, "2": a2, "3": a3}


    print(fc.get_or_call(test, ("hi", "bye", "hello")))
