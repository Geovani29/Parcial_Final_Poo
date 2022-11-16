class Usuario():
    def __init__(self) -> None:
        self.user_name = str
        self.password = str
        self.list_users = []
        self.list_pass = []

    def sign_in(self) -> None:
        self.user_name = input("User name:\n")
        self.list_users.append(self.user_name)
        self.password = input("Password:\n")
        self.list_pass.append(self.password)

    def login(self) -> None:
        self.user_name = input("User name:\n")
        if self.user_name in self.list_users:
            self.password = input("Password:\n")
            if self.password in self.list_pass:
                print("Welcome")
