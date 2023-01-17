import subprocess
import sys
from termcolor import colored

key_terms = {"green": ["success", "OK", "200"], "yellow": ["unknown", "207"], "red": ["400", "404", "409"]}

def pretty_print_logs():
    # Run the docker logs --follow command with the container passed as a cli argument
    # python3 pretty_print_logs.py [container_name]
    proc = subprocess.Popen(['docker', 'logs', '--follow', sys.argv[1]], stdout=subprocess.PIPE)

    # Iterate over the logs output and format in a structure similar to JSON
    for line in iter(proc.stdout.readline, ''):
        tab_count = 0
        print("\n\n===========================================\n")
        new_line = []
        for char in line.decode('utf-8'):
            if char == '{':
                tab_count += 1
#                print(f"{char}\n", "".join(["  "] * tab_count), end="")
                new_line.append("{}\n{}".format(char, "".join(["  "] * tab_count)))
            elif char == '}':
                tab_count -= 1
#                print("\n", "".join(["  "] * tab_count), "}", end="")
                new_line.append("\n{}}}".format("".join(["  "] * tab_count)))
            elif char == ',':
#                print(f"{char}\n", "".join(["  "] * tab_count), end="")
                new_line.append("{}\n{}".format(char, "".join(["  "] * tab_count)))
            else:
#                print(char, end="")
                new_line.append(char)
                
        line_string = "".join(new_line)
        for term in key_terms:
            index = line_string.find(term)
            if index != -1:
                line_string = string
        print("".join(new_line))

if __name__ == '__main__':
    pretty_print_logs()
