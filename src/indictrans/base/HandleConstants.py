# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/base/HandleConstants.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   HandleConstants.py : constants
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

INDICTRANS_URDU_MAP = {
	ord('\u0643') : '\u06a9', ord('\u0647') : '\u06c1', ord('\u0649') : '\u06cc', 
	ord('\u064a') : '\u06cc', ord('\u0660') : '\u06f0', ord('\u0661') : '\u06f1',
	ord('\u0662') : '\u06f2', ord('\u0663') : '\u06f3', ord('\u0664') : '\u06f4', 
	ord('\u0665') : '\u06f5', ord('\u0666') : '\u06f6', ord('\u0667') : '\u06f7',
	ord('\u0668') : '\u06f8', ord('\u0669') : '\u06f9', ord('\uff00') : '\u0621', 
	ord('\uff01') : '\u0622', ord('\ufee2') : '\u0622', ord('\ufee5') : '\u0624',
	ord('\ufee6') : '\u0624', ord('\ufef1') : '\u0626', ord('\ufef2') : '\u0626', 
	ord('\ufef3') : '\u0626', ord('\ufef4') : '\u0626', ord('\ufe8d') : '\u0627',
	ord('\ufe8e') : '\u0627', ord('\ufe8f') : '\u0628', ord('\ufe90') : '\u0628', 
	ord('\ufe91') : '\u0628', ord('\ufe92') : '\u0628', ord('\ufe93') : '\u062a',
	ord('\ufe94') : '\u062a', ord('\ufe95') : '\u062a', ord('\ufe96') : '\u062a', 
	ord('\ufe97') : '\u062a', ord('\ufe98') : '\u062a', ord('\ufe99') : '\u062b',
	ord('\ufe9a') : '\u062b', ord('\ufe9b') : '\u062b', ord('\ufe9c') : '\u062b', 
	ord('\ufe9d') : '\u062c', ord('\ufe9e') : '\u062c', ord('\ufe9f') : '\u062c',
	ord('\ufea0') : '\u062c', ord('\ufea1') : '\u062d', ord('\ufea2') : '\u062d', 
	ord('\ufea3') : '\u062d', ord('\ufea4') : '\u062d', ord('\ufea5') : '\u062e',
	ord('\ufea6') : '\u062e', ord('\ufea7') : '\u062e', ord('\ufea8') : '\u062e', 
	ord('\ufea9') : '\u062f', ord('\ufeaa') : '\u062f', ord('\ufeab') : '\u0630',
	ord('\ufeac') : '\u0630', ord('\ufead') : '\u0631', ord('\ufeae') : '\u0631', 
	ord('\ufeaf') : '\u0632', ord('\ufeb0') : '\u0632', ord('\ufeb1') : '\u0633',
	ord('\ufeb2') : '\u0633', ord('\ufeb3') : '\u0633', ord('\ufeb4') : '\u0633', 
	ord('\ufeb5') : '\u0634', ord('\ufeb6') : '\u0634', ord('\ufeb7') : '\u0634',
	ord('\ufeb8') : '\u0634', ord('\ufeb9') : '\u0635', ord('\ufeba') : '\u0635', 
	ord('\ufebb') : '\u0635', ord('\ufebc') : '\u0635', ord('\ufebd') : '\u0636',
	ord('\ufebe') : '\u0636', ord('\ufebf') : '\u0636', ord('\ufec0') : '\u0636', 
	ord('\ufec1') : '\u0637', ord('\ufec2') : '\u0637', ord('\ufec3') : '\u0637',
	ord('\ufec4') : '\u0637', ord('\ufec5') : '\u0638', ord('\ufec6') : '\u0638', 
	ord('\ufec7') : '\u0638', ord('\ufec8') : '\u0638', ord('\ufec9') : '\u0639',
	ord('\ufeca') : '\u0639', ord('\ufecb') : '\u0639', ord('\ufecc') : '\u0639', 
	ord('\ufecd') : '\u063a', ord('\ufece') : '\u063a', ord('\ufecf') : '\u063a',
	ord('\ufed0') : '\u063a', ord('\ufed1') : '\u0641', ord('\ufed2') : '\u0641', 
	ord('\ufed3') : '\u0641', ord('\ufed4') : '\u0641', ord('\ufed5') : '\u0642',
	ord('\ufed6') : '\u0642', ord('\ufed7') : '\u0642', ord('\ufed8') : '\u0642', 
	ord('\ufed9') : '\u06a9', ord('\ufeda') : '\u06a9', ord('\ufedb') : '\u06a9',
	ord('\ufedc') : '\u06a9', ord('\ufedd') : '\u0644', ord('\ufede') : '\u0644', 
	ord('\ufedf') : '\u0644', ord('\ufee0') : '\u0644', ord('\ufee1') : '\u0645',
	ord('\ufee2') : '\u0645', ord('\ufee3') : '\u0645', ord('\ufee4') : '\u0645', 
	ord('\ufee5') : '\u0646', ord('\ufee6') : '\u0646', ord('\ufee7') : '\u0646',
	ord('\ufee8') : '\u0646', ord('\ufee9') : '\u06c1', ord('\ufeea') : '\u06c1', 
	ord('\ufeeb') : '\u06be', ord('\ufeec') : '\u06be', ord('\ufeed') : '\u0648',
	ord('\ufeee') : '\u0648', ord('\ufeef') : '\u06cc', ord('\ufef0') : '\u06cc', 
	ord('\ufef1') : '\u06cc', ord('\ufef2') : '\u06cc', ord('\ufef3') : '\u06cc',
	ord('\ufef4') : '\u06cc', ord('\ufef5') : '\u0644\u0627', ord('\ufef6') : '\u0644\u0627', 
	ord('\ufb56') : '\u067e', ord('\ufb57') : '\u067e', ord('\ufb58') : '\u067e',
	ord('\ufb59') : '\u067e', ord('\ufb5e') : '\u062a', ord('\ufb5f') : '\u062a', 
	ord('\ufb60') : '\u062a', ord('\ufb61') : '\u062a', ord('\ufb66') : '\u0679',
	ord('\ufb67') : '\u0679', ord('\ufb68') : '\u0679', ord('\ufb69') : '\u0679', 
	ord('\ufb7a') : '\u0686', ord('\ufb7b') : '\u0686', ord('\ufb7c') : '\u0686',
	ord('\ufb7d') : '\u0686', ord('\ufb88') : '\u0688', ord('\ufb89') : '\u0688', 
	ord('\ufb8a') : '\u0698', ord('\ufb8b') : '\u0698', ord('\ufb8c') : '\u0691',
	ord('\ufb8d') : '\u0691', ord('\ufb8e') : '\u06a9', ord('\ufb8f') : '\u06a9', 
	ord('\ufb90') : '\u06a9', ord('\ufb91') : '\u06a9', ord('\ufb92') : '\u06af',
	ord('\ufb93') : '\u06af', ord('\ufb94') : '\u06af', ord('\ufb95') : '\u06af', 
	ord('\ufb9e') : '\u06ba', ord('\ufb9f') : '\u06ba', ord('\ufba6') : '\u06c1',
	ord('\ufba7') : '\u06c1', ord('\ufba8') : '\u06c1', ord('\ufba9') : '\u06c1', 
	ord('\ufbaa') : '\u06be', ord('\ufbab') : '\u06be', ord('\ufbac') : '\u06be',
	ord('\ufbad') : '\u06be', ord('\ufbae') : '\u06d2', ord('\ufbaf') : '\u06d2', 
	ord('\ufbb0') : '\u06d3', ord('\ufbb1') : '\u06d3', ord('\ufbfc') : '\u06cc',
	ord('\ufbfd') : '\u06cc', ord('\ufbfe') : '\u06cc', ord('\ufbff') : '\u06cc', 
	ord('\ufefb') : '\u0644\u0622', ord('\u0623') : '\u0627\u0654', ord('\u06c0') : '\u06c1\u0654',
}

