import subprocess
import sys

def pretty_print_logs():
    # Run the docker logs --follow command with the container passed as a cli argument
    # python3 pretty_print_logs.py [container_name]
    proc = subprocess.Popen(['docker', 'logs', '--follow', sys.argv[1]], stdout=subprocess.PIPE)

    # Iterate over the logs output, format as JSON, and print to stdout
    for line in iter(proc.stdout.readline, ''):
        tab_count = 0
        print("\n\n===========================================\n")
        for char in line.decode('utf-8'):
            if char == '{':
                tab_count += 1
                print(f"{char}\n", "".join(["  "] * tab_count), end="")
            elif char == '}':
                tab_count -= 1
                print("\n", "".join(["  "] * tab_count), "}", end="")
            elif char == ',':
                print(f"{char}\n", "".join(["  "] * tab_count), end="")
            else:
                print(char, end="")

if __name__ == '__main__':
    pretty_print_logs()
