class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            cls._instances[cls].num_connections = 0

        # Increase the number of connections
        cls._instances[cls].num_connections += 1
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):

    def __init__(self):
        """
        The init method of this class is only going to be called once.
        """
        self.num_connections = 0 

    def connect(self):
        self.connection = "Database Connected"
        self.connected = False

    def disconnect(self):
        self.connection = "Database Disconnected"
        self.connected = False

    def get_connection_status(self):
        return self.connected

    def some_business_logic(self):
        pass


if __name__ == '__main__':
    s1 = Database()
    s2 = Database()

    if id(s1) == id(s2):
        print("this thing is working as expected")
    else:
        print("this is actually not working")


    s3 = Database()

    print("Number of connections: ", s1.num_connections, s2.num_connections, s3.num_connections)
