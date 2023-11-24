class User:
    def __init__(self):
        self.feedback = []
        self.math = {}
        self.analysis = {}

    def feed_form(self, form):
        count = 0
        ans = None
        i = form.get_question()
        for i in i:
            count += 1
            print(f"{count}.{i[0]}")
            if i[2] == "None":
                ans = self.get_result(i[1])
            else:
                number = 0
                for j in i[2]:
                    number += 1
                    print(f"{number}. {j}")
                ans = input("Ans: ")
                self.math[i[0]] = ans
            self.feedback += [[i[0], ans]]
        submit = input("To Submit press yes else press No ")
        return self.feedback

    def get_result(self, choice):
        match choice:
            case 3:
                return input("Ans: ")
            case 5:
                while True:
                    name = input("Ans: ")
                    if name.isalpha():
                        return name
                    else:
                        print("Re-enter the input Correctly..!")
            case 6:
                while True:
                    number = input("Ans: ")
                    if number.isdigit() and 9 < len(number) < 12:
                        return number
                    else:
                        print("Enter the correct Phone number ")
            case 7:
                while True:
                    mail = input("Ans: ").lower()
                    if mail.endswith("@gmail.com") or mail.endswith("@outlook.com") or mail.endswith("@yahoo.com"):
                        return mail
                    else:
                        print("Enter the correct mail")

    def get_math_analysis(self):
        return self.math

