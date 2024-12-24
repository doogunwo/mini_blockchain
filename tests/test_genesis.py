import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

# 필요한 모듈 가져오기
from block import Block  # blockchain/block.py에서 Block 클래스 가져오기

def test_blocks():
    difficulty = 4
    genesis_block = Block(0, "Genesis Block", "0",difficulty)
    print("Genesis block : ", genesis_block.info_block())

    second_block = Block(1, "Second Block data", genesis_block.hash, difficulty)
    print("\nSecond block :", second_block.info_block())
   
if __name__ == "__main__":
    test_blocks()
