import json
from blockchain.block import Block

class BlockchainSync:
    @staticmethod
    def serialize_chain(blockchain):
        """
        블록체인을 JSON 형식으로 직렬화
        :param blockchain: Blockchain 객체
        :return: 직렬화된 JSON 문자열
        """
        return json.dumps([block.__dict__ for block in blockchain.chain])

    @staticmethod
    def deserialize_chain(serialized_chain):
        """
        JSON 형식의 블록체인을 Blockchain 객체로 역직렬화
        :param serialized_chain: 직렬화된 JSON 문자열
        :return: Blockchain 객체
        """
        blockchain = Blockchain()
        blockchain.chain = []
        chain_data = json.loads(serialized_chain)

        for block_data in chain_data:
            block = Block(
                index=block_data["index"],
                transactions=block_data["transactions"],
                pre_hash=block_data["pre_hash"],
                difficulty=block_data["difficulty"],
            )
            block.hash = block_data["hash"]
            blockchain.chain.append(block)

        return blockchain

    @staticmethod
    def synchronize(local_chain, remote_chain):
        """
        원격 블록체인과 동기화
        :param local_chain: 로컬 블록체인
        :param remote_chain: 원격 블록체인
        :return: 동기화된 Blockchain 객체
        """
        if len(remote_chain.chain) > len(local_chain.chain):
            if remote_chain.is_chain_valid():
                print("Updating local chain with remote chain.")
                return remote_chain

        print("Local chain is up-to-date.")
        return local_chain
