from __future__ import print_function
import asyncio
import chess
import chess.engine
import chess.svg
import time
import base64
import os
from state import State
from flask import Flask, render_template, request, Response

board = chess.Board
s = State()


def to_svg(s):
    return base64.b64encode(chess.svg.board(board=s.board).encode('utf-8')).decode('utf-8')


@app.route("/")
def hello():
    ret = open("index.html").read()
    return ret.replace('start', s.board.fen())


async def main():
    transport, engine = await chess.engine.popen_uci(
        r"C:\Users\Zounon\Desktop\CodeFiles\FunChess\stockfish-11-win\Windows\stockfish_20011801_x64.exe")

    board = chess.Board()
    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=0.1))
        print(result.move)
        board.push(result.move)
        print(board)

    await engine.quit()


asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())

if __name__ == "__main__":
    if os.getenv("SELFPLAY") is not None:
        s = State()
        while not s.board.is_game_over():
            result = await engine.play(board, chess.engine.Limit(time=0.1))
            print(result.move)
            board.push(result.move)
            print(board)
            print(s.board)
        print(s.board.result())
    else:
        app.run(debug=True)
