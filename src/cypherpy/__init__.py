import os.path
import sys

sys.path.append("/Users/adrian.trejo/Worspace/cypherPy")

from src.cypherpy.rsa import encryptRSA
    
def main():
    """Entry point for the application script"""
    fileToEncrypt = input("Enter the file to encrypt: ")
    if not (os.path.exists(fileToEncrypt)):
        print("File does not exist")
        return
    algorithmToEncrypt = input("Enter the algorithm to use: 1. RSA 2. AES: ")
    if not (algorithmToEncrypt == "1" or algorithmToEncrypt == "2"):
        print("Invalid algorithm")
        return
    if algorithmToEncrypt == "1":
        encryptRSA(fileToEncrypt)

if __name__ == "__main__": main()