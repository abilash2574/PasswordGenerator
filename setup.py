import string, secrets, random

class Setup:
    # This will initialize all the data needed for getting the values.
    def __init__(self, abc):
        self.abc = abc
    __secret_generator = secrets.SystemRandom()
    __system_data = [string.ascii_letters, "!@#$%&"]
    # This method will be used to get the values needed.

    # def __get_values(self):
    #     print("Enter the length of Password:")
    #     self.pass_length = int(input())
    #     print("Enter the number of digits to include:")
    #     self.digit_length = int(input())
    #     print("Enter the number of special characters to include:")
    #     self.special_length = int(input())
    #     return (self.pass_length-(self.digit_length + self.special_length), self.digit_length, self.special_length)

    # This is the method that creates the password
    def __generator(self, pass_user_data):
        self.__user_data = pass_user_data
        self.__pass_var = []
        for i in range(self.__user_data[0]):                            # For choosing Ascii Letters
            self.__pass_var.append(str(self.__secret_generator.choice(self.__system_data[0])))
        for i in range(self.__user_data[1]):                            # For choosing random integers between 0 to 9
            self.__pass_var.append(str(self.__secret_generator.randint(0,9)))
        for i in range(self.__user_data[2]):
            self.__pass_var.append(str(self.__secret_generator.choice(self.__system_data[1])))
        # Shuffling the result just to make it random
        random.shuffle(self.__pass_var)
        # Now we have to return this as a string using the join() method
        return(''.join(self.__pass_var))

    def get_password(self):
        self.temp = self.__generator(self.abc)
        return (self.temp)
