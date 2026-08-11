
from QuizGame import QuizGame

if __name__ == '__main__':
    game=QuizGame('state.json')
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print('\n입력이 중단되었습니다. 저장 후 종료합니다.')
        game.save_data()