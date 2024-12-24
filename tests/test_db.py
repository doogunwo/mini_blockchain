import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가
from blockchain import Blockchain
sys.path.append(os.path.join(project_root, 'utils'))  # utils 디렉토리 추가

def test_block():
   blockchain = Blockchain()

 


if __name__ == "__main__":
    test_block()
