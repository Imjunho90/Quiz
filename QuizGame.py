from GameRecord import GameRecord
from Quiz import Quiz
import json
import os
import random
import datetime

class QuizGame:
    def __init__(self,file_name='state.json'):
        self.filename=file_name
        self.quizzes=[]
        self.high_score=0
        self.load_data()
        self.history=[]
        self.load_history()

        
        
    def default_data(self):
        initial_data=[
                        {"question": "파이썬에서 리스트에 요소를 추가하는 함수는?", "choices": ["add()", "append()", "insert()", "push()"], "answer": 2},
                        {"question": "파이썬의 창시자는?", "choices": ["Guido van Rossum", "Elon Musk", "Bill Gates", "James Gosling"], "answer": 1},
                        {"question": "다음 중 불변(Immutable) 자료형은?", "choices": ["list", "dict", "set", "tuple"], "answer": 4},
                        {"question": "출력 함수는?", "choices": ["input()", "print()", "write()", "echo()"], "answer": 2},
                        {"question": "논리 연산자 중 '그리고'를 뜻하는 것은?", "choices": ["or", "not", "and", "xor"], "answer": 3},
                        {"question": "문자열의 길이를 구하는 함수는?", "choices": ["size()", "len()", "count()", "length()"], "answer": 2},
                        {"question": "파이썬에서 주석을 작성할 때 쓰는 기호는?", "choices": ["//", "#", "/* */", "--"], "answer": 2},
                        {"question": "다음 중 반복문 키워드가 아닌 것은?", "choices": ["for", "while", "loop", "break"], "answer": 3},
                        {"question": "리스트의 마지막 요소를 꺼내면서 제거하는 메서드는?", "choices": ["pop()", "remove()", "del()", "cut()"], "answer": 1},
                        {"question": "정수형으로 변환하는 함수는?", "choices": ["str()", "float()", "int()", "bool()"], "answer": 3},
                        {"question": "다음 중 딕셔너리를 생성하는 올바른 표현은?", "choices": ["[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "{'a': 1}"], "answer": 4},
                        {"question": "함수를 정의할 때 사용하는 키워드는?", "choices": ["func", "def", "function", "define"], "answer": 2},
                        {"question": "7 // 2 의 결과값은?", "choices": ["3.5", "3", "4", "1"], "answer": 2},
                        {"question": "예외 처리를 위해 사용하는 키워드 조합은?", "choices": ["try - except", "do - catch", "if - else", "begin - rescue"], "answer": 1},
                        {"question": "range(5)가 생성하는 숫자의 범위는?", "choices": ["1~5", "0~5", "0~4", "1~4"], "answer": 3},
                        
                    ]
        self.quizzes=[Quiz(**q) for q in initial_data]
        self.high_score=0
        self.save_data()
        
    def load_data(self): #완료
        
        
        if not os.path.exists(self.filename):
            print("저장된 파일이 없습니다. 기본 퀴즈를 생성합니다.")
            self.default_data()
            return
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.high_score = data.get('high_score', 0)
            self.quizzes = [Quiz(**q) for q in data.get('quizzes', [])]

            if not self.quizzes:
                raise ValueError('퀴즈 목록이 비어 있음')

        except (json.JSONDecodeError, UnicodeDecodeError,
                AttributeError, TypeError, ValueError, OSError) as e:
            print(f'저장 파일이 손상되었습니다({e}). 기본 퀴즈를 생성합니다.')
            self.default_data()
            
            
    def save_data(self):
        data = {'high_score': self.high_score,
                'quizzes': [q.to_dict() for q in self.quizzes]}
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f'저장에 실패했습니다: {e}')
            
            
    def get_valid_value(self,prompt,is_numeric=False,minv=1,maxv=4): #완료
        
        while True:
            user_input=input(prompt).strip()
            if not user_input:
                print("입력값이 비었습니다. 다시 입력해주세요: ")
                continue
                
                
            # 정답 선택 or 문제
            if is_numeric:
                try:
                    user_input=int(user_input)
                        
                    if minv<=user_input<=maxv:
                        return user_input
                    else: print(f"숫자를 {minv}부터 {maxv}사이로 입력해주세요.")
                except ValueError:
                    print("숫자만 입력이 가능합니다. 다시 입력해주세요.")
            else:
                return user_input
                    
    
    def add_quiz(self): # 완료
        
        print('새 퀴즈를 입력해주세요')
        #질문
        question=self.get_valid_value('질문을 입력해주세요:')
        
        #옵션
        choices=[]
        for i in range(1,5):
            opt=self.get_valid_value(f'{i}번째 보기를 입력해주세요')
            choices.append(opt)
        #정답
        answer=self.get_valid_value('정답을 입력해주세요 (숫자 1~4):',True)

        while True:
            hint=self.get_valid_value('힌트를 입력하시겠습니까?(y/n):')
            if hint.lower()== 'y':
                hint_input=self.get_valid_value('힌트를 입력해주세요:') 
            elif hint.lower()=='n':
                hint_input=''
            else:
                print("y 또는 n을 입력해주세요.")
                continue
            break

        self.quizzes.append(Quiz(question,choices,answer,hint_input))
        self.save_data()
    
    def start_quiz(self):
        if not self.quizzes:
            print('등록된 퀴즈가 없습니다.')
            return
        
        
        total=len(self.quizzes)
        
        count=self.get_valid_value(f"몇 문제를 푸시겠습니까?(최대 {total}개):",True,1,total)
        
        quiz_list = random.sample(self.quizzes, count)
    
        score=0
        correct=0
        print('---퀴즈 게임 시작---')
        for q in quiz_list:
            q.show_quiz()
            
            use_hint=False
            if q.hint:
                while True:
                    choice=input("힌트를 보시겠습니까? (y/n):")
                    if choice.lower()=='y':
                        print(f'힌트: {q.hint}')
                        use_hint=True
                        break
                    elif choice.lower()=='n':
                        break
                    else:
                        print("y 또는 n을 입력해주세요.")
                

            user_ans=self.get_valid_value('정답을 입력해주세요:',True)
            if q.is_correct(user_ans): 
                
                if use_hint:
                    gain=5
                    print(f'정답입니다! +{gain}점')
                else:
                    gain=10
                    print(f'정답입니다! +{gain}점')
    
                score+=gain
                correct+=1
            else:
                if use_hint:
                    loss=-5
                    score+=loss
                    print(f'틀렸습니다. 정답은 {q.answer}번입니다. -5점')
                else:
                    print(f'틀렸습니다. 정답은 {q.answer}번입니다.')
                        
        print(f'\n게임 종료! {correct}/{len(self.quizzes)}문제 정답, 점수: {score}')
        
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record=GameRecord(now,len(quiz_list),score)
        
        self.history.append(record)
        self.save_history()
        
        if score>self.high_score:
            print(f'축하합니다! 최고 점수 경신! ({self.high_score} -> {score})')
            self.high_score=score
            self.save_data()
            
    def show_list(self):
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
            
        for i, r in enumerate(self.history):
            print(f'{i+1}. [{r.date}] {r.total}문제 중 {r.score}점')
            
        best=max(self.history,key=lambda x:x.score)
        print(f'최고 점수 기록: [{best.date}] {best.total}문제 중 {best.score}점')
        
    def save_history(self):
        data=[r.to_dict() for r in self.history]
        with open('history.json','w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
            
            
            
    def load_history(self):
        self.history=[]
        
        if not os.path.exists('history.json'):
            return
        with open('history.json','r',encoding='utf-8') as f:
            data=json.load(f)
            
        for d in data:
            record=GameRecord(**d)
            self.history.append(record)
            
    def run(self):
        while True:
            print("메뉴를 선택해 주세요")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가하기")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 보기")
            print("5. 퀴즈 삭제하기")
            print("6. 프로그램 종료")

            user_select=self.get_valid_value('숫자를 입력해 주세요:',True,1,7)
            
            if user_select==1:
                self.start_quiz()
            elif user_select==2:
                self.add_quiz()
            elif user_select==3:
                self.show_list()
            elif user_select==4:
                self.show_score()
            elif user_select==5:
                self.delete_quiz()
            elif user_select==6:
                print('프로그램을 종료합니다.')
                break

    def delete_quiz(self):
        if not self.quizzes:
            print('등록된 퀴즈가 없습니다.')
            return
        
        print('---등록된 퀴즈 목록---')
        for i,q in enumerate(self.quizzes):
            print(f'{i+1}. {q.question}')
        
        num=self.get_valid_value('삭제할 퀴즈 번호를 입력해주세요:',True,1,len(self.quizzes))
        removed=self.quizzes.pop(num-1)
        self.save_data()
        print(f'{removed.question} 퀴즈가 삭제되었습니다.')
            