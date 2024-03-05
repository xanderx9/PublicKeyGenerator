import ecdsa
import hashlib


curve = ecdsa.SECP256k1


start_private_key = int(input("Enter start private key: "), 16)
end_private_key = int(input("Enter end private key: "), 16)

output_file = "public_keys.txt"

with open(output_file, "w") as file:
    for private_key_value in range(start_private_key, end_private_key + 1):
        private_key_hex = hex(private_key_value)[2:].zfill(64)  # Convert to hexadecimal and zero-fill to 64 characters
        private_key_bytes = bytes.fromhex(private_key_hex)
        
        # Create a private key object
        private_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=curve)
        
        # Get the corresponding public key object
        public_key = private_key.verifying_key
        
        # Convert the public key to hexadecimal format
        public_key_hex = public_key.to_string("compressed").hex()
        
        
        file.write(public_key_hex + "\n")

print(f"Public keys written to {output_file}")
