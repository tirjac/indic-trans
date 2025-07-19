# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/utils/Transliterator.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   Transliterator.py : transliterator base class
# 
# This code is adapted from https://github.com/libindic/indic-trans/blob/master/indictrans/transliterator.py
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

from indictrans.utils.HandleDecoders import DECODERS
from indictrans.utils.ScriptTransliterator import (Ind2Target, Rom2Target, Urd2Target, Ind2IndRB)

NORB_NOT_FOUND = [
	('hin' , 'mar'), ('mar' , 'hin'),
	('hin' , 'nep'), ('nep' , 'hin'),
	('hin' , 'bod'), ('bod' , 'hin'),
	('hin' , 'kok'), ('kok' , 'hin'),
	('ben' , 'asm'), ('asm' , 'ben'),
	('mar' , 'nep'), ('nep' , 'mar'),
	('mar' , 'bod'), ('bod' , 'mar'),
	('mar' , 'kok'), ('kok' , 'mar'),
	('nep' , 'bod'), ('bod' , 'nep'),
	('nep' , 'kok'), ('kok' , 'nep'),
	('bod' , 'kok'), ('kok' , 'bod'),
]

def _get_decoder(decode):
	try:
		return DECODERS[decode]
	except KeyError:
		raise ValueError('Unknown decoder {0!r}'.format(decode))

def _get_trans(trans, decode):
	if decode == 'viterbi':
		return trans.transliterate
	else:
		return trans.top_n_trans

class Transliterator():
	"""Transliterator for Indic scripts including English and Urdu."""

	def __init__(self, source='hin', target='eng', decode='viterbi', build_lookup=False, rb=True):
		source = source.lower()
		target = target.lower()
		if source == target or (source,target) in NORB_NOT_FOUND:
			self.donthandle = True
			return None
		self.donthandle = False
		impl = "hin guj pan ben mal kan tam tel ori mar nep kok bod asm eng urd".split()
		decoder = (decode, _get_decoder(decode))
		if source in ['eng', 'urd']:
			if target not in impl or source == target:
				raise NotImplementedError( 'Language pair `%s-%s` is not implemented.' % (source, target))
			if source == 'eng':
				ru2i = Rom2Target(source, target, decoder, build_lookup)
			else:
				ru2i = Urd2Target(source, target, decoder, build_lookup)
			self.transform = _get_trans(ru2i, decode)
		elif target in ['eng', 'urd']:
			if source not in impl or source == target:
				raise NotImplementedError( 'Language pair `%s-%s` is not implemented.' % (source, target))
			i2o = Ind2Target(source, target, decoder, build_lookup)
			self.transform = _get_trans(i2o, decode)
		else:
			if source not in impl or target not in impl or source == target:
				raise NotImplementedError( 'Language pair `%s-%s` is not implemented.' % (source, target))
			if rb:
				self.transform = Ind2IndRB(source, target).rtrans
			else:
				i2i = Ind2Target(source, target, decoder, build_lookup)
				self.transform = _get_trans(i2i, decode)

	def check(self):
		return False if self.donthandle else True

	def convert(self, line):
		return self.transform(line) if (not self.donthandle) else ''
