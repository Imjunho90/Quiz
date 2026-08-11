class GameRecord:
    def __init__(self,date,total,score):
        self.date=date
        self.total=total
        self.score=score
        
    def to_dict(self):
        return {
            "date": self.date,
            "total": self.total,
            "score": self.score
        }