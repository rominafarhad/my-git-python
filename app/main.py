import sys
import os

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
    else:
        raise RuntimeError(f"Unknown command: {command}")

if __name__ == "__main__":
    main()