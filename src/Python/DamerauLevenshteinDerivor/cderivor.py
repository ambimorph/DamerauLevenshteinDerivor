#!/usr/bin/python

import os, string, subprocess

class Derivor:
    def __init__(self, path_to_vocabulary_file):
        self.derivor = subprocess.Popen(['derivor', path_to_vocabulary_file], stdin=-1, stdout=-1)
        self.stdin = self.derivor.stdin
        self.stdout = self.derivor.stdout

    def variations(self, word, verbose=False):
    	self.derivor.stdin.write("d ")
    	self.derivor.stdin.write(word)
    	self.derivor.stdin.write("\n")
        result = []
	line = self.derivor.stdout.readline()
        while line != "\n":
            if verbose:
                result.append(line)
            else:
                result.append(line.split()[0])
            line = self.derivor.stdout.readline()
	return result


    def inV(self, word):
        self.derivor.stdin.write("v " + word + "\n")
        return self.derivor.stdout.readline().strip() == '1'

    def shutdown(self):
        if hasattr(self, "derivor"):
            if hasattr(self.derivor, "pid") and self.derivor.pid:
                os.kill(self.derivor.pid, 15)
            self.derivor.wait()

    def __del__(self):
        self.shutdown()