INDICTRANS_PUNKT_URDU_MAP = {
	ord(';') : '\u061b', ord(',') : '\u060c', 
	ord('%') : '\u066a', ord('*') : '\u066d', ord('?') : '\u061f', ord('\u0964') : '\u06d4',
	ord('.') : '\u06d4', ord('\u0966') : '\u0660', ord('\u0967') : '\u0661', 
	ord('\u0968') : '\u0662', ord('\u0969') : '\u0663', ord('\u096a') : '\u0664',
	ord('\u096b') : '\u0665', ord('\u096c') : '\u0666', ord('\u096d') : '\u0667', 
	ord('\u096e') : '\u0668', ord('\u096f') : '\u0669', ord('\u0966') : '\u06f0',
	ord('\u0967') : '\u06f1', ord('\u0968') : '\u06f2', ord('\u0969') : '\u06f3', 
	ord('\u096a') : '\u06f4', ord('\u096b') : '\u06f5', ord('\u096c') : '\u06f6',
	ord('\u096d') : '\u06f7', ord('\u096e') : '\u06f8', ord('\u096f') : '\u06f9', 
	ord('0') : '\u06f0', ord('1') : '\u06f1', ord('2') : '\u06f2',
	ord('3') : '\u06f3', ord('4') : '\u06f4', ord('5') : '\u06f5', 
	ord('6') : '\u06f6', ord('7') : '\u06f7', ord('8') : '\u06f8',
	ord('9') : '\u06f9', 
}

INDICTRANS_PUNKT_MAP = {
	ord('\u061b') : ';', ord('\u060c') : ',', 
	ord('\u066a') : '%', ord('\u066d') : '*', ord('\u061f') : '?', ord('\u066e') : "'",
	ord('\u06d4') : '\u0964', ord('\u06d4') : '.', ord('\u066e') : "'", 
	ord('\u2018') : "'", ord('\u2019') : "'", ord('\u201c') : '"',
	ord('\u201d') : '"', ord('\u0660') : '\u0966', ord('\u0661') : '\u0967', 
	ord('\u0662') : '\u0968', ord('\u0663') : '\u0969', ord('\u0664') : '\u096a',
	ord('\u0665') : '\u096b', ord('\u0666') : '\u096c', ord('\u0667') : '\u096d', 
	ord('\u0668') : '\u096e', ord('\u0669') : '\u096f', ord('\u06f0') : '\u0966',
	ord('\u06f1') : '\u0967', ord('\u06f2') : '\u0968', ord('\u06f3') : '\u0969', 
	ord('\u06f4') : '\u096a', ord('\u06f5') : '\u096b', ord('\u06f6') : '\u096c',
	ord('\u06f7') : '\u096d', ord('\u06f8') : '\u096e', ord('\u06f9') : '\u096f', 
	ord('\u06f0') : '0', ord('\u06f1') : '1', ord('\u06f2') : '2',
	ord('\u06f3') : '3', ord('\u06f4') : '4', ord('\u06f5') : '5', 
	ord('\u06f6') : '6', ord('\u06f7') : '7', ord('\u06f8') : '8',
	ord('\u06f9') : '9', 
}

