

class Quiz:
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

    
    def add_quiz(self,question,options,answer):
        
        
    
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

            
            
            