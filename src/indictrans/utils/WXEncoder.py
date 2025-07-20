# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/utils/WXEncoder.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   WXEncoder.py :  WX Encoder
# 
# This code is adapted from https://github.com/libindic/indic-trans/blob/master/indictrans/_utils/wx.py
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
import re
from six import unichr

class WXEncoder():
	"""WX-converter for UTF to WX conversion of Indic scripts and vice-versa. """

	def __init__(self, order='utf2wx', lang='hin'):
		self.order = order
		self.lang_tag = lang.lower()
		self.fit()

	def fit(self):
		self.punctuation = r'!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~'
		# Handle iscii characters
		self.iscii_num = dict(
			zip(
				[unichr(i) for i in range(161, 252)],
				['\x03%s\x04' % (unichr(i)) for i in range(300, 391)]))
		self.num_iscii = dict(
			zip(
				['\x03%s\x04' % (unichr(i)) for i in range(300, 391)],
				[unichr(i) for i in range(161, 252)]))
		self.mask_isc = re.compile('([\xA1-\xFB])')
		self.unmask_isc = re.compile('(%s)' % '|'.join(
			['\x03%s\x04' % (unichr(i)) for i in range(300, 391)]))
		if self.order == "utf2wx":
			self.initialize_utf2wx_hash()
		elif self.order == "wx2utf":
			self.initialize_wx2utf_hash()
		else:
			raise ValueError('invalid source/target encoding\n')

	def initialize_wx2utf_hash(self):
		# CONSONANTS, VOWELS , MATRAS, MODIFIERS
		from indictrans.base.HandleWXConstants import \
			INDICTRANS_HASHC_W2I, INDICTRANS_HASHV_W2I, INDICTRANS_HASHM_W2I, INDICTRANS_HASHMD_W2I, INDICTRANS_DIGITS_W2I, \
			INDICTRANS_HASHH_I2U, INDICTRANS_HASHT_I2U, INDICTRANS_HASHP_I2U, \
			INDICTRANS_HASHK_I2U, INDICTRANS_HASHM_I2U, INDICTRANS_HASHB_I2U, \
			INDICTRANS_HASHCTA_I2U, INDICTRANS_HASHO_I2U, INDICTRANS_HASHG_I2U

		self.hashc_w2i = INDICTRANS_HASHC_W2I 
		self.hashv_w2i = INDICTRANS_HASHV_W2I 
		self.hashm_w2i = INDICTRANS_HASHM_W2I 
		self.hashmd_w2i = INDICTRANS_HASHMD_W2I 
		self.digits_w2i = INDICTRANS_DIGITS_W2I 
		self.hashh_i2u = INDICTRANS_HASHH_I2U 
		self.hasht_i2u = INDICTRANS_HASHT_I2U 
		self.hashp_i2u = INDICTRANS_HASHP_I2U 
		self.hashk_i2u = INDICTRANS_HASHK_I2U 
		self.hashm_i2u = INDICTRANS_HASHM_I2U 
		self.hashb_i2u = INDICTRANS_HASHB_I2U 
		self.hashcta_i2u = INDICTRANS_HASHCTA_I2U 
		self.hasho_i2u = INDICTRANS_HASHO_I2U 
		self.hashg_i2u = INDICTRANS_HASHG_I2U 

		# compile regexes
		const = 'kKgGfcCjJFtTdDNwWxXnpPbBmyrlvSsRh'
		self.ceVmd = re.compile("([%s])eV([MHz])" % const)
		self.ceV = re.compile("([%s])eV" % const)
		self.cZeV = re.compile("([%s])ZeV" % const)
		self.cZeVmd = re.compile("([%s])ZeV([MHz])" % const)
		self.cEYmd = re.compile("([%s])EY([MHz])" % const)
		self.cEY = re.compile("([%s])EY" % const)
		self.cOYmd = re.compile("([%s])OY([MHz])" % const)
		self.coVmd = re.compile("([%s])oV([MHz])" % const)
		self.coV = re.compile("([%s])oV" % const)
		self.cZoV = re.compile("([%s])ZoV" % const)
		self.cZoVmd = re.compile("([%s])ZoV([MHz])" % const)
		self.cOY = re.compile("([%s])OY" % const)
		self.cZOY = re.compile("([%s])ZOY" % const)
		self.cvmd = re.compile("([%s])([AiIuUeEoO])([MHz])" % const)
		self.cZvmd = re.compile("([%s])Z([AiIuUeEoO])([MHz])" % const)
		self.cv = re.compile("([%s])([AiIuUeEoO])" % const)
		self.cZv = re.compile("([%s])Z([AiIuUeEoO])" % const)
		self.camd = re.compile("([%s])a([MHz])" % const)
		self.cZamd = re.compile("([%s])Za([MHz])" % const)
		self.cZmd = re.compile("([%s])Z([MHz])" % const)
		self.ca = re.compile("([%s])a" % const)
		self.cZa = re.compile("([%s])Za" % const)
		self.cYZa = re.compile("([%s])YZa" % const)
		self.c = re.compile("([%s])" % const)
		self.cZ = re.compile("([%s])Z" % const)
		self.aqmd = re.compile("aq([MHz])")
		self.cq = re.compile("([%s])q" % const)
		self.cqmd = re.compile("([%s])q([MHz])" % const)
		self.qmd = re.compile("q([MHz])")
		self.dig = re.compile("([0-9])")
		self.i2u = re.compile('([\xA1-\xFB])')

	def initialize_utf2wx_hash(self):

		# second set
		from indictrans.base.HandleWXConstants import \
			INDICTRANS_HASHC_I2W, INDICTRANS_HASHV_I2W, INDICTRANS_HASHM_I2W, INDICTRANS_HASHMD_I2W, INDICTRANS_DIGITS_I2W, \
			INDICTRANS_HASHH_U2I, INDICTRANS_UNICODE_NORM_HASHH_U2I, INDICTRANS_HASHT_U2I, \
			INDICTRANS_HASHP_U2I, INDICTRANS_UNICODE_NORM_HASHP_U2I, INDICTRANS_HASHK_U2I, \
			INDICTRANS_HASHM_U2I, INDICTRANS_HASHB_U2I, INDICTRANS_UNICODE_NORM_HASHB_U2I, INDICTRANS_HASHTA_U2I, \
			INDICTRANS_HASHO_U2I, INDICTRANS_UNICODE_NORM_HASHO_U2I, INDICTRANS_HASHG_U2I

		self.hashc_i2w = INDICTRANS_HASHC_I2W
		self.hashv_i2w = INDICTRANS_HASHV_I2W
		self.hashm_i2w = INDICTRANS_HASHM_I2W
		self.hashmd_i2w = INDICTRANS_HASHMD_I2W
		self.digits_i2w = INDICTRANS_DIGITS_I2W
		self.hashh_u2i = INDICTRANS_HASHH_U2I
		self.unicode_norm_hashh_u2i = INDICTRANS_UNICODE_NORM_HASHH_U2I
		self.hasht_u2i = INDICTRANS_HASHT_U2I
		self.hashp_u2i = INDICTRANS_HASHP_U2I
		self.unicode_norm_hashp_u2i = INDICTRANS_UNICODE_NORM_HASHP_U2I
		self.hashk_u2i = INDICTRANS_HASHK_U2I
		self.hashm_u2i = INDICTRANS_HASHM_U2I
		self.hashb_u2i = INDICTRANS_HASHB_U2I
		self.unicode_norm_hashb_u2i = INDICTRANS_UNICODE_NORM_HASHB_U2I
		self.hashta_u2i = INDICTRANS_HASHTA_U2I
		self.hasho_u2i = INDICTRANS_HASHO_U2I
		self.unicode_norm_hasho_u2i = INDICTRANS_UNICODE_NORM_HASHO_U2I
		self.hashg_u2i = INDICTRANS_HASHG_U2I

		# compile regexes
		self.c = re.compile("([\xB3-\xD8])")
		self.v = re.compile("([\xA5-\xB2])")
		self.dig = re.compile("([\xF1-\xFA])")
		self.ch = re.compile("([\xB3-\xD8])\xE8")
		self.cn = re.compile("([\xB3-\xD8])\xE9")
		self.amd = re.compile("[\xA4]([\xA1-\xA3])")
		self.cm = re.compile("([\xB3-\xD8])([\xDA-\xE7])")
		self.vmd = re.compile("([\xA5-\xB2])([\xA1-\xA3])")
		self.cnh = re.compile("([\xB3-\xD8])\xE9\xE8")
		self.cmd = re.compile("([\xB3-\xD8])([\xA1-\xA3])")
		self.cnm = re.compile("([\xB3-\xD8])\xE9([\xDA-\xE7])")
		self.cnmd = re.compile("([\xB3-\xD8])\xE9([\xA1-\xA3])")
		self.cmmd = re.compile("([\xB3-\xD8])([\xDA-\xE7])([\xA1-\xA3])")
		self.cnmmd = re.compile("([\xB3-\xD8])\xE9([\xDA-\xE7])([\xA1-\xA3])")
		self.u2i_h = re.compile("([\u0900-\u097F])")
		self.u2i_t = re.compile("([\u0C01-\u0C6F])")
		self.u2i_k = re.compile("([\u0C80-\u0CFF])")
		self.u2i_m = re.compile("([\u0D00-\u0D6F])")
		self.u2i_b = re.compile("([\u0980-\u09EF])")
		self.u2i_o = re.compile("([\u0B00-\u0B7F])")
		self.u2i_p = re.compile("([\u0A01-\u0A75])")
		self.u2i_g = re.compile("([\u0A80-\u0AFF])")
		self.u2i_ta = re.compile("([\u0B82-\u0BEF])")
		self.u2i_hn = re.compile("([\u0958-\u095F])")
		self.u2i_on = re.compile("([\u0B5C\u0B5D\u0B5F])")
		self.u2i_bn = re.compile("([\u09DC\u09DD\u09DF])")
		self.u2i_pn = re.compile("([\u0A59-\u0A5B\u0A5E])")

	def normalize(self, text):
		"""Performs some common normalization, which includes:
		- Byte order mark, word joiner, etc. removal
		- ZERO_WIDTH_NON_JOINER and ZERO_WIDTH_JOINER removal
		"""
		text = text.replace('\uFEFF', '')  # BYTE_ORDER_MARK
		text = text.replace('\uFFFE', '')  # BYTE_ORDER_MARK_2
		text = text.replace('\u2060', '')  # WORD JOINER
		text = text.replace('\u00AD', '')  # SOFT_HYPHEN
		text = text.replace('\u200C', '')  # ZERO_WIDTH_NON_JOINER
		text = text.replace('\u200D', '')  # ZERO_WIDTH_JOINER
		# Convert Devanagari VIRAM and Deergh Viram to "fullstop"
		text = text.replace('\u0964', '.')
		text = text.replace('\u0965', '.')

		return text

	def map_ZeV(self, my_string):
		if 'ZeV' not in my_string:
			return my_string
		my_string = self.cZeVmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashm_w2i["eV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.cZeV.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashm_w2i["eV"], my_string)
		return my_string

	def map_eV(self, my_string):
		if 'eV' not in my_string:
			return my_string
		my_string = self.ceVmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.ceV.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"], my_string)
		return my_string

	def map_EY(self, my_string):
		if 'EY' not in my_string:
			return my_string
		my_string = self.cEYmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.cEY.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"], my_string)
		return my_string

	def map_ZoV(self, my_string):
		if 'ZoV' not in my_string:
			return my_string
		my_string = self.cZoVmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashm_w2i["oV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.cZoV.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashm_w2i["oV"], my_string)
		return my_string

	def map_oV(self, my_string):
		if 'oV' not in my_string:
			return my_string
		my_string = self.coVmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.coV.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"], my_string)
		return my_string

	def map_OY(self, my_string):
		if 'OY' not in my_string:
			return my_string
		if 'Z' in my_string:
			my_string = self.cZOY.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashm_w2i["OY"], my_string)
		my_string = self.cOYmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.cOY.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"], my_string)
		return my_string

	def map_Z(self, my_string):
		if 'Z' not in my_string:
			return my_string
		my_string = self.cZvmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashm_w2i[ m.group(2)] + self.hashmd_w2i[ m.group(3)], my_string)
		my_string = self.cZv.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashm_w2i[ m.group(2)], my_string)
		my_string = self.cZamd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.cZmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.cZa.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"], my_string)
		my_string = self.cYZa.sub(
			lambda m: self.hashc_w2i[ m.group(1) + "Y"] + self.hashc_w2i["Z"], my_string)
		my_string = self.cZ.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["Z"] + self.hashc_w2i["_"], my_string)
		return my_string

	def map_q(self, my_string):
		if 'q' not in my_string:
			return my_string
		my_string = self.cqmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["q"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.qmd.sub(
			lambda m: self.hashv_w2i["q"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = self.cq.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["q"], my_string)
		my_string = self.aqmd.sub(
			lambda m: self.hashv_w2i["aq"] + self.hashmd_w2i[ m.group(1)], my_string)
		return my_string

	def map_lYY(self, my_string):
		if 'lYY' not in my_string:
			return my_string
		my_string = re.sub( '(lYY)eV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lYY)eV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"], my_string)
		my_string = re.sub( '(lYY)EY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lYY)EY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"], my_string)
		my_string = re.sub( '(lYY)oV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lYY)oV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"], my_string)
		my_string = re.sub( '(lYY)OY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lYY)OY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"], my_string)
		my_string = re.sub( '(lYY)([AiIuUeEoO])([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)] + self.hashmd_w2i[ m.group(3)], my_string)
		my_string = re.sub( '(lYY)([AiIuUeEoO])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lYY)a([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lYY)a',
			lambda m: self.hashc_w2i[ m.group(1)], my_string)
		my_string = re.sub( '(lYY)',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["_"], my_string)
		return my_string

	def map_lY(self, my_string):
		if 'lY' not in my_string:
			return my_string
		my_string = re.sub( '(lY)eV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lY)eV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"], my_string)
		my_string = re.sub( '(lY)EY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lY)EY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"], my_string)
		my_string = re.sub( '(lY)oV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lY)oV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"], my_string)
		my_string = re.sub( '(lY)OY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lY)OY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"], my_string)
		my_string = re.sub( '(lY)([AiIuUeEoO])([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)] + self.hashmd_w2i[ m.group(3)], my_string)
		my_string = re.sub( '(lY)([AiIuUeEoO])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lY)a([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(lY)a',
			lambda m: self.hashc_w2i[ m.group(1)], my_string)
		my_string = re.sub( '(lY)',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["_"], my_string)
		return my_string

	def map_nY(self, my_string):
		if 'nY' not in my_string:
			return my_string
		my_string = re.sub( '(nY)eV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(nY)eV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"], my_string)
		my_string = re.sub( '(nY)EY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(nY)EY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"], my_string)
		my_string = re.sub( '(nY)oV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(nY)oV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"], my_string)
		my_string = re.sub( '(nY)OY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(nY)OY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"], my_string)
		my_string = re.sub( '(nY)([AiIuUeEoO])([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)] + self.hashmd_w2i[ m.group(3)], my_string)
		my_string = re.sub( '(nY)([AiIuUeEoO])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(nY)a([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(nY)a',
			lambda m: self.hashc_w2i[ m.group(1)], my_string)
		my_string = re.sub( '(nY)',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["_"], my_string)
		return my_string

	def map_rY(self, my_string):
		if 'rY' not in my_string:
			return my_string
		my_string = re.sub( '(rY)eV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(rY)eV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["eV"], my_string)
		my_string = re.sub( '(rY)EY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(rY)EY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["EY"], my_string)
		my_string = re.sub( '(rY)oV([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(rY)oV',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["oV"], my_string)
		my_string = re.sub( '(rY)OY([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(rY)OY',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i["OY"], my_string)
		my_string = re.sub( '(rY)([AiIuUeEoO])([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)] + self.hashmd_w2i[ m.group(3)], my_string)
		my_string = re.sub( '(rY)([AiIuUeEoO])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(rY)a([MHz])',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '(rY)a',
			lambda m: self.hashc_w2i[ m.group(1)], my_string)
		my_string = re.sub( '(rY)',
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["_"], my_string)
		return my_string

	def map_eV2(self, my_string):
		if 'eV' not in my_string:
			return my_string
		my_string = re.sub( 'aeV([MHz])',
			lambda m: self.hashv_w2i["aeV"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('aeV', self.hashv_w2i["aeV"])
		my_string = re.sub( 'eV([MHz])',
			lambda m: self.hashv_w2i["eV"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('eV', self.hashv_w2i["eV"])
		return my_string

	def map_EY2(self, my_string):
		if 'EY' not in my_string:
			return my_string
		my_string = re.sub( 'aEY([MHz])',
			lambda m: self.hashv_w2i["aEY"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('aEY', self.hashv_w2i["aEY"])
		my_string = re.sub( 'EY([MHz])',
			lambda m: self.hashv_w2i["EY"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('EY', self.hashv_w2i["EY"])
		return my_string

	def map_oV2(self, my_string):
		if 'oV' not in my_string:
			return my_string
		my_string = re.sub( 'aoV([MHz])',
			lambda m: self.hashv_w2i["aoV"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('aoV', self.hashv_w2i["aoV"])
		my_string = re.sub( 'oV([MHz])',
			lambda m: self.hashv_w2i["oV"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('oV', self.hashv_w2i["oV"])
		return my_string

	def map_OY2(self, my_string):
		if 'OY' not in my_string:
			return my_string
		my_string = re.sub( 'aOY([MHz])',
			lambda m: self.hashv_w2i["aOY"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('aOY', self.hashv_w2i["aOY"])
		my_string = re.sub( 'OY([MHz])',
			lambda m: self.hashv_w2i["OY"] + self.hashmd_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('OY', self.hashv_w2i["OY"])
		return my_string

	def map_a(self, my_string):
		if 'a' not in my_string:
			return my_string
		my_string = re.sub(r'\BaA', self.hashv_w2i["aA"], my_string)
		my_string = re.sub(r'\Bai', self.hashv_w2i["ai"], my_string)
		my_string = re.sub(r'\BaI', self.hashv_w2i["aI"], my_string)
		my_string = re.sub(r'\Bau', self.hashv_w2i["au"], my_string)
		my_string = re.sub(r'\BaU', self.hashv_w2i["aU"], my_string)
		my_string = re.sub(r'\Bae', self.hashv_w2i["ae"], my_string)
		my_string = re.sub(r'\BaE', self.hashv_w2i["aE"], my_string)
		my_string = re.sub(r'\Bao', self.hashv_w2i["ao"], my_string)
		my_string = re.sub(r'\BaO', self.hashv_w2i["aO"], my_string)
		return my_string

	def wx2iscii(self, my_string):
		"""Convert WX to ISCII"""
		if self.lang_tag == 'pan':
			my_string = my_string.replace('EY', self.hashv_w2i["E"] + 'Y')
		my_string = self.map_ZeV(my_string)
		my_string = self.map_eV(my_string)
		my_string = self.map_EY(my_string)
		my_string = self.map_ZoV(my_string)
		my_string = self.map_oV(my_string)
		my_string = self.map_OY(my_string)
		my_string = self.map_Z(my_string)
		my_string = self.map_q(my_string)
		my_string = self.map_lYY(my_string)
		my_string = self.map_lY(my_string)
		my_string = self.map_nY(my_string)
		my_string = self.map_rY(my_string)

		my_string = self.cvmd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)] + self.hashmd_w2i[ m.group(3)], my_string)
		my_string = self.cv.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashm_w2i[ m.group(2)], my_string)
		my_string = self.camd.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = self.ca.sub(
			lambda m: self.hashc_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('aq', self.hashv_w2i["aq"])
		my_string = my_string.replace('q', self.hashv_w2i["aq"])
		my_string = self.c.sub(
			lambda m: self.hashc_w2i[ m.group(1)] + self.hashc_w2i["_"], my_string)
		# Added for the case of U0946
		my_string = self.map_eV2(my_string)
		# Added for the case of U0945
		my_string = self.map_EY2(my_string)
		# Added for the case of U094A
		my_string = self.map_oV2(my_string)
		# Added for the case of U0949
		my_string = self.map_OY2(my_string)
		my_string = self.map_a(my_string)

		my_string = re.sub( '([aAiIuUeEoO])([MHz])',
			lambda m: self.hashv_w2i[ m.group(1)] + self.hashmd_w2i[ m.group(2)], my_string)
		my_string = re.sub( '([aAiIuUeEoO])',
			lambda m: self.hashv_w2i[ m.group(1)], my_string)
		my_string = my_string.replace('.', self.hashc_w2i["."])
		# For PUNJABI ADDAK
		my_string = my_string.replace("Y", "\xFB")
		# Replace Roman Digits with ISCII
		my_string = self.dig.sub(
			lambda m: self.digits_w2i[ m.group(1)], my_string)
		return my_string

	def iscii2unicode(self, iscii):
		"""Convert ISCII to Unicode"""
		if self.lang_tag in ["hin", "mar", "nep", "bod", "kok"]:
			unicode_ = self.iscii2unicode_hin(iscii)
		elif self.lang_tag == "tel":
			unicode_ = self.iscii2unicode_tel(iscii)
		elif self.lang_tag in ["ben", "asm"]:
			unicode_ = self.iscii2unicode_ben(iscii)
		elif self.lang_tag == "kan":
			unicode_ = self.iscii2unicode_kan(iscii)
		elif self.lang_tag == "pan":
			unicode_ = self.iscii2unicode_pan(iscii)
		elif self.lang_tag == "mal":
			unicode_ = self.iscii2unicode_mal(iscii)
		elif self.lang_tag == "tam":
			unicode_ = self.iscii2unicode_tam(iscii)
		elif self.lang_tag == "ori":
			unicode_ = self.iscii2unicode_ori(iscii)
		elif self.lang_tag == "guj":
			unicode_ = self.iscii2unicode_guj(iscii)
		else:
			raise NotImplementedError( 'Language `%s` is not implemented.' % self.lang_tag)
		return unicode_

	def iscii2unicode_hin(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hashh_i2u.get( m.group(1), ""), iscii)
		return unicode_

	def iscii2unicode_tel(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hasht_i2u.get( m.group(1), ""), iscii)
		return unicode_

	def iscii2unicode_pan(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hashp_i2u.get( m.group(1), ""), iscii)
		return unicode_

	def iscii2unicode_kan(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hashk_i2u.get( m.group(1), ""), iscii)
		unicode_ = unicode_.replace('\u0CAB\u0CBC', '\u0CDE')
		return unicode_

	def iscii2unicode_mal(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hashm_i2u.get( m.group(1), ""), iscii)
		return unicode_

	def iscii2unicode_ben(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hashb_i2u.get( m.group(1), ""), iscii)
		return unicode_

	def iscii2unicode_tam(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hashcta_i2u.get( m.group(1), ""), iscii)
		return unicode_

	def iscii2unicode_ori(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hasho_i2u.get( m.group(1), ""), iscii)
		unicode_ = unicode_.replace('\u0B2F\u0B3C', '\u0B5F')
		return unicode_

	def iscii2unicode_guj(self, iscii):
		unicode_ = self.i2u.sub(
			lambda m: self.hashg_i2u.get( m.group(1), ""), iscii)
		return unicode_

	def unicode2iscii(self, unicode_):
		"""Convert Unicode to ISCII"""
		if self.lang_tag in ["hin", "mar", "nep", "bod", "kok"]:
			iscii = self.unicode2iscii_hin(unicode_)
		elif self.lang_tag == "tel":
			iscii = self.unicode2iscii_tel(unicode_)
		elif self.lang_tag in ["ben", "asm"]:
			iscii = self.unicode2iscii_ben(unicode_)
		elif self.lang_tag == "kan":
			iscii = self.unicode2iscii_kan(unicode_)
		elif self.lang_tag == "pan":
			iscii = self.unicode2iscii_pan(unicode_)
		elif self.lang_tag == "mal":
			iscii = self.unicode2iscii_mal(unicode_)
		elif self.lang_tag == "tam":
			iscii = self.unicode2iscii_tam(unicode_)
		elif self.lang_tag == "ori":
			iscii = self.unicode2iscii_ori(unicode_)
		elif self.lang_tag == "guj":
			iscii = self.unicode2iscii_guj(unicode_)
		else:
			raise NotImplementedError( 'Language `%s` is not implemented.' % self.lang_tag)
		return iscii

	def iscii2wx(self, my_string):
		"""Convert ISCII to WX"""
		# CONSONANT+HALANT
		my_string = self.ch.sub(
			lambda m: self.hashc_i2w[
				m.group(1)], my_string)
		# CONSONANT+NUKTA+MATRA+MODIFIER
		my_string = self.cnmmd.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + self.hashc_i2w["\xE9"] + self.hashm_i2w[ m.group(2)] +
			self.hashmd_i2w[ m.group(3)], my_string)
		# CONSONANT+NUKTA+MATRA
		my_string = self.cnm.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + self.hashc_i2w["\xE9"] + self.hashm_i2w[ m.group(2)], my_string)
		# CONSONANT+NUKTA+MODIFIER
		my_string = self.cnmd.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + self.hashc_i2w["\xE9"] + self.hashmd_i2w[ m.group(2)], my_string)
		# CONSONANT+NUKTA+HALANT
		my_string = self.cnh.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + self.hashc_i2w["\xE9"], my_string)
		# CONSONANT+NUKTA
		my_string = self.cn.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + self.hashc_i2w["\xE9"] + "a", my_string)
		# CONSONANT+MATRA+MODIFIER
		my_string = self.cmmd.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + self.hashm_i2w[ m.group(2)] + self.hashmd_i2w[ m.group(3)], my_string)
		# CONSONANT+MATRA
		my_string = self.cm.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + self.hashm_i2w[ m.group(2)], my_string)
		# CONSONANT+MODIFIER
		my_string = self.cmd.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + "a" + self.hashmd_i2w[ m.group(2)], my_string)
		# CONSONANT
		my_string = self.c.sub(
			lambda m: self.hashc_i2w[ m.group(1)] + "a", my_string)
		# VOWEL+MODIFIER, VOWEL, MATRA
		my_string = self.vmd.sub(
			lambda m: self.hashv_i2w[ m.group(1)] + self.hashmd_i2w[ m.group(2)], my_string)
		my_string = self.amd.sub(
			lambda m: "a" + self.hashmd_i2w[ m.group(1)], my_string)
		my_string = self.v.sub(
			lambda m: self.hashv_i2w[m.group(1)], my_string)
		# VOWEL A, FULL STOP or VIRAM Northern Scripts
		my_string = my_string.replace("\xA4", "a")
		my_string = my_string.replace("\xEA", ".")
		# For PUNJABI ADDAK
		my_string = my_string.replace("\xFB", "Y")
		# Replace ISCII Digits with Roman
		my_string = self.dig.sub(
			lambda m: self.digits_i2w[ m.group(1)], my_string)

		return my_string

	def unicode2iscii_hin(self, unicode_):
		# Normalize Unicode values (NUKTA variations)
		unicode_ = self.u2i_hn.sub(
			lambda m: self.unicode_norm_hashh_u2i.get( m.group(1), "") + "\u093C", unicode_)
		# Convert Unicode values to ISCII values
		iscii_hin = self.u2i_h.sub(
			lambda m: self.hashh_u2i.get( m.group(1), ""), unicode_)
		return iscii_hin

	def unicode2iscii_tel(self, unicode_):
		# dependent vowels
		unicode_ = unicode_.replace('\u0c46\u0c56', '\u0c48')
		# Convert Telugu Unicode values to ISCII values
		iscii_tel = self.u2i_t.sub(
			lambda m: self.hasht_u2i.get( m.group(1), ""), unicode_)
		return iscii_tel

	def unicode2iscii_pan(self, unicode_):
		# Normalize Unicode values (NUKTA variations)
		unicode_ = self.u2i_pn.sub(lambda m: self.unicode_norm_hashp_u2i.get( m.group(1), "") + "\u0A3C", unicode_)
		# Convert Unicode values 0x0A5C to ISCII
		unicode_ = unicode_.replace("\u0A5C", "\xBF\xE9")
		# Convert Unicode Punjabi values to ISCII values
		iscii_pan = self.u2i_p.sub(
			lambda m: self.hashp_u2i.get( m.group(1), ""), unicode_)
		return iscii_pan

	def unicode2iscii_kan(self, unicode_):
		# Normalize Unicode values (NUKTA variations)
		unicode_ = unicode_.replace('\u0CDE', '\u0CAB\u0CBC')
		# Normalize two-part dependent vowels
		unicode_ = unicode_.replace('\u0cbf\u0cd5', '\u0cc0')
		unicode_ = unicode_.replace('\u0cc6\u0cd5', '\u0cc7')
		unicode_ = unicode_.replace('\u0cc6\u0cd6', '\u0cc8')
		unicode_ = unicode_.replace('\u0cc6\u0cc2', '\u0cca')
		unicode_ = unicode_.replace('\u0cca\u0cd5', '\u0ccb')
		# Convert Unicode values to ISCII values
		iscii_kan = self.u2i_k.sub(
			lambda m: self.hashk_u2i.get( m.group(1), ""), unicode_)
		return iscii_kan

	def unicode2iscii_mal(self, unicode_):
		# Normalize two-part dependent vowels
		unicode_ = unicode_.replace('\u0d46\u0d3e', '\u0d4a')
		unicode_ = unicode_.replace('\u0d47\u0d3e', '\u0d4b')
		unicode_ = unicode_.replace('\u0d46\u0d57', '\u0d57')
		# Convert Unicode values to ISCII values
		iscii_mal = self.u2i_m.sub(
			lambda m: self.hashm_u2i.get( m.group(1), ""), unicode_)
		return iscii_mal

	def unicode2iscii_ben(self, unicode_):
		# Normalize Unicode values (NUKTA variations)
		unicode_ = self.u2i_bn.sub(
			lambda m: self.unicode_norm_hashb_u2i.get( m.group(1), "") + "\u09BC", unicode_)
		# Normalize two part dependent vowels
		unicode_ = unicode_.replace('\u09c7\u09be', '\u09cb')
		unicode_ = unicode_.replace('\u09c7\u0bd7', '\u09cc')
		# Convert Unicode values to ISCII values
		iscii_ben = self.u2i_b.sub(
			lambda m: self.hashb_u2i.get( m.group(1), ""), unicode_)
		return iscii_ben

	def unicode2iscii_tam(self, unicode_):
		# Normalizetwo part dependent vowels
		unicode_ = unicode_.replace('\u0b92\u0bd7', '\u0b94')
		unicode_ = unicode_.replace('\u0bc6\u0bbe', '\u0bca')
		unicode_ = unicode_.replace('\u0bc7\u0bbe', '\u0bcb')
		unicode_ = unicode_.replace('\u0bc6\u0bd7', '\u0bcc')
		# Convert Unicode values to ISCII values
		iscii_tam = self.u2i_ta.sub(
			lambda m: self.hashta_u2i.get( m.group(1), ""), unicode_)
		return iscii_tam

	def unicode2iscii_ori(self, unicode_):
		# Normalize Unicode values (NUKTA variations)
		unicode_ = self.u2i_on.sub(
			lambda m: self.unicode_norm_hasho_u2i.get( m.group(1), "") + "\u0B3C", unicode_)
		# Normalize two part dependent vowels
		unicode_ = unicode_.replace('\u0b47\u0b3e', '\u0b4b')
		unicode_ = unicode_.replace('\u0b47\u0b57', '\u0b4c')
		# Convert Unicode values to ISCII values
		iscii_ori = self.u2i_o.sub(
			lambda m: self.hasho_u2i.get( m.group(1), ""), unicode_)
		return iscii_ori

	def unicode2iscii_guj(self, unicode_):
		# Convert Gujurati Unicode values to ISCII values
		iscii_guj = self.u2i_g.sub(
			lambda m: self.hashg_u2i.get( m.group(1), ""), unicode_)
		return iscii_guj

	def utf2wx(self, unicode_):
		"""Convert UTF string to WX-Roman"""
		unicode_ = self.normalize(unicode_)
		# Mask iscii characters (if any)
		unicode_ = self.mask_isc.sub(
			lambda m: self.iscii_num[ m.group(1)], unicode_)
		# Convert Unicode values to ISCII values
		iscii = self.unicode2iscii(unicode_)
		# Convert ISCII to WX-Roman
		wx = self.iscii2wx(iscii)
		# Consecutive Vowel Normalization
		wx = re.sub('[\xA0-\xFA]+', '', wx)
		# Unmask iscii characters
		wx = self.unmask_isc.sub(
			lambda m: self.num_iscii[m.group(1)], wx)
		return wx

	def wx2utf(self, wx):
		"""Convert WX-Roman to UTF"""
		# Mask iscii characters (if any)
		wx = self.mask_isc.sub(
			lambda m: self.iscii_num[ m.group(1)], wx)
		iscii = self.wx2iscii(wx)
		# Convert ISCII to Unicode
		unicode_ = self.iscii2unicode(iscii)
		# Unmask iscii characters
		unicode_ = self.unmask_isc.sub(
			lambda m: self.num_iscii[ m.group(1)], unicode_)
		return unicode_
