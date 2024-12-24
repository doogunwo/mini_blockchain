import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount):
        """
        sender : 송신자 -> 공개 키 주소
        receiver : 수신자 주소 -> 공개 키 주소
        amount : 송금 금액
        """

        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.tx_id = self.calculate_tx_id()

    def calculate_tx_id(self):
        """
        tx 주소 생성 -> tx_id
        """
        tx_string = f"{self.sender}{self.receiver}{self.amount}"
        return hashlib.sha256(tx_string.encode()).hexdigest()

    def __repr__(self):
        """
        트랜잭션 정보 반환
        """
        return (
            f"Transaction(sender={self.sender}, receiver={self.receiver}, "
            f"amount={self.amount}, tx_address={self.tx_id})"
        )
    