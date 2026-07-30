
import os
import json

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
    def __init__(self,file_name='state.json'):
        self.filename=file_name
        self.quizzes=[]
        self.high_score=0
        self.load_data()

        
        
        
    def load_data(self): #완료
        if os.path.exists(self.filename):
            with open(self.filename,'r',encoding='utf-8') as f:
                data=json.load(f)
                self.high_score=data.get('high_score',0)
                self.quizzes=[quiz(**q) for q in data.get('quizzes',[])]
        else:
            initial_data=[
                                {"question": "파이썬에서 리스트에 요소를 추가하는 함수는?", "options": ["add()", "append()", "insert()", "push()"], "answer": 2},
                                {"question": "파이썬의 창시자는?", "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "James Gosling"], "answer": 1},
                                {"question": "다음 중 불변(Immutable) 자료형은?", "options": ["list", "dict", "set", "tuple"], "answer": 4},
                                {"question": "출력 함수는?", "options": ["input()", "print()", "write()", "echo()"], "answer": 2},
                                {"question": "논리 연산자 중 '그리고'를 뜻하는 것은?", "options": ["or", "not", "and", "xor"], "answer": 3}
                            ]
            self.quizzes=[quiz(**q) for q in initial_data]
            self.save_data()
    def save_data(self): #완료
        
        data={
            'high_score':self.high_score,
            'quizzes':[q.to_dict() for q in self.quizzes]
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
    def get_valid_value(self,prompt,is_numeric=False,menu=False): #완료
        
        if not menu:
            while True:
                user_input=input(prompt).strip()
                if not user_input:
                    print("입력값이 비었습니다. 다시 입력해주세요")
                    continue
                
                
                # 정답 선택 or 문제
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
        else:
            while True:
                user_input=input(prompt).strip()
                if not user_input:
                    print("입력값이 비었습니다. 다시 입력해주세요")
                    continue
                if is_numeric:
                    try:
                        user_input=int(user_input)
                        
                        if 1<=user_input<=5:
                            return user_input
                        else: print("숫자를 1부터 5사이로 입력해주세요.")
                    except ValueError:
                        print("숫자만 입력이 가능합니다. 다시 입력해주세요.")

                    
    
    def add_quiz(self): # 완료
        
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
        
        self.quizzes.append(quiz(question,options,answer))
        self.save_data()
    
    def start_quiz(self):
        if not self.quizzes:
            print('등록된 퀴즈가 없습니다.')
            return
        score=0
        
        print('---퀴즈 게임 시작---')
        for q in self.quizzes:
            print(f'\nQ:{q.question}')
            for i,opt in enumerate(q.options):
                print(f'{i+1} {opt}')
            try:
                user_ans=self.get_valid_value('정답을 입력해주세요',True)
                if user_ans==q.answer:
                    print('정답입니다! +10점')
                    score+=10
                else:
                    print(f'틀렸습니다. 정답은 {q.answer}번입니다.')
                    
            except ValueError:
                print("숫자를 입력해야 합니다. 오답 처리됩니다.")
        
        print(f'\n게임 종료! 당신의 점수: {score}')
        if score>self.high_score:
            print(f'축하합니다! 최고 점수 경신! ({self.high_score} -> {score})')
            self.high_score=score
            self.save_data()
    def show_quiz(self):
        
        if not self.quizzes:
            print('등록된 퀴즈가 없습니다.')
            return
        
        print('\n---퀴즈 목록---')
        for i,q in enumerate(self.quizzes):
            print(f'{i+1}.{q.question}')
            
            
    def show_score(self):
        print('---최고 점수---')
        
        if self.high_score>0:
            print(f'현재 최고 점수: {self.high_score}점')
        else:
            print('아직 플레이 기록이 없습니다.')
            print('퀴즈를 풀어보세요.')
        
    def run(self):
        
        
        
        while True:
            
            print("메뉴를 선택해 주세요")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가하기")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 보기")
            print("5. 종료")

        
                    
            user_select=self.get_valid_value('숫자를 입력해 주세요:',True,True)
            
            if user_select==1:
                self.start_quiz()
            elif user_select==2:
                self.add_quiz()
            elif user_select==3:
                self.show_quiz()
            elif user_select==4:
                self.show_score()
            elif user_select==5:
                print('프로그램을 종료합니다.')
                break
            else:
                print("다시 입력해 주세요")

            
            
if __name__ == '__main__':
    game=QuizGame('state.json')
    game.run()