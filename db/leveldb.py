import plyvel
import json

class Leveldb:
    def __init__(self, path="./db/blockchain_db"):
        """
        초기화 
        """
        self.db = plyvel.DB(path, create_if_missing=True)

    def save_block(self, block):

        block_key = f"block_{block.index}".encode()
        block_data = json.dumps(block.__dict__).encode()
        self.db.put(block_key, block_data)
        self.db.put(b"last_block",block_data)
        print(f"Block {block.index} saved to db.")
    
    def get_last_block(self):
        """
        최신 블록 가져오기
        :return: 최신 블록 데이터 (딕셔너리 형태)
        """
        last_block_data = self.db.get(b"last_block")
        if last_block_data:
            return json.loads(last_block_data.decode())
        return None

    def get_block_by_index(self, index):
        """
        특정 인덱스의 블록 가져오기
        :param index: 블록 인덱스
        :return: 블록 데이터 (딕셔너리 형태)
        """
        block_key = f"block_{index}".encode()
        block_data = self.db.get(block_key)
        if block_data:
            return json.loads(block_data.decode())
        return None

    def get_all_blocks(self):
        """
        모든 블록 가져오기
        :return: 블록 데이터 리스트
        """
        blocks = []
        for key, value in self.db:
            if key.startswith(b"block_"):
                blocks.append(json.loads(value.decode()))
        return blocks
