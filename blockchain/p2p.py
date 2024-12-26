import socket
import threading
import json

class Node:
    def __init__(self,host, port):
        """
        p2p 노드 클래스
        host : ip 주소
        port : 포트번호
        """

        self.host = host
        self.port = port
        self.peers = []
        self.server_thread = threading.Thread(target=self.start_server)  # 서버 스레드

    def start_server(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        print(f"Node listening on {self.host}:{self.port}...")

        while True:
            conn, addr = server.accept()
            print(f"Connected by {addr}")
            threading.Thread(target=self.handle_client, args=(conn,)).start()
    
    def handle_client(self, conn):
        try:
            data = conn.recv(1024).decode()
            if data:
                msg = json.loads(data)
                if "index" in msg:
                    print("rciv")
                    #self.blockchain.add_block(msg)
                else:
                    print(f"Recv unkown msg : {msg}")
                conn.close()
        except Exception as e:
            print(f"{e}")
    
    def process_message(self, message):
        print(f"Processing message: {message}")

    def connect_to_peer(self, peer_host, peer_port):
        """
        다른 피어에 연결
        :param peer_host: 피어의 호스트 주소
        :param peer_port: 피어의 포트 번호
        """
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((peer_host, peer_port))
            self.peers.append((peer_host, peer_port))
            print(f"Connected to peer {peer_host}:{peer_port}")

            # 기본 메시지 전송
            message = json.dumps({"message": "Hello, Peer!"})
            client.sendall(message.encode())
            client.close()
        except Exception as e:
            print(f"Error connecting to peer: {e}")
    
    def start(self):
        """
        서버 스레드 시작
        """
        self.server_thread.start()
    
    def broadcast_block(self, block):
        """
        네트워크에 새 블록 브로드캐스트
        :param block: 새로 채굴된 블록
        """
        block_data = json.dumps(block.__dict__)
        for peer in self.peers:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect(peer)
                client.sendall(block_data.encode())
                client.close()
            except Exception as e:
                print(f"Error broadcasting to peer {peer}: {e}")

    def process_block(self, block_data):
        """
        수신된 블록 데이터 블록체인에 추가
        수신된 블록 데이터 JSON 형식
        """
        if self.blockchain:
            self.blockchain.add_block(block_data)
        else:
            print("No blockchain attached to this node")

   
