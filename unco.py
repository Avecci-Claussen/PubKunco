import binascii
import ecdsa

def modular_sqrt(a, p):
    """Compute the square root of 'a' modulo prime 'p'."""
    if legendre_symbol(a, p) != 1:
        raise ValueError("Input value 'a' is not a square modulo 'p'")
    if a == 0:
        return 0
    if p == 2:
        return a
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t % p == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, pow(2, r - m - 1, p), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

def legendre_symbol(a, p):
    """Compute the Legendre symbol (a/p)."""
    ls = pow(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls

def uncompress_public_key(compressed_key):
    # Remove the compression flag
    compressed_key = compressed_key.strip()
    compressed_key = compressed_key[2:]  # Remove the leading '03' or '02'

    # Convert the compressed key to bytes
    compressed_bytes = binascii.unhexlify(compressed_key)

    # Get the x-coordinate from the compressed key
    x = int.from_bytes(compressed_bytes, byteorder='big')

    # Determine the y-coordinate based on the compression flag
    curve = ecdsa.curves.SECP256k1.curve
    p = curve.p()
    a = curve.a()
    b = curve.b()
    y_square = (pow(x, 3, p) + a * x + b) % p
    y = modular_sqrt(y_square, p)

    # Format the x and y coordinates as hex strings
    x_hex = hex(x)[2:].zfill(64)
    y_hex = hex(y)[2:].zfill(64)

    # Combine the x and y coordinates to form the uncompressed key
    uncompressed_key = '04' + x_hex + y_hex

    return uncompressed_key

# Example usage
compressed_key = '0205eaf779d2ba38eac770699b8f59ccbcf645ab6789ed481a53c1f8d2c489c04b'
uncompressed_key = uncompress_public_key(compressed_key)
print(uncompressed_key)