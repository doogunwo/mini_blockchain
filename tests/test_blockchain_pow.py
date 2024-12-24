import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

# 필요한 모듈 가져오기
from blockchain import Blockchain

def test_blockchain_pow():
    blockchain = Blockchain(mining_interval=2)
    genesis_block = blockchain.chain[0]

    print("\nGenesis Block:")
    print(genesis_block.info_block())
    assert genesis_block.hash.startswith("0" * blockchain.difficulty), "Genesis Block PoW failed!"

    blockchain.mine_block()

    latest_block = blockchain.get_latest_block()
    print("\nLatest Block:")
    print(latest_block.info_block())
    assert latest_block.hash.startswith("0" * blockchain.difficulty), "New Block PoW failed!"

   
if __name__ == "__main__":
    test_blockchain_pow()
    