# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/utils/BaseTransliterator.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   BaseTransliterator.py : Base class for transliterator.
# 
# This code is adapted from https://github.com/libindic/indic-trans/blob/master/indictrans/base.py
#                         - Loading is from single lazy source
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

import io
import re
import json
import os

import numpy as np
from scipy.sparse import issparse

from indictrans.utils.HandleCommonUtils import WXEncoder, OneHotEncoder, UrduNormalizer, ngram_context
from indictrans.base.HandleConstants import INDICTRANS_PUNKT_URDU_MAP, INDICTRANS_PUNKT_MAP

class BaseTransliterator(object):
	"""Base class for transliterator."""

	npzdata = None
	vecdata = None

	def get_npz_data(self, item, key):
		return BaseTransliterator.npzdata[f"{item}_{key}"]

	def get_vec_data(self, item, key):
		return BaseTransliterator.vecdata[f"{item}_{key}"]

	def _init_npz_data(self):
		if not BaseTransliterator.npzdata:
			dist_dir = os.path.dirname(os.path.abspath(__file__))
			BaseTransliterator.npzdata = np.load('%s/../models/npzdata.npz' % (dist_dir), allow_pickle=True)
		if not BaseTransliterator.vecdata:
			dist_dir = os.path.dirname(os.path.abspath(__file__))
			BaseTransliterator.vecdata = np.load('%s/../models/vecdata.npz' % (dist_dir), allow_pickle=True)

	def load_mappings(self):
		self.punkt_tbl = INDICTRANS_PUNKT_URDU_MAP if self.target == 'urd' else INDICTRANS_PUNKT_MAP

	def case_trans(self, word, k_best=5):
		raise NotImplementedError( 'Not implemented in base class')

	def __init__(self, source, target, decoder, build_lookup=False):
		self._init_npz_data()
		self._to_indic = False
		if source in ('mar', 'nep', 'kok', 'bod'):
			source = 'hin'
		elif source == 'asm':
			source = 'ben'
		if target in ('mar', 'nep', 'kok', 'bod'):
			target = 'hin'
		elif target == 'asm':
			target = 'ben'
		self.source = source
		self.target = target
		self.lookup = dict()
		self.build_lookup = build_lookup
		self.decode, self.decoder = decoder
		self.tab = '\x01\x03'  # mask tabs
		self.space = '\x02\x04'  # mask spaces
		self.esc_ch = '\x00'  # escape-sequence for Roman in WX
		self.dist_dir = os.path.dirname(os.path.abspath(__file__))
		self.base_fit()

	def load_models(self):
		"""Loads transliteration models."""
		self.vectorizer_ = OneHotEncoder()
		model = '%s-%s' % (self.source, self.target)
		self.vectorizer_.unique_feats = self.get_vec_data( model, 'sparse')
		self.classes_ = self.get_npz_data(model,'classes')[0]
		self.coef_ = self.get_npz_data(model,'coef')[0].astype(np.float64)
		self.intercept_init_ = self.get_npz_data(model,'intercept_init').astype(np.float64)
		self.intercept_trans_ = self.get_npz_data(model,'intercept_trans').astype(np.float64)
		self.intercept_final_ = self.get_npz_data(model,'intercept_final').astype(np.float64)

		# convert numpy.bytes_/numpy.string_ to numpy.unicode_
		if not isinstance(self.classes_[0], np.str_):
			self.classes_ = {k: v.decode('utf-8') for k, v in self.classes_.items()}

	def base_fit(self):
		# load models
		self.load_models()
		# load mapping tables for Urdu
		if 'urd' in [self.source, self.target]:
			self.load_mappings()
		# initialize Urdu Normalizer
		if self.source == 'urd':
			self.nu = UrduNormalizer()
		# initialize wx-converter and character-maps
		if self.source in ['eng', 'urd']:
			wxp = WXEncoder(order='wx2utf', lang=self.target)
			self.wx_process = wxp.wx2utf
		else:
			wxp = WXEncoder(order='utf2wx', lang=self.source)
			self.wx_process = wxp.utf2wx
			self.mask_roman = re.compile(r'([a-zA-Z]+)')

	def predict(self, word, k_best=5):
		"""Given encoded word matrix and HMM parameters, predicts output sequence (target word)"""
		X = self.vectorizer_.transform(word)
		if issparse(X):
			scores = X.dot(self.coef_.T).toarray()
		else:
			scores = self.coef_.dot(X.T).T
		if self.decode == 'viterbi':
			y = self.decoder(scores, self.intercept_trans_, self.intercept_init_, self.intercept_final_)
			y = [self.classes_[pid] for pid in y]
			y = ''.join(y).replace('_', '')
			return y
		else:
			top_seq = list()
			y = self.decoder(scores, self.intercept_trans_, self.intercept_init_, self.intercept_final_, k_best)
			for path in y:
				w = [self.classes_[pid] for pid in path]
				w = ''.join(w).replace('_', '')
				top_seq.append(w)
			return top_seq

	def convert_to_wx(self, text):
		"""Converts Indic scripts to WX."""
		if self.source == 'eng':
			return text.lower()
		if self.source == 'urd':
			return self.nu.normalize(text)
		if self.source == 'ben':
			# Assamese `ra` to Bengali `ra`
			text = text.replace('\u09f0', '\u09b0')
			# Assamese `va` to Bengali `va`
			text = text.replace('\u09f1', '\u09ac')
		text = self.mask_roman.sub(r'%s\1' % (self.esc_ch), text)
		text = self.wx_process(text)
		return text

	def transliterate(self, text, k_best=None):
		"""Single best transliteration using viterbi decoding."""
		trans_list = []
		text = self.convert_to_wx(text)
		text = text.replace('\t', self.tab)
		text = text.replace(' ', self.space)
		lines = text.split("\n")
		for line in lines:
			if not line.strip():
				trans_list.append(line)
				continue
			trans_line = str()
			line = self.non_alpha.split(line)
			for word in line:
				trans_line += self.case_trans(word)
			trans_list.append(trans_line)
		trans_line = '\n'.join(trans_list)
		trans_line = trans_line.replace(self.space, ' ')
		trans_line = trans_line.replace(self.tab, '\t')
		return trans_line

	def top_n_trans(self, text, k_best=5):
		"""Returns k-best transliterations using beamsearch decoding.  """
		if k_best < 2:
			raise ValueError('`k_best` value should be >= 2')
		trans_word = []
		text = self.convert_to_wx(text)
		words = self.non_alpha.split(text)
		for word in words:
			op_word = self.case_trans(word, k_best)
			if isinstance(op_word, list):
				trans_word.append(op_word)
			else:
				trans_word.append([word] * k_best)
		return [''.join(w) for w in zip(*trans_word)]
