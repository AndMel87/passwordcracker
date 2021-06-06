# password hash cracker 2021
# Can decrypt MD5, SHA1, SHA256, SHA512 hashes and find matches in target file of passwords


# --- Libraries ---
import hashlib

#User input
typeHash = str(input("which type of Hash do you want to brute force? "))
filePath = str(input("Enter path to the file to brute force with: "))
hashDecrypt = str(input("Enter hash value to brute force: "))

#open filepath
with open(filePath, "r") as file:
    for line in file.readlines():
        if typeHash == "md5":
            hashObject = hashlib.md5(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == hashDecrypt:
                print("Found MD5 password: " + line.strip())
                exit(0)

        if typeHash == "sha1":
            hashObject = hashlib.sha1(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == hashDecrypt:
                print("Found SHA1 password: " + line.strip())
                exit(0)

        if typeHash == "sha256":
            hashObject = hashlib.sha256(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == hashDecrypt:
                print("Found SHA256 password: " + line.strip())
                exit(0)

        if typeHash == "sha512":
            hashObject = hashlib.sha512(line.strip().encode())
            hashedWord = hashObject.hexdigest()
            if hashedWord == hashDecrypt:
                print("Found SHA512 password: " + line.strip())
                exit(0)

    print("Password not in file.")
