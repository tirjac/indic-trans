# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/utils/UrduNormalizer.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   UrduNormalizer.py : Normalizer for Urdu scripts. Normalizes different unicode canonical equivalances to a single unicode code-point.
# 
# This code is adapted from https://github.com/libindic/indic-trans/blob/master/indictrans/_utils/script_normalizer.py
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

from __future__ import unicode_literals
import os
import re
from indictrans.base.HandleConstants import INDICTRANS_URDU_MAP

class UrduNormalizer():
	"""Normalizer for Urdu scripts. Normalizes different unicode canonical
	equivalances to a single unicode code-point.

	Examples
	--------
	>>> from indictrans import UrduNormalizer
	>>> nu = UrduNormalizer()
	>>> print(nu.normalize(text))
	"""
	def __init__(self):
		self.norm_tbl = INDICTRANS_URDU_MAP

	def cnorm(self, text):
		"""Normalize NO_BREAK_SPACE, SOFT_HYPHEN, WORD_JOINER, H_SPACE,
		ZERO_WIDTH[SPACE, NON_JOINER, JOINER],
		MARK[LEFT_TO_RIGHT, RIGHT_TO_LEFT, BYTE_ORDER, BYTE_ORDER_2]
		"""
		text = text.replace('\u00A0', ' ')  # NO_BREAK_SPACE
		text = text.replace('\u00AD', '')  # SOFT_HYPHEN
		text = text.replace('\u2060', '')  # WORD_JOINER
		text = text.replace('\u200A', ' ')  # H_SP
		text = text.replace('\u200B', ' ')  # ZERO_WIDTH_SPACE
		text = text.replace('\u200C', '')  # ZERO_WIDTH_NON_JOINER
		text = text.replace('\u200D', '')  # ZERO_WIDTH_JOINER
		text = text.replace('\u200E', '')  # LEFT_TO_RIGHT_MARK
		text = text.replace('\u200F', '')  # RIGHT_TO_LEFT_MARK
		text = text.replace('\uFEFF', '')  # BYTE_ORDER_MARK
		text = text.replace('\uFFFE', '')  # BYTE_ORDER_MARK_2

		return text

	def normalize(self, text):
		"""normalize text"""
		text = self.cnorm(text)
		# canonical normalizations
		text = text.translate(self.norm_tbl)
		# matra normalizations
		text = re.sub('[\u064d\u0652\u0654-\u065b]', '', text)
		text = re.sub('([^\u06a9\u06af\u0686\u062c\u0679\u0688\u062a\u062f\u067e\u0628\u0691])\u06be', r'\1%s' % '\u06c1', text)
		# remove vowels
		text = re.sub('[\u0650\u064e\u064f]', '', text)
		# hamza and mada normalizations
		text = text.replace('\u0627\u0653', '\u0622')
		text = text.replace('\u0648\u0654', '\u0624')
		text = text.replace('\u06cc\u0654', '\u0626')
		text = text.replace('\u06d2\u0654', '\u06d3')
		text = text.replace('\u0626\u0626', '\u0626\u06cc')
		text = text.replace('\u06d5\u0654', '\u06c1\u0654')

		return text
