# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file tests/test_trans.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   test_trans.py : tests 
# 
# This code is adapted from https://github.com/libindic/indic-trans/blob/master/indictrans/_utils/one_hot_encoder.py
# 
# @section LICENSE
# 
# Copyright (c) 2025 Shreos Roychowdhury.
# Copyright (c) 2025 Tirja Consulting LLP.
# Copyright (c) 2015 Irshad Ahmad Bhat.
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

from __future__ import division, unicode_literals

import io
import os

from testtools import TestCase
from indictrans.utils.Transliterator import Transliterator

class TestTransliterator(TestCase):
	def setUp(self):
		super(TestTransliterator, self).setUp()
		# test transliterations with English
		source = 'hin ben mal guj pan kan tam tel ori'.split()
		target_rom = ['eng'] * len(source)
		self.src2trg = list(zip(source, target_rom))
		self.trg2src = list(zip(target_rom, source))
		# test transliterations with Urdu
		source = 'hin pan eng'.split()
		target_urd = ['urd'] * len(source)
		self.src2trg += list(zip(source, target_urd))
		self.trg2src += list(zip(target_urd, source))
		self.test_dir = os.path.dirname(os.path.abspath(__file__))

	def test_bad_input_lang(self):
		self.assertRaises(NotImplementedError, Transliterator, source='eng', target='unknown')
		self.assertRaises(NotImplementedError, Transliterator, source='unknown', target='eng')
		self.assertRaises(NotImplementedError, Transliterator, source='unknown', target='unknown')

	def test_bad_decoder(self):
		self.assertRaises(ValueError, Transliterator, decode='unknown')

	def test_ind2ru(self):
		"""Test Indic-to-[Roman, Urdu] ML models"""
		for lang_pair in self.src2trg:
			src = lang_pair[0]
			trg = lang_pair[1]
			trans = Transliterator(source=src, target=trg)
			with io.open('%s/%s_%s.testpairs' % (self.test_dir, src, trg), encoding='utf-8') as fp:
				for line in fp:
					word, expected = line.split()
					self.assertEqual(trans.transform(word), expected)

	def test_ru2ind(self):
		"""Test [Roman, Urdu]-to-Indic ML models"""
		for lang_pair in self.trg2src:
			src = lang_pair[0]
			trg = lang_pair[1]
			trans = Transliterator(source=src, target=trg)
			with io.open('%s/%s_%s.testpairs' % (self.test_dir, trg, src), encoding='utf-8') as fp:
				for line in fp:
					expected, word = line.split()
					self.assertEqual(trans.transform(word), expected)

	def test_kbest(self):
		"""Make sure `k-best` works without failure"""
		k_best = range(2, 15)
		r2i = Transliterator(source='eng', target='hin', decode='beamsearch')
		i2r = Transliterator(source='hin', target='eng', decode='beamsearch')
		for k in k_best:
			hin = r2i.transform('indictrans', k_best=k)
			eng = i2r.transform(hin[0], k_best=k)
			self.assertTrue(len(hin) == k)
			self.assertTrue(len(eng) == k)

	def test_rtrans(self):
		"""Test Indic-to-Indic ML and Rule-Based models."""
		with io.open('%s/indic-test' % self.test_dir, encoding='utf-8') as fp:
			# first line contains language codes
			lang_codes = fp.readline().split()
			lang2word = dict(zip(lang_codes, [[] for i in range(len(lang_codes))]))
			for line in fp:
				line = line.split()
				for i, word in enumerate(line):
					lang2word[lang_codes[i]].append(word)
		for src in lang_codes:
			for trg in lang_codes:
				if src == trg:
					continue
				s2t_ml = Transliterator(source=src, target=trg, rb=False)
				s2t_rb = Transliterator(source=src, target=trg, rb=True)
				for word in lang2word[src]:
					s2t_ml.transform(word)
					s2t_rb.transform(word)

	def test_parser(self):
		# test parser arguments
		parser = self.parse_args(['--input', 'infile',
							 '--output', 'outfile',
							 '--source', 'hin',
							 '--target', 'eng',
							 '--build-lookup',
							 '--rb'])
		self.assertEqual(parser.infile, 'infile')
		self.assertEqual(parser.outfile, 'outfile')
		self.assertEqual(parser.source, 'hin')
		self.assertEqual(parser.target, 'eng')
		self.assertTrue(parser.build_lookup)
		self.assertTrue(parser.rb)
		# test parser args processing
		self.process_args(self.parse_args(['-i', '%s/indic-test' % self.test_dir,
								 '-o', '/tmp/test.out',
								 '-s', 'hin',
								 '-t', 'mal',
								 '-b', '-r']))

	def parse_args(self, args):
		languages = '''hin guj pan ben mal kan tam tel ori eng mar nep bod kok asm urd'''.split()
		# help messages
		lang_help = "select language (3 letter ISO-639 code) {%s}" % ( ', '.join(languages))
		# parse command line arguments
		parser = argparse.ArgumentParser( prog="indictrans", description="Transliterator for Indian Languages including English")
		group = parser.add_mutually_exclusive_group()
		parser.add_argument('-v', '--version', action="version", version="%(prog)s 1.0")
		parser.add_argument( '-s', '--source', dest="source", choices=languages, default="hin", metavar='', help="%s" % lang_help)
		parser.add_argument( '-t', '--target', dest="target", choices=languages, default="eng", metavar='', help="%s" % lang_help)
		parser.add_argument( '-b', '--build-lookup', dest="build_lookup", action='store_true', help='build lookup to fasten transliteration')
		group.add_argument( '-m', '--ml', action='store_true', help='use ML system for transliteration')
		group.add_argument( '-r', '--rb', action='store_true', help='use rule-based system for transliteration')
		parser.add_argument( '-i', '--input', dest="infile", type=str, metavar='', help="<input-file>")
		parser.add_argument( '-o', '--output', dest="outfile", type=str, metavar='', help="<output-file>")
		args = parser.parse_args(args)
		if args.source == args.target:
			sys.stderr.write('indictrans: error: source must be different from target\n')
			sys.stderr.write(parser.parse_args(['-h']))
		return args


	def process_args(self, args):
		if not (args.ml or args.rb):
			args.rb = True
		if args.infile:
			ifp = io.open(args.infile, encoding='utf-8')
		else:
			if sys.version_info[0] >= 3:
				ifp = codecs.getreader('utf8')(sys.stdin.buffer)
			else:
				ifp = codecs.getreader('utf8')(sys.stdin)

		if args.outfile:
			ofp = io.open(args.outfile, mode='w', encoding='utf-8')
		else:
			if sys.version_info[0] >= 3:
				ofp = codecs.getwriter('utf8')(sys.stdout.buffer)
			else:
				ofp = codecs.getwriter('utf8')(sys.stdout)

		# initialize transliterator object
		trn = Transliterator(args.source, args.target, rb=args.rb, build_lookup=args.build_lookup)

		# transliterate text
		for line in ifp:
			tline = trn.convert(line)
			ofp.write(tline)

		# close files
		ifp.close()
		ofp.close()
