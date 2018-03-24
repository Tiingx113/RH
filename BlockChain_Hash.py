#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	import hashlib
	#要使用hash運算的文字
	hashTarget = 'hello python 255!'
	#hash 運算
	encryptionBySHA256 = hashlib.sha256(hashTarget).hexdigest()
	print 'hashTarget: %s\n encryptionBySHA256: %s'%(hashTarget, encryptionBySHA256)
	pass

if __name__ == '__main__':
	main()