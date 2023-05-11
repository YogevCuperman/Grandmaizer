class Profile:
    def __init__(self):
        self.name = None
        self.age = None
        self.id_number = None

    ### GETTERS ###
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_id_number(self):
        return self.id_number

    ### SETTERS ###
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_id_number(self, id):
        self.id_number = id