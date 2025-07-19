# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/utils/HandleCommonUtils.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   HandleCommonUtils.py : common utils adaptor
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

from indictrans.utils.WXEncoder import WXEncoder
from indictrans.utils.OneHotEncoder import OneHotEncoder
from indictrans.putils import count_tranxn, sparse_add
from indictrans.utils.UrduNormalizer import UrduNormalizer

__all__ = ["WXEncoder", "count_tranxn", "sparse_add", "OneHotEncoder", "UrduNormalizer", "ngram_context"]

def ngram_context(letters, n=4):
	feats = []
	dummies = ["_"] * n
	context = dummies + letters + dummies
	for i in range(n, len(context) - n):
		unigrams = context[i - n: i] +\
			[context[i]] +\
			context[i + 1: i + (n + 1)]
		ngrams = ['|'.join(ng) for k in range(2, n + 1)
				  for ng in zip(*[unigrams[j:]
								  for j in range(k)])]
		feats.append(unigrams + ngrams)
	return feats
