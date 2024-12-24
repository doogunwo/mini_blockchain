import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

# 필요한 모듈 가져오기
from block import Block  

from p2p import Node
import time

def test_p2p():

    node1 = Node("127.0.0.1", 5000)
    node1.start()

    node2 = Node("127.0.0.1", 5001)
    node2.start()

    node2.connect_to_peer("127.0.0.1",5000)

if __name__ == "__main__":
    test_p2p()