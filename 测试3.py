class Singleton:
    __instance=None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return  cls.__instance
s=Singleton()
print(s)
s1=Singleton()
print(s1)




