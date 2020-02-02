import chess
import chess.engine 
#from stockfish import stockfish



engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\Zounon\Desktop\CodeFiles\FunChess\stockfish-11-win\Windows\stockfish_20011801_x64.exe")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    board

    
engine.quit()
