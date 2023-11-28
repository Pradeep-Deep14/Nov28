import sys,getopt
sys.argv=['c:\\a.py','-h','word1','word2']
options,arguments=getopt.getopt(sys.argv[1:],'s:t:h')
print(options)