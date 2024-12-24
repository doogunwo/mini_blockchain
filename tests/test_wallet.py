import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

# 필요한 모듈 가져오기
from wallet import Wallet

def test_wallet():
    # 지갑 생성
    wallet = Wallet(wallet_dir="../wallet")
    print("Wallet Address:", wallet.get_address())

    # 트랜잭션 데이터
    message = "Transaction: Alice -> Bob (50 BTC)"

    # 서명 생성
    signature = wallet.sign_transaction(message)
    print("\nSignature:", signature)

    # 서명 검증
    is_valid = Wallet.verify_signature(
        wallet.public_key.to_string(), message, signature
    )
    print("\nSignature Valid:", is_valid)

if __name__ == "__main__":
    test_wallet()
