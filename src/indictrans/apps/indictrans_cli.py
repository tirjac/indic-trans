# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/apps/indictrans_cli.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   indictrans_cli.py : test program for indictrans
# 
# @section LICENSE
# 
# Copyright (c) 2025 Shreos Roychowdhury.
# Copyright (c) 2025 Tirja Consulting LLP.
# 
# This source code is released under GNU Affero General Public License.
# Please refer https://www.gnu.org/licenses/agpl-3.0.en.html#license-text
#
# THE SOFTWARE IS PROVIDED , WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 

import sys
import argparse
from pathlib import Path
import json
from datetime import datetime
import traceback

from indictrans.utils.HandleCommonUtils import WXEncoder, UrduNormalizer
from indictrans.utils.Transliterator import Transliterator

def create_app():

	languages = '''eng hin guj pan ben mal kan tam tel ori mar nep bod kok asm urd'''.split()
	lang_help = "select language (3 letter ISO-639 code) {%s}" % ( ', '.join(languages))

	parser = argparse.ArgumentParser( prog="indictrans-cli", description="Transliterator for Indian Languages")
	group = parser.add_mutually_exclusive_group()

	parser.add_argument('-v', '--version', action="version", version="%(prog)s 1.0")
	parser.add_argument( '-q', '--query', type=str, metavar='', help="<query>")
	parser.add_argument( '-s', '--source', dest="source", choices=languages, default="hin", metavar='', help="%s" % lang_help)
	parser.add_argument( '-t', '--target', dest="target", choices=languages, default="eng", metavar='', help="%s" % lang_help)
	parser.add_argument( '-b', '--build-lookup', dest="build_lookup", action='store_true', help='build lookup to fasten transliteration')
	group.add_argument( '-r', '--rb', metavar='', help='use rule-based system for transliteration', action=argparse.BooleanOptionalAction)
	parser.add_argument( '-x', '--xtest', metavar='', help="test all: " % languages, action=argparse.BooleanOptionalAction)

	args = parser.parse_args()
	start_dd = datetime.now()

	try:
		if args.xtest:
			query = { 'eng' : args.query if args.query else 'A quick brown fox jumps over the lazy dog' }
			no_lang = len(languages)
			for ii, xx in enumerate(languages):
				for yy in languages[ii+1:]:
					if xx == yy:
						continue
					for rb in (True,False):
						trn = Transliterator(xx, yy, rb=rb, build_lookup=True)
						if trn.check():
							tline = trn.convert(query[xx])
							print (f"Test {xx} -> {yy} rb={rb}: {tline}")
							if yy not in query:
								query[yy] = tline
						else:
							print (f"Test {xx} -> {yy} rb={rb}: NOT SUPPORTED")
						r_trn = Transliterator(yy,xx, rb=rb, build_lookup=True)
						if r_trn.check():
							tline = r_trn.convert(query[yy])
							print (f"Test {yy} -> {xx} rb={rb}: {tline}")
						else:
							print (f"Test {yy} -> {xx} rb={rb}: NOT SUPPORTED")

		else:
			if (not args.source) or (not args.target) or (not args.query):
				raise ValueError("query, source and target are needed")
			if args.source == args.target:
				raise ValueError("source and target should be different")
			# initialize transliterator object
			trn = Transliterator(args.source, args.target, rb=args.rb, build_lookup=args.build_lookup)
			# transliterate text
			tline = trn.convert(args.query)
			print ( tline)

		# done
		delta = datetime.now() - start_dd
		print(f"Time difference is {delta.total_seconds()} seconds")

	except OSError as err:
		print("OS error: {0}".format(err))
		print(traceback.format_exc())
	except ValueError as ve:
		print(ve)
		print(traceback.format_exc())
	except:
		print("Unexpected error:", sys.exc_info())
		print(traceback.format_exc())

if __name__ == '__main__':
	create_app()
