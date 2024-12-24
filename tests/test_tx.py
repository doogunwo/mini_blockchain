import sys
import os

# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가

# 필요한 모듈 가져오기
from transaction import Transaction  # blockchain/block.py에서 Block 클래스 가져오기

def test_transaction_address():
    
   tx1 = Transaction("Alice", "Bob", 50)
   tx2 = Transaction("Bob","charlie", 25)
   print(tx1)
   print(tx2)

if __name__ == "__main__":
    test_transaction_address()
