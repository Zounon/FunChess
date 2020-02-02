import asyncio 
import chess
import chess.engine

async def main():
    transport, engine = await chess.engine.popen_uci(r"C:\Users\Zounon\Desktop\CodeFiles\FunChess\stockfish-11-win\Windows\stockfish_20011801_x64.exe")

    board = chess.Board()
    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=0.1))
        print(result.move)
        board.push(result.move)
        print(board)

    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())