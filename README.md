# PubKunco
code to uncompress public keys for math purposes



This Python code is used to uncompress a compressed public key on the SECP256k1 elliptic curve. The compressed public key is converted to its uncompressed form. Here's a simple explanation of how it works:

The code defines three functions:

modular_sqrt: Computes the square root of an integer a modulo a prime p.
legendre_symbol: Computes the Legendre symbol (a/p) of an integer a modulo a prime p.
uncompress_public_key: Uncompresses a compressed public key to its uncompressed form.
The uncompress_public_key function takes a compressed public key as input and converts it to its uncompressed form.

It removes the compression flag ('03' or '02') from the compressed key and converts it to bytes.

It retrieves the x-coordinate from the compressed key and computes the corresponding y-coordinate using the SECP256k1 elliptic curve equation.

The x and y coordinates are then combined to form the uncompressed key in the format '04' + x-coordinate + y-coordinate.

The code then prints the resulting uncompressed key.
