import subprocess
import sys
from termcolor import colored
# temp comment
key_terms = {"green": ["success", "OK", "200"], "yellow": ["unknown", "207"], "red": ["400", "404", "409"]}

def pretty_print_logs():
    # Run the docker logs --follow command with the container passed as a cli argument
    # python3 pretty_print_logs.py [container_name]
    proc = subprocess.Popen(['docker', 'logs', '--follow', sys.argv[1]], stdout=subprocess.PIPE)

    # Iterate over the logs output and format in a structure similar to JSON
    for line in iter(proc.stdout.readline, ''):
        tab_count = 0
        print("\n\n===========================================\n")
        chars = []
        for char in line.decode('utf-8'):
            if char == '{':
                tab_count += 1
                chars.append("{}\n{}".format(char, "".join(["  "] * tab_count)))
            elif char == '}':
                tab_count -= 1
                chars.append("\n{}}}".format("".join(["  "] * tab_count)))
            elif char == ',':
                chars.append("{}\n{}".format(char, "".join(["  "] * tab_count)))
            else:
                chars.append(char)
            
        # Search for key terms and highlight them accordingly
        line = "".join(chars)
        for color, terms in key_terms.items():
            for term in terms:
                index = line.find(term)
                if index != -1:
                    line = line[:index] + colored(term, color) + line[index + len(term):]
        
        print(line, end="")

if __name__ == '__main__':
    pretty_print_logs()
