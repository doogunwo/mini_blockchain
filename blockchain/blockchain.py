import os,sys
# 프로젝트 루트 디렉토리를 경로에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 테스트 파일 경로
project_root = os.path.abspath(os.path.join(current_dir, '..'))  # 루트 디렉토리 경로
sys.path.append(os.path.join(project_root, 'blockchain'))  # blockchain 디렉토리 추가
sys.path.append(os.path.join(project_root, 'utils'))  # utils 디렉토리 추가
sys.path.append(os.path.join(project_root, "db"))

from leveldb import Leveldb
from block import Block
from transaction import Transaction
from proof_of_work import ProofOfWork
from consensus import Consensus
import json, socket
import  threading

class Blockchain:

    def __init__(self,mining_interval=2, path="./db/blockchain_db"):
        """
        블록체인 초기화
        """
        self.difficulty = 4
        self.chain = []
        self.pending_txs = []
        self.mining_interval = mining_interval
        self.peers = []
        self.db = Leveldb(path)

        last_block = self.db.get_last_block()
        if last_block:
            self.load_chain_from_db()
        else:
            genesis_block = self.create_genesis_block()
            self.db.save_block(genesis_block)
            self.chain.append(genesis_block)
    
    def load_chain_from_db(self):
        blocks = self.db.get_all_blocks()
        for block_data in blocks:

            block = Block(
                    index = block_data["index"],
                    txs = block_data["txs"],
                    pre_hash = block_data["pre_hash"],
                    difficulty = block_data["difficulty"],
            )

            block.timestamp = block_data["timestamp"]
            block.hash = block_data["hash"]
            self.chain.append(block)
            

    def create_genesis_block(self):
        """
        제네시스 블록 생성
        """
        pow = ProofOfWork(self.difficulty)
        nonce, block_hash = pow.mine("GenesisBlock", "0")

        genesis_block = Block(
                index = 0,
                txs = [],
                pre_hash = "0x0000000000000001",
                difficulty=self.difficulty
        )
        
        genesis_block.nonce = nonce
        genesis_block.hash = block_hash
        return genesis_block
        
    
    def get_latest_block(self):
        last_block_data =self.db.get_last_block()
        if last_block_data:
            return Block(**last_block_data)
        return None
    
    def add_txs(self, txs):
        self.pending_txs.append(txs)
    
    def mine_block(self):
        """
        블록 생성 및 추가
        """
        
        latest_block = self.get_latest_block()
        if latest_block is None:
            print("last block is None")
            return

        block_data =str(self.pending_txs)                        
        pow = ProofOfWork(self.difficulty)
    
        nonce, block_hash = pow.mine(block_data, latest_block.hash)
        for tx in self.pending_txs:
            tx_id = tx.get("tx_id")
            self.pending_txs.append(tx_id)

        new_block = Block(
            index= latest_block.index+1,
            txs = self.pending_txs,
            pre_hash=latest_block.hash,
            difficulty=self.difficulty,
        )
        new_block.nonce = nonce
        new_block.hash = block_hash
    
        self.db.save_block(new_block)

        self.pending_txs = []
        
        print(f"Block {new_block.index} has been mined")
        print(f"Nonce: {nonce}, hash : {block_hash}")
        
        # 네트워크에 블록 브로드캐스트
        self.broadcast_block(new_block)
        
    def broadcast_block(self, block):
        print(f"Broadcasting block {block.index} to the network.")

        block_data = json.dumps(block.__dict__)
        
        for peer in self.peers:
            peer_host, peer_port = peer
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                    client.connect((peer_host, peer_port))
                    client.sendall(block_data.encode())
                    print("f{block.index} sent to {peer_host}:{peer_port}")
            except Exception as e:
                print("f Error broadcasting to peer {e}")

    def add_block(self, block_data):
        
        new_block = Block(
            index=block_data["index"],
            tx = block_data["txs"],
            pre_hash = block_data["pre_hash"],
            difficulty = block_data["difiiculty"],
        )
        new_block.nonce = block_data["nonce"]
        new_block.hash = block_data["hash"]
        
        if new_block.pre_hash == self.get_latest_block().hash and \
            new_block.hash.startwith("0" * self.difficulty):
                self.chain.append(new_block)
                print(f"Block {new_block.index} added to the chain")
        else:
            print(f"Invalid block received : {new_block.index}")

            
        
