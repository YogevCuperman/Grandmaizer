class Profile:
    def __init__(self):
        self.name = None
        self.age = None
        self.id_number = None
        self.problem = None
        self.additional_data = []

    ### GETTERS ###
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_id_number(self):
        return self.id_number

    def get_problem(self):
        return self.problem

    def get_additional_data(self):
        return self.additional_data

    ### SETTERS ###
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_id_number(self, id):
        self.id_number = id

    def set_problem(self, problem):
        self.problem = problem

    def add_additional_data(self, data):
        self.additional_data.append(data)
