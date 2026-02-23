import sys
import os
import zlib

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "init":
        os.makedirs(".git", exist_ok=True)
        os.makedirs(".git/objects", exist_ok=True)
        os.makedirs(".git/refs", exist_ok=True)
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/master\n")
        print("Initialized empty Git repository in .git/")

    elif command == "cat-file":
        if len(sys.argv) < 4 or sys.argv[2] != "-p":
            sys.exit(1)
            
        object_hash = sys.argv[3]
        # Git stores objects in .git/objects/first_2_chars/remaining_chars
        path = f".git/objects/{object_hash[:2]}/{object_hash[2:]}"
        
        with open(path, "rb") as f:
            raw_data = zlib.decompress(f.read())
            # Format is: "blob <size>\x00<content>"
            header, content = raw_data.split(b"\x00", 1)
            sys.stdout.buffer.write(content)

    else:
        raise RuntimeError(f"Unknown command: {command}")

if __name__ == "__main__":
    main()