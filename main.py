import os
import sys
import threading
import argparse
# 현재 디렉토리 기준 하위 디렉토리 추가
sys.path.append(os.path.join(os.path.dirname(__file__), 'blockchain'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from cli import handle_cli
from blockchain import Blockchain
from p2p import Node

def start_peer_explore(blockchain, ip, port):
    """
    피어 탐색
    """
    print("Starting peer discovery")
    blockchain.peers.append((ip,port))
    print("Peer explore")

def main():

    parser = argparse.ArgumentParser(description="P2P Blockchain Node")
    parser.add_argument("ip", type=str, help="IP address to bind the server")
    parser.add_argument("port", type=int, help="Port to bind the server")
    args = parser.parse_args()

    ip = args.ip
    port = args.port

    p2p_node = Node(host=ip,port=port)
    p2p_node.start()

    print("Starting blockchain program...")

    blockchain  = Blockchain(path="./db/blockchain_db/")
    print("블록 로드 시작 ")

    blockchain.load_chain_from_db()
    print("블록 로드 완료 ")

    peer_thread = threading.Thread(target=start_peer_explore, args=(blockchain,ip, port))
    peer_thread.start()

    handle_cli(blockchain, p2p_node)
    print("Block chain program terminated")

if __name__ == "__main__":
    main()
