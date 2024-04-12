import secrets
import base64

# OTP uses base32 keys to generate the TOTP code. 
# Base32 converts 5 bytes to 8 characters.
# Most Websites use 32 character keys in base32. You can use 64 characters but there's no real benifit as 32 is already secure.
# Calculate required bytes to generate: 5/8 *32 = 20 [Bytes per 8 characters by desired number of characters]
random_bytes = secrets.token_bytes(20)
# Encode these bytes in Base32 then decode to string.
encoded_key = base64.b32encode(random_bytes).decode()
# Display Secret Key
print (encoded_key)
