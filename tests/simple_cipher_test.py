import re

from src.simple_cipher import Cipher


class TestRandomKeyCipher:
    def test_can_encode(self) -> None:
        cipher = Cipher()
        plaintext = "aaaaaaaaaa"
        assert cipher.encode(plaintext) == cipher.key[0 : len(plaintext)]

    def test_can_decode(self) -> None:
        cipher = Cipher()
        assert cipher.decode(cipher.key[0 : len("aaaaaaaaaa")]) == "aaaaaaaaaa"

    def test_is_reversible(self) -> None:
        cipher = Cipher()
        plaintext = "abcdefghij"
        assert cipher.decode(cipher.encode(plaintext)) == plaintext

    def test_key_is_made_only_of_lowercase_letters(self) -> None:
        assert re.match("^[a-z]+$", Cipher().key)

    def test_one_encode(self) -> None:
        """REMOVE ME."""
        cipher = Cipher(key="b")
        plaintext = "a"
        encode = cipher.encode(plaintext)
        print(encode)
        assert cipher.decode(cipher.encode(plaintext)) == plaintext


class TestSubstitutionCipher:
    def test_can_encode(self) -> None:
        cipher = Cipher("abcdefghij")
        plaintext = "aaaaaaaaaa"
        assert cipher.encode(plaintext) == cipher.key

    def test_can_decode(self) -> None:
        cipher = Cipher("abcdefghij")
        assert cipher.decode(cipher.key) == "aaaaaaaaaa"

    def test_is_reversible(self) -> None:
        cipher = Cipher("abcdefghij")
        plaintext = "abcdefghij"
        assert cipher.decode(cipher.encode(plaintext)) == plaintext

    def test_can_double_shift_encode(self) -> None:
        cipher = Cipher("iamapandabear")
        plaintext = "iamapandabear"
        assert cipher.encode(plaintext) == "qayaeaagaciai"

    def test_can_wrap_on_encode(self) -> None:
        cipher = Cipher("abcdefghij")
        plaintext = "zzzzzzzzzz"
        assert cipher.encode(plaintext) == "zabcdefghi"

    def test_can_wrap_on_decode(self) -> None:
        cipher = Cipher("abcdefghij")
        assert cipher.decode("zabcdefghi") == "zzzzzzzzzz"

    def test_can_encode_messages_longer_than_the_key(self) -> None:
        cipher = Cipher("abc")
        plaintext = "iamapandabear"
        assert cipher.encode(plaintext) == "iboaqcnecbfcr"

    def test_can_decode_messages_longer_than_the_key(self) -> None:
        cipher = Cipher("abc")
        assert cipher.decode("iboaqcnecbfcr") == "iamapandabear"
