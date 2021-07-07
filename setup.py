#!/usr/bin/env python

import sys

def main():
    file = open(ganach_dev.bash,'w+')
    flags = ['-h','-f']
    long_flags = ['--help', '--fork']
	bash_comand = 'npx ganache-cli{}{}'.format(' ', flags[0])
	bash_script = (
		"#!/bin/bash\n"
		"\n"
		"cmd='{}'\n".format(bash_comand)
		"echo $cmd\n"
		"$cmd"
	)
    file.write(bash_script)

if __name__ == "__main__":
    main()
