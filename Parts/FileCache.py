import diskcache
from diskcache import FanoutCache


class FileCache:
    cache: FanoutCache

    def __init__(self, name, namespace="", default_expire: int = 86400):
        self.cache = FanoutCache(directory="./.cache/")
        self.key = f"{namespace}_{name}"
        self.expire = default_expire

    def set(self, dict_data, expire=None):
        if expire is None:
            expire = self.expire

        return self.cache.set(key=self.key, value=dict_data, expire=expire)

    def get(self, default=None):
        return self.cache.get(key=self.key, default=default)

    def rm(self):
        return self.cache.delete(key=self.key)

    def get_or_call(self, fun, args: tuple, expire=None):
        data = self.get(default=None)

        if data is None:
            data = fun(*args)
            self.set(data, expire=expire)

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

