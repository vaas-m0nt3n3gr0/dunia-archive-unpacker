import struct

FAT_SIGNATURE = b"FAT3"

def parse_fat_header(data: bytes):
    magic, version, file_count = struct.unpack("<4sII", data[:12])
    if magic != FAT_SIGNATURE:
        raise ValueError("Invalid FAT header")
    return {"version": version, "count": file_count}
