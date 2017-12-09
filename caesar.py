"""
Main Caesar Cipher
"""
class CaesarCipher:
    def __init__(self, seed="abcdefghijklmnopqrstuvwxyz"):
        self.__seed_in_space = (seed.find(" ") != -1)
        self.__seed_list = tuple(seed)
        self.__seed_num = len(self.__seed_list)

    """
    1. Convert string data to seed number
    """
    def __get_seed_num_list(self, data):
        num_list = []
        for data_char in tuple(data):
            num = 0
            for seed_char in self.__seed_list:
                if (data_char == seed_char):
                    num_list.append(num)
                    break
                elif ((not(self.__seed_in_space)) & (data_char == " ")):
                    num_list.append(-1)
                    break
                else:
                    num += 1
        return tuple(num_list)

    """
    2. Move seed number
    """
    def __move_str(self, move_num, num_list):
        change_num = []
        for num in num_list:
            if (num != -1):        
                new_num = num + move_num
                if (new_num >= self.__seed_num):
                    new_num = new_num - self.__seed_num
                elif (new_num < 0):
                    new_num = self.__seed_num + new_num
                change_num.append(new_num)
            else:
                change_num.append(-1)

        return tuple(change_num)

    """
    3. Convert seed number to string data
    """
    def __convert_num_to_str(self, num_list):
        str_data = ""
        for num in num_list:
            if (num == -1):
                str_data += " "
            else:
                str_data += self.__seed_list[num]
        
        return str_data

    """
    data: String data
    move_num: Move string number
    """
    def GetMoveString(self, data, move_num):
        num_list = self.__get_seed_num_list(data)
        num_list = self.__move_str(move_num, num_list)
        
        return self.__convert_num_to_str(num_list)

    def GetMoveStringAll(self, data):
        str_list = []
        for i in range(self.__seed_num):
            str_list.append(self.GetMoveString(data, i))
        
        return tuple(str_list)

        