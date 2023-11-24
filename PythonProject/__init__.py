from PythonProject.Option import Answer
from PythonProject.Text import Style
from PythonProject.User import User

style = Style()


class Form:

    def __init__(self, title=None):
        self.title = title
        self.count = 0
        self.question = []
        self.description = None
        self.math_question = {}
        self.math_analysis = {}
        self.responsive = []

    def create_form(self, feedback_id):
        print("-" * 50)
        print(f"{style.bold_start()}Create the Survey Template{style.bold_end()}")
        print(
            f"{style.italic_start()}Feedback Id{style.italic_end()}:{style.bold_start()}{feedback_id}{style.bold_end()}")
        print("-" * 50)
        self.title = input(f"{style.italic_start()}Title          : ")
        self.description = input("Description/Aim:")
        print("-" * 50, style.italic_end())
        self.form_question()

    def choice_template(self):
        print("-" * 50)
        print(
            f"{style.bold_start()}Choose The type of Answer Expected After Every Question by number{style.bold_end()}")
        # print("Expected Answer is of : ")
        print("1. Choose one Option Type")
        print("2. Linear Scale 0 to 5 type ")
        print("3. Short or Long Answer Type ")
        print("4. Choose Multi Option Type ")
        print("5. Person Name Type ")
        print("6. Mobile Number Type ")
        print("7. Mail Type (@)")
        print("-" * 50)
        print("Type The question below ")

    def form_question(self):
        try:
            self.count += 1
            n = int(input("Enter the number of Question to Form : "))
            self.choice_template()
            for i in range(n):
                question = input(f"{i + 1}.")
                question_type = self.get_type()
                ans_type = Answer()
                result = ans_type.answer_type(question_type)
                self.question += [[question, question_type, result]]
                self.check_math(question, question_type, result)
                print("-" * 50)
        except Exception:
            print("Please Enter the valid Input...!")

    def check_math(self, question, question_type, result):
        if question_type == 1 or question_type == 2:
            self.math_analysis[question] = [0] * (len(result) + 1)
            self.math_question[question] = result

    def add_question(self):
        while True:
            self.choice_template()
            question = input("Enter the Question to update : ")
            question_type = self.get_type()
            ans_type = Answer()
            result = ans_type.answer_type(question_type)
            while True:
                ch = input("Type Yes to change and No to Exit ")
                if ch.upper() == "YES":
                    self.question += [[question, question_type, result]]
                    self.check_math(question, question_type, result)
                    return
                elif ch.upper() == "NO":
                    return
                else:
                    print("Invalid Choice...!")

    def update_question(self):
        self.choice_template()
        while True:
            num = int(input("Enter the question to Update ? "))
            if len(self.question) >= num > 0:
                break
            else:
                print("Invalid Question Number ")
        print("-" * 50)
        print("Enter updated Question Below:  ")
        question = input(f"{num}.")
        question_type = self.get_type()
        ans_type = Answer()
        result = ans_type.answer_type(question_type)
        while True:
            ch = input("Type Yes to Update and No to Exit ")
            if ch.upper() == "YES":
                self.question[num - 1] = [question, question_type, result]
                return
            elif ch.upper() == "NO":
                return
            else:
                print("Invalid Choice...!")

    def remove_question(self):
        while True:
            num = int(input("Enter the question to Update ? "))
            if len(self.question) > num > 0:
                while True:
                    ch = input("Type Yes to Remove and No to Exit ")
                    if ch.upper() == "YES":
                        self.question.pop(num - 1)
                        return
                    elif ch.upper() == "NO":
                        return
                    else:
                        print("Invalid Choice...!")

    def get_feedback(self):
        print("-" * 50)
        print(f"{style.bold_start()}Welcome to {self.title}{style.bold_end()}")
        print(f"{style.italic_start()}{self.description}{style.italic_end()}")
        print("-" * 50)
        person = User()
        feedback = person.feed_form(self)
        self.responsive += [[feedback]]
        for i in feedback:
            if i[0] in self.math_analysis:
                value = self.math_analysis[i[0]]
                value[int(i[1])] += 1
                self.math_analysis[i[0]] = value
        # for i in feedback:
        #     for j in i:
        #         if i[0] in self.math_analysis:
        #             j[int(i[1])] += 1

    def get_responses(self):
        print("-" * 50)
        print(f"{style.bold_start()}Response of  {self.title} Survey is As follows {style.bold_end()}")
        print(f"{style.italic_start()}{self.description}{style.italic_end()}")
        print("-" * 50)
        for i in self.responsive:
            count = 1
            for j in i:
                print(f"Person  Responded : {count}")
                for k in j:
                    print(k[0])
                    print(f"Ans : {k[1]}")
                count += 1

    def form_analysis(self):
        print(f"Number of Question Framed  : {len(self.question)}")
        print(f"Number of Person Responded : {len(self.responsive)}")
        for i in self.math_analysis.keys():
            count = 0
            # print(f"{i} ---> {self.math_analysis[i]}")
            print(f"The Response of the \"{i}\" are as follows ")
            ls = self.math_analysis[i]
            people_attempted = sum(ls)
            # print(ls)
            most_responded = None
            for j in range(len(ls) - 1):
                response = ls[j + 1]
                percentage = ((ls[j + 1] / people_attempted) * 100)
                option = self.math_question[i][j]
                print(
                    f"{option}".ljust(10), f"Total Response {int(ls[j + 1])}/ {people_attempted}".ljust(20), f"percentage of people opted:{round(percentage,2)}%")

    def get_type(self):
        try:
            while True:
                choice = int(input("Choice : "))
                if 0 < choice < 8:
                    return choice
                else:
                    print("Invalid Choice Made By The User ")
        except Exception:
            print("Enter the correct Choice ")
            return self.get_type()

    def set_title(self, title):
        self.title = title

    def get_question(self):
        return self.question

    def set_description(self, description):
        self.description = description
