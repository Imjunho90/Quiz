

class quiz:
    def __init__(self,question,options,answer):
        self.question=question
        self.options=options
        self.answer=answer
        
    def to_dict(self):
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }

class QuizGame:
    def __init__(self,file_name=None):
        
        if not file_name:
            self.quizzes=[
                    {"question": "파이썬에서 리스트에 요소를 추가하는 함수는?", "options": ["add()", "append()", "insert()", "push()"], "answer": 2},
                    {"question": "파이썬의 창시자는?", "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "James Gosling"], "answer": 1},
                    {"question": "다음 중 불변(Immutable) 자료형은?", "options": ["list", "dict", "set", "tuple"], "answer": 4},
                    {"question": "출력 함수는?", "options": ["input()", "print()", "write()", "echo()"], "answer": 2},
                    {"question": "논리 연산자 중 '그리고'를 뜻하는 것은?", "options": ["or", "not", "and", "xor"], "answer": 3}
                ]
        else: self.quizzes=[]

    def get_valid_value(self,prompt,is_numeric=False):
        while True:
            user_input=input(prompt).strip()
            if not user_input:
                print("입력값이 비었습니다. 다시 입력해주세요")
                continue
            if is_numeric:
                try:
                    user_input=int(user_input)
                    
                    if 1<=user_input<=4:
                        return user_input
                    else: print("숫자를 1부터 4사이로 입력해주세요.")
                except ValueError:
                    print("숫자만 입력이 가능합니다. 다시 입력해주세요.")
            else:
                return user_input
    
    def add_quiz(self):
        
        print('새 퀴즈를 입력해주세요')
        #질문
        question=self.get_valid_value('질문을 입력해주세요')
        
        #옵션
        options=[]
        for i in range(1,5):
            opt=self.get_valid_value(f'{i}번째 보기를 입력해주세요')
            options.append(opt)
        #정답
        answer=self.get_valid_value('정답을 입력해주세요 (숫자 1~4)',True)
        
    
    def run(self):
        
        
        
        while True:
            
            print("메뉴를 선택해 주세요")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가하기")
            print("3. 종료")
                    
            try:
                user_select=int(input("번호 입력:").strip())
                if user_select=='':
                    print("다시 입력해 주세요")
                    continue
                    
            except ValueError:
                print("숫자만 입력 가능합니다.")
                continue
            
            if user_select==1:
                pass
            elif user_select==2:
                pass
            elif user_select==3:
                break
            else:
                print("다시 입력해 주세요")

            
            
            