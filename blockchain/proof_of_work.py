import hashlib

class ProofOfWork:
    def __init__(self, difficulty):
        """
        pow init
        difficulty : 작업 증명 난이도 
        """

        self.difficulty = difficulty
    
    def mine(self, block_data, pre_hash):
        """
        block_data : 블록 데이터
        pre_hash : 이전 블록 해시 값
        return 유효한 nonce 값과 블록 해시
        """
        
        nonce = 0
        while 1:
            block_string = f"{block_data}{pre_hash}{nonce}"
            block_hash = hashlib.sha256(block_string.encode()).hexdigest()

            if block_hash.startswith('0' * self.difficulty):
                return nonce, block_hash

            
            nonce = nonce + 1