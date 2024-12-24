import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

# 필요한 모듈 가져오기
from blockchain import Blockchain
from p2p import Node
import threading
import time

def test_block_sync():
    node1 =Node("127.0.0.1", 5000)
    node1.blockchain = Blockchain()
    node1.start()

    def node1_mine():
        while 1:
            node1.blockchain.mine_block()
            node1.broadcast_block(node1.blockchain.get_latest_block())
            time.sleep(2)

    threading.Thread(target=node1_mine, daemon=True).start()


    node2 = Node("127.0.0.1", 5001)

    for block in node1.blockchain.chain:
        print(block.info_block())

    for block in node2.blockchain.chain:
        print(block.info_block())

test_block_sync()
