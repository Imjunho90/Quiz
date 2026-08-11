class Quiz:
    def __init__(self,question,choices,answer,hint=''):
        self.question=question
        self.choices=choices
        self.answer=answer
        self.hint=hint
        
    def show_quiz(self):
        print(f'{self.question}\n\n')
        for i,opt in enumerate(self.choices):
            print(f'{i+1}.{opt}')
    
            
    def is_correct(self, user_ans):
        return user_ans == self.answer


    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            'hint': self.hint
        }
        


