class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class BrainF_ck_Error(Error):
    """
    InputFormatError: Input must be an integer value from 0 to 255
    """

class BrainF_ck():
    def __init__(self):
        self.memory = [0]
        self.now_pointa = 0
        self.exit = False
        self.count = 0
        self.k = 10000

    def brainf_ck_error_checker(self, n):
        try:
            n = ord(n)
        except:
            raise ValueError()
        else:
            if not (0 <= n <= 255):
                raise BrainF_ck_Error()
            else:
                return n

    # +の処理
    def plus(self):
        tmp = self.memory[self.now_pointa]
        self.memory[self.now_pointa] = tmp + 1 if not tmp + 1 > 255 else 0

    # -の処理
    def minus(self):
        tmp = self.memory[self.now_pointa]
        self.memory[self.now_pointa] = tmp - 1 if tmp - 1 >= 0 else 255
    # .の処理
    def period(self):
        print(chr(self.memory[self.now_pointa]), end='')

    # ,の処理
    def comma(self):
        try:
            self.memory[self.now_pointa] = self.brainf_ck_error_checker(input())
        except:
            print("0 ~ 255 の整数値を入力してください")
            self.exit = True

    # >の処理
    def more_than(self):
        self.now_pointa += 1
        if len(self.memory) <= self.now_pointa:
            self.memory += [0]

    # <の処理
    def less_than(self):
        self.now_pointa -= 1
        if self.now_pointa < 0:
            print('0未満のポインタを参照しようとしています')
            self.exit= True


    # [の処理
    def left_square_brackets(self):
        if not self.memory[self.now_pointa]:
            tmp, count = 1, self.count
            while True:
                count += 1
                if self.message[count] == '[':
                    tmp += 1
                elif self.message[count] == ']':
                    tmp -= 1

                if count == len(self.message) - 1 or not tmp:
                    self.count = count
                    break

    # ]の処理
    def right_square_brackets(self):
        tmp, count = 1, self.count
        while True:
            count -= 1
            if count < 0:
                self.exit = True
                self.count = 0
                break

            if self.message[count] == ']':
                tmp += 1
            elif self.message[count] == '[':
                tmp -= 1

            if not tmp:
                self.count = count - 1
                break

    # 実行
    def run(self, message):
        self.message = message
        while len(message) > self.count:
            order = message[self.count]

            if self.exit:
                break
            elif order == '.':
                self.period()
            elif order == ',':
                self.comma()
            elif order == '+':
                self.plus()
            elif order == '-':
                self.minus()
            elif order == '>':
                self.more_than()
            elif order == '<':
                self.less_than()
            elif order == '[':
                self.left_square_brackets()
            elif order == ']':
                self.right_square_brackets()

            self.count += 1
            self.k -= 1
            if self.k < 0:
                print('Over Flow')
                self.exit = True

# メインで実行する
if __name__ == '__main__':
    app = BrainF_ck()
    app.run(input())

