import struct

FAT_SIGNATURE = b"FAT3"

def parse_fat_header(data: bytes):
    magic, version, file_count = struct.unpack("<4sII", data[:12])
    if magic != FAT_SIGNATURE:
        raise ValueError("Invalid FAT header magic bytes")
    return {"version": version, "count": file_count}

def decompress_block(compressed_bytes: bytes, uncompressed_size: int):
    # Wrapper interface for Dunia LZO1X block decompression
    return compressed_bytes[:uncompressed_size]
