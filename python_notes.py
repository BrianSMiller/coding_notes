# FOLDER HANDLING
# get all filenames in curdir with <str>
import os
path = os.curdir
files = os.listdir(path)
sfFiles = [i for i in files if i.endswith('.sf')]


# FILE HANDLING
# open and load into RAM
with open("file_name.txt", 'r') as input_handle:
    file_lines_list = input_handle.readlines()

# write to file
filename = 'test_file_output.txt'
file_lines=["list","of","lines"]
with open(filename, 'w+') as file:
    file.writelines(i for i in file_lines)

# open a file one line at a time
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
	print(line)

# open a file and keep it open while writing to it
file=open('test1.txt', 'w+')
for i in range(1000):
    file.write('\n')
file.close()


## ARGUMENT HANDLING ##
import argparse
parser=argparse.ArgumentParser(description="program that replaces fasta headers")
parser.add_argument("-i", help="input fasta", type=file)
parser.add_argument("-o", help="output fasta")
args = parser.parse_args()
print("output file: {}".format(args.o))
## USAGE ##
# ./rename_fa_headers.py -i input.fa -l lookup_table.txt -o output.fa


# OTHER RANDOM THINGS
def bash_cmd(command):
	"""
	Calls a bash command and returns the standard output.
	"""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=os.curdir)
    proc_stdout = process.communicate()[0].strip()
    print("BASH_cmd_stdout: {}".format(proc_stdout))


if __name__ == '__main__':
    execute_order_66()

a="world"
print("hello {}".format(a))
