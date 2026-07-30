

class Quiz:
    def __init__(self):
        pass
    
    def run(self):
        
        
        
        while True:
            
            print("메뉴를 선택해 주세요")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가하기")
            print("3. 종료")
                    
            try:
                user_select=int(input("번호 입력:"))
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

            
            
            