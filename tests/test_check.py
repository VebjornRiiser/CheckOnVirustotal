import sys
from pathlib import Path
from io import BytesIO
src_dir = str(Path(__file__).parent.parent / 'src')
sys.path.append(src_dir)
from src import main

EmptyFileHash = "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"
filepath = "tests/file with spaces.txt"


def test_correct_hash():
    #Empty file with spaces in name
    assert main.create_file_hash(filepath) == EmptyFileHash


def test_wrong_hash():
    assert main.create_file_hash(filepath) != "AAAAAAD74E"


def test_create_hash():
    # Test case 1: Empty input
    reader = BytesIO(b"")
    assert main.create_hash(reader) == EmptyFileHash

    # Test case 2: Non-empty input
    # reader = BytesIO(b"Hello, world!")
    # assert check.create_hash(reader) == "2BB632B2DD0C15B22E1609C366065FD770CFB01890CBB6AAAD8D6DF719A2EDED"

    # # Test case 3: Large input
    # # reader = BytesIO(b"A" * 10**6)
    # # assert check.create_hash(reader) == "DDEB2C7F1A1C68D0F3A0A1FDDC1D7D5A8C4F4D9E"

    # # Test case 4: Input with special characters
    # reader = BytesIO(b"!@#$%^&*()")
    # assert check.create_hash(reader) == "8D4CF633E5A68A90CD91CA06E815E134508EC6D3E930551458F3718926B367A5"

    # # Test case 5: Input with newline characters
    # reader = BytesIO(b"Line 1\nLine 2\nLine 3")
    # assert check.create_hash(reader) == "619B1057E97904FF8899F44AABA712270FDAC8F02C7B7C27C3D114CF1D891ED4"

    # Add more test cases as needed