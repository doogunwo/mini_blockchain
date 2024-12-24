import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가
sys.path.append(os.path.join(project_root, 'utils'))  # utils 디렉토리 추가

from proof_of_work import ProofOfWork

def test_proof_of_work():
    # 작업 증명 난이도 설정
    difficulty = 4
    pow = ProofOfWork(difficulty)

    # 블록 데이터 및 이전 해시
    block_data = "Block Data"
    pre_hash = "0000abcd1234"

    # PoW 실행
    nonce, block_hash = pow.mine(block_data, pre_hash)
    print(f"Nonce: {nonce}")
    print(f"Block Hash: {block_hash}")

    # 검증
    assert block_hash.startswith('0' * difficulty), "PoW 실패: 난이도 조건 불충족"

if __name__ == "__main__":
    test_proof_of_work()
