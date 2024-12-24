import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

# 필요한 모듈 가져오기
from block import Block  

def test_blocks():
   blockchain = Blockchain()

    # 초기 블록체인 상태 출력
    print("\nInitial Blockchain:")
    for block in blockchain.chain:
        print(block.info_block())

    # 트랜잭션 없이 블록 생성
    blockchain.mine_block()

    # 다시 블록 생성
    blockchain.mine_block()

    # 결과 출력
    print("\nBlockchain After Mining Empty Blocks:")
    for block in blockchain.chain:
        print(block.info_block())
   
if __name__ == "__main__":
    