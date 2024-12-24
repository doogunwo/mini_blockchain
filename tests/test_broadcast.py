import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

from blockchain import Blockchain
from p2p import Node
import time
import threading

def test_broadcast_block():
    node1 = Node("127.0.0.1", 5000)
    node1.blockchain = Blockchain()
    node1.start()
    
    def node1_mine():
        while 1:
            node1.blockchain.mine_block()
            node1.broadcast_block(node1.blockchain.get_latest_block())
            time.sleep(2)
    mining_thread = threading.Thread(target=node1_mine, daemon=True)
    mining_thread.start()
    


if __name__ == "__main__":
    test_broadcast_block()
