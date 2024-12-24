import hashlib
import time

from proof_of_work import ProofOfWork

class Block:
    def __init__(self, index, txs, pre_hash, difficulty):
        """
        블록 클래스
        index : 블록번호":"
        data : 블록 저장 데이터
        pre_hash : 이전 블록 해시 값
        """
        self.index = index
        self.timestamp = time.time()
        self.pre_hash = pre_hash
        self.difficulty = difficulty
        self.txs = txs
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        현재 블록의 해시 값 계산
        SHA256 해시 값 생성
        """
        block_string = f"{self.index}{self.txs}{self.pre_hash}{self.timestamp}{self.difficulty}"
        return hashlib.sha256(block_string.encode()).hexdigest() 
      
    def info_block(self):
        """
        블록 정보 반환
        """
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "txs": self.txs,
            "pre_hash": self.pre_hash,
            "difficulty": self.difficulty,
            "hash": self.hash,
        }    
