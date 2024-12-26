from p2p import Node

def handle_cli(blockchain, p2p_node):
    """
    CLI 명령 처리
    """
    print("Blockchain CLI started. Type 'help' for available commands.")
    while True:
        command = input("> ").strip()
        if command == "exit":
            print("Exiting program...")
            break
        elif command == "help":
            print("""
Available commands:
    show_chain        - Show all blocks in the blockchain
    mine              - Mine a new block
    add_tx <data>     - Add a transaction to the blockchain
    add_peer <host> <port> - Add a new peer to the network
    show_peers        - Show the list of connected peers
    exit              - Exit the program
            """)


        elif command == "show_chain":
            print("Blockchain:")
            for block in blockchain.chain:
                print(block.info_block())


        elif command == "mine":
            blockchain.mine_block()


        elif command.startswith("add_tx "):
            data = command[len("add_tx "):]
            blockchain.add_txs(data)
            print(f"Transaction added: {data}")


        elif command.startswith("add_peer "):
            parts = command.split()
            if len(parts) == 3:
                host, port = parts[1], int(parts[2])
                blockchain.peers.append((host, port))
                p2p_node.connect_to_peer(host, port) 
                print(f"Peer added: {host}:{port}")
            else:
                print("Usage: add_peer <host> <port>")



        elif command == "show_peers":
            print("Connected peers:")
            for peer in blockchain.peers:
                print(f"{peer[0]}:{peer[1]}")

        else:
            print(f"Unknown command: {command}. Type 'help' for available commands.")

