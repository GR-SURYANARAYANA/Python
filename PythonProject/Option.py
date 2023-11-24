class Answer:
    def __init__(self, choice=None):
        self.choice = choice

    def answer_type(self, choice):
        match choice:
            case 1:
                return self.option_type()
            case 2:
                return self.scaling_type()
            case 4:
                return self.option_type()
            case _:
                return "None"

    def option_type(self):
        count = 0
        answer = []
        while True:
            count += 1
            option = input(f"Enter the option {count} : ")
            answer += [option]
            ch = input("To add more option type Y or N to End ")
            if ch.upper() == "N":
                break
        return answer

    def scaling_type(self):
        return ['Poor', "Good", "Average", "Satisfactory", "Excellent"]