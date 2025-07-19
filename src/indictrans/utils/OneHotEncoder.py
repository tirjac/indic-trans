# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/utils/OneHotEncoder.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   OneHotEncoder.py :  OneHot encoder for dense and sparse
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

import numpy as np
from scipy import sparse as sp

class OneHotEncoder():
	"""Transforms categorical features to continuous numeric features.  """

	def fit(self, X):
		"""Fit OneHotEncoder to X.  """
		data = np.asarray(X)
		unique_feats = []
		offset = 0
		for i in range(data.shape[1]):
			feat_set_i = set(data[:, i])
			d = {val: i + offset for i, val in enumerate(feat_set_i)}
			unique_feats.append(d)
			offset += len(feat_set_i)

		self.unique_feats = unique_feats
		return self

	def transform(self, X, sparse=True):
		"""Transform X using one-hot encoding. """
		X = np.atleast_2d(X)
		if sparse:
			one_hot_matrix = sp.lil_matrix( (len(X), sum(len(i) for i in self.unique_feats)))
		else:
			one_hot_matrix = np.zeros( (len(X), sum(len(i) for i in self.unique_feats)), bool)
		for i, vec in enumerate(X):
			for j, val in enumerate(vec):
				if val in self.unique_feats[j]:
					one_hot_matrix[i, self.unique_feats[j][val]] = 1.0

		return sp.csr_matrix(one_hot_matrix) if sparse else one_hot_matrix
