import hashlib
import os
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class Wallet:
    def __init__(self, wallet_dir="wallet"):
        """
        지갑 초기화: 개인 키 및 공개 키 생성
        :param wallet_dir: 개인 키를 저장할 폴더 경로
        """
        self.wallet_dir = os.path.abspath(wallet_dir)  # 절대 경로로 변환
        os.makedirs(self.wallet_dir, exist_ok=True)  # 폴더 생성
        self.private_key_file = os.path.join(self.wallet_dir, "private_key.pem")
        
        if os.path.exists(self.private_key_file):
            # 기존 개인 키 로드
            self.private_key = self.load_private_key()
        else:
            # 새로운 개인 키 생성 및 저장
            self.private_key = SigningKey.generate(curve=SECP256k1)
            self.save_private_key()

        self.public_key = self.private_key.verifying_key  # 공개 키 생성

    def save_private_key(self):
        """
        개인 키를 파일에 저장
        """
        with open(self.private_key_file, "wb") as file:
            file.write(self.private_key.to_pem())
        print(f"Private key saved to {self.private_key_file}")

    def load_private_key(self):
        """
        기존 개인 키를 파일에서 로드
        :return: SigningKey 객체
        """
        with open(self.private_key_file, "rb") as file:
            return SigningKey.from_pem(file.read())

    def get_address(self):
        """
        공개 키로부터 지갑 주소 생성 (SHA-256 사용)
        :return: 지갑 주소 (16진수 문자열)
        """
        public_key_bytes = self.public_key.to_string()
        address = hashlib.sha256(public_key_bytes).hexdigest()
        return address

    def sign_transaction(self, message):
        """
        트랜잭션에 디지털 서명 추가
        :param message: 서명할 메시지 (트랜잭션 데이터)
        :return: 서명된 데이터 (16진수 문자열)
        """
        if isinstance(message, str):
            message = message.encode()
        signature = self.private_key.sign(message)
        return signature.hex()

    @staticmethod
    def verify_signature(public_key, message, signature):
        """
        디지털 서명 검증
        :param public_key: 송신자의 공개 키
        :param message: 서명된 메시지
        :param signature: 검증할 서명
        :return: 검증 결과 (True/False)
        """
        if isinstance(message, str):
            message = message.encode()
        if isinstance(signature, str):
            signature = bytes.fromhex(signature)

        verifying_key = VerifyingKey.from_string(public_key, curve=SECP256k1)
        try:
            return verifying_key.verify(signature, message)
        except Exception:
            return False
