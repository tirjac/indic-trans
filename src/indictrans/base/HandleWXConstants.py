# -*- coding: utf-8 -*-
#
# @project IndicTrans
# @file src/indictrans/base/HandleWXConstants.py
# @author  Shreos Roychowdhury <shreos@tirja.com>
# @version 1.0.0
# 
# @section DESCRIPTION
# 
#   HandleWXConstants.py : Constants from WXEncoder
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

# CONSONANTS
INDICTRANS_HASHC_W2I = {
	"k": "\xB3",
	"K": "\xB4",
	"g": "\xB5",
	"G": "\xB6",
	"f": "\xB7",
	"c": "\xB8",
	"C": "\xB9",
	"j": "\xBA",
	"J": "\xBB",
	"F": "\xBC",
	"t": "\xBD",
	"T": "\xBE",
	"d": "\xBF",
	"D": "\xC0",
	"N": "\xC1",
	"w": "\xC2",
	"W": "\xC3",
	"x": "\xC4",
	"X": "\xC5",
	"n": "\xC6",
	"p": "\xC8",
	"P": "\xC9",
	"b": "\xCA",
	"B": "\xCB",
	"m": "\xCC",
	"y": "\xCD",
	"r": "\xCF",
	"l": "\xD1",
	"v": "\xD4",
	"S": "\xD5",
	"s": "\xD7",
	"R": "\xD6",
	"h": "\xD8",
	"_": "\xE8",
	"Z": "\xE9",
	".": "\xEA",
	"Y": "\xFB",
	"lY": "\xD2",
	# Added for tamil
	"rY": "\xD0",
	"nY": "\xC7",
	"lYY": "\xD3",
}
# VOWELS
INDICTRANS_HASHV_W2I = {
	"a": "\xA4",
	"A": "\xA5",
	"aA": "\xA5",
	"i": "\xA6",
	"ai": "\xA6",
	"I": "\xA7",
	"aI": "\xA7",
	"u": "\xA8",
	"au": "\xA8",
	"U": "\xA9",
	"aU": "\xA9",
	"q": "\xAA",
	"aq": "\xAA",
	"eV": "\xAB",
	"aeV": "\xAB",
	"e": "\xAC",
	"ae": "\xAC",
	"E": "\xAD",
	"aE": "\xAD",
	"EY": "\xAE",
	"aEY": "\xAE",
	"oV": "\xAF",
	"aoV": "\xAF",
	"o": "\xB0",
	"ao": "\xB0",
	"O": "\xB1",
	"aO": "\xB1",
	"OY": "\xB2",
	"aOY": "\xB2",
}
# MATRA
INDICTRANS_HASHM_W2I = {
	"A": "\xDA",
	"aA": "\xDA",
	"i": "\xDB",
	"ai": "\xDB",
	"I": "\xDC",
	"aI": "\xDC",
	"u": "\xDD",
	"au": "\xDD",
	"U": "\xDE",
	"aU": "\xDE",
	"q": "\xDF",
	"aq": "\xDF",
	"eV": "\xE0",
	"aeV": "\xE0",
	"e": "\xE1",
	"ae": "\xE1",
	"E": "\xE2",
	"aE": "\xE2",
	"EY": "\xE3",
	"aEY": "\xE3",
	"oV": "\xE4",
	"aoV": "\xE4",
	"o": "\xE5",
	"ao": "\xE5",
	"O": "\xE6",
	"aO": "\xE6",
	"OY": "\xE7",
	"aOY": "\xE7",
}
# MODIFIERS
INDICTRANS_HASHMD_W2I = {
	"z": "\xA1",
	"M": "\xA2",
	"H": "\xA3",
}
INDICTRANS_DIGITS_W2I = {
	"0": "\xF1",
	"1": "\xF2",
	"2": "\xF3",
	"3": "\xF4",
	"4": "\xF5",
	"5": "\xF6",
	"6": "\xF7",
	"7": "\xF8",
	"8": "\xF9",
	"9": "\xFA",
}
INDICTRANS_HASHH_I2U = {
	"\xA1": "\u0901",  # Vowel-modifier CHANDRABINDU
	"\xA2": "\u0902",  # Vowel-modifier ANUSWAR
	"\xA3": "\u0903",  # Vowel-modifier VISARG
	"\xA4": "\u0905",  # Vowel A
	"\xA5": "\u0906",  # Vowel AA
	"\xA6": "\u0907",  # Vowel I
	"\xA7": "\u0908",  # Vowel II
	"\xA8": "\u0909",  # Vowel U
	"\xA9": "\u090A",  # Vowel UU
	"\xAA": "\u090B",  # Vowel RI
	"\xAB": "\u090E",  # Vowel E
	"\xAC": "\u090F",  # Vowel EY
	"\xAD": "\u0910",  # Vowel AI
	"\xAE": "\u090D",  # Vowel AI
	# "\xB2": "\u090D",  # Vowel AYE (Devanagari Script)  #FIXME
	"\xAF": "\u0912",  # Vowel O
	"\xB0": "\u0913",  # Vowel OW
	"\xB1": "\u0914",  # Vowel AU
	"\xB2": "\u0911",  # Vowel AWE
	"\xB3": "\u0915",  # Consonant KA
	"\xB4": "\u0916",  # Consonant KHA
	"\xB5": "\u0917",  # Consonant GA
	"\xB6": "\u0918",  # Consonant GHA
	"\xB7": "\u0919",  # Consonant NGA
	"\xB8": "\u091A",  # Consonant CHA
	"\xB9": "\u091B",  # Consonant CHHA
	"\xBA": "\u091C",  # Consonant JA
	"\xBB": "\u091D",  # Consonant JHA
	"\xBC": "\u091E",  # Consonant JNA
	"\xBD": "\u091F",  # Consonant Hard TA
	"\xBE": "\u0920",  # Consonant Hard THA
	"\xBF": "\u0921",  # Consonant Hard DA
	"\xC0": "\u0922",  # Consonant Hard DHA
	"\xC1": "\u0923",  # Consonant Hard NA
	"\xC2": "\u0924",  # Consonant Soft TA
	"\xC3": "\u0925",  # Consonant Soft THA
	"\xC4": "\u0926",  # Consonant Soft DA
	"\xC5": "\u0927",  # Consonant Soft DHA
	"\xC6": "\u0928",  # Consonant Soft NA
	"\xC7": "\u0929",  # Consonant NA (Tamil)
	"\xC8": "\u092A",  # Consonant PA
	"\xC9": "\u092B",  # Consonant PHA
	"\xCA": "\u092C",  # Consonant BA
	"\xCB": "\u092D",  # Consonant BHA
	"\xCC": "\u092E",  # Consonant MA
	"\xCD": "\u092F",  # Consonant YA
	"\xCF": "\u0930",  # Consonant RA
	"\xD0": "\u0931",  # Consonant Hard RA (Southern Script)
	"\xD1": "\u0932",  # Consonant LA
	"\xD2": "\u0933",  # Consonant Hard LA
	"\xD3": "\u0934",  # Consonant ZHA (Tamil & Malyalam)
	"\xD4": "\u0935",  # Consonant VA
	"\xD5": "\u0936",  # Consonant SHA
	"\xD6": "\u0937",  # Consonant Hard SHA
	"\xD7": "\u0938",  # Consonant SA
	"\xD8": "\u0939",  # Consonant HA
	"\xDA": "\u093E",  # Vowel Sign AA
	"\xDB": "\u093F",  # Vowel Sign I
	"\xDC": "\u0940",  # Vowel Sign II
	"\xDD": "\u0941",  # Vowel Sign U
	"\xDE": "\u0942",  # Vowel Sign UU
	"\xDF": "\u0943",  # Vowel Sign RI
	"\xE0": "\u0946",  # Vowel Sign E (Southern Scripts)
	"\xE1": "\u0947",  # Vowel Sign EY
	"\xE2": "\u0948",  # Vowel Sign AI
	"\xE3": "\u0945",  # Vowel Sign AYE (Devanagari Script)
	"\xE4": "\u094A",  # Vowel Sign O
	"\xE5": "\u094B",  # Vowel Sign OW
	"\xE6": "\u094C",  # Vowel Sign AU
	"\xE7": "\u0949",  # Vowel Sign AWE (Devanagari Script)
	"\xE8": "\u094D",  # Vowel Omission Sign (Halant)
	"\xE9": "\u093C",  # Diacritic Sign (Nukta)
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0966",  # Digit 0
	"\xF2": "\u0967",  # Digit 1
	"\xF3": "\u0968",  # Digit 2
	"\xF4": "\u0969",  # Digit 3
	"\xF5": "\u096A",  # Digit 4
	"\xF6": "\u096B",  # Digit 5
	"\xF7": "\u096C",  # Digit 6
	"\xF8": "\u096D",  # Digit 7
	"\xF9": "\u096E",  # Digit 8
	"\xFA": "\u096F",  # Digit 9
}
INDICTRANS_HASHT_I2U = {
	"\xA1": "\u0C01",  # Vowel-modifier CHANDRABINDU
	"\xA2": "\u0C02",  # Vowel-modifier ANUSWAR
	"\xA3": "\u0C03",  # Vowel-modifier VISARG
	"\xA4": "\u0C05",  # Vowel A
	"\xA5": "\u0C06",  # Vowel AA
	"\xA6": "\u0C07",  # Vowel I
	"\xA7": "\u0C08",  # Vowel II
	"\xA8": "\u0C09",  # Vowel U
	"\xA9": "\u0C0A",  # Vowel UU
	"\xAA": "\u0C0B",  # Vowel RI
	"\xAB": "\u0C0E",  # Vowel E
	"\xAC": "\u0C0F",  # Vowel EY
	"\xAD": "\u0C10",  # Vowel AI
	"\xAF": "\u0C12",  # Vowel O
	"\xB0": "\u0C13",  # Vowel OW
	"\xB1": "\u0C14",  # Vowel AU
	"\xB3": "\u0C15",  # Consonant KA
	"\xB4": "\u0C16",  # Consonant KHA
	"\xB5": "\u0C17",  # Consonant GA
	"\xB6": "\u0C18",  # Consonant GHA
	"\xB7": "\u0C19",  # Consonant NGA
	"\xB8": "\u0C1A",  # Consonant CHA
	"\xB9": "\u0C1B",  # Consonant CHHA
	"\xBA": "\u0C1C",  # Consonant JA
	"\xBB": "\u0C1D",  # Consonant JHA
	"\xBC": "\u0C1E",  # Consonant JNA
	"\xBD": "\u0C1F",  # Consonant Hard TA
	"\xBE": "\u0C20",  # Consonant Hard THA
	"\xBF": "\u0C21",  # Consonant Hard DA
	"\xC0": "\u0C22",  # Consonant Hard DHA
	"\xC1": "\u0C23",  # Consonant Hard NA
	"\xC2": "\u0C24",  # Consonant Soft TA
	"\xC3": "\u0C25",  # Consonant Soft THA
	"\xC4": "\u0C26",  # Consonant Soft DA
	"\xC5": "\u0C27",  # Consonant Soft DHA
	"\xC6": "\u0C28",  # Consonant Soft NA
	"\xC8": "\u0C2A",  # Consonant PA
	"\xC9": "\u0C2B",  # Consonant PHA
	"\xCA": "\u0C2C",  # Consonant BA
	"\xCB": "\u0C2D",  # Consonant BHA
	"\xCC": "\u0C2E",  # Consonant MA
	"\xCD": "\u0C2F",  # Consonant YA
	"\xCF": "\u0C30",  # Consonant RA
	"\xD0": "\u0C31",  # Consonant Hard RA (Southern Script)
	"\xD1": "\u0C32",  # Consonant LA
	"\xD2": "\u0C33",  # Consonant Hard LA
	"\xD4": "\u0C35",  # Consonant VA
	"\xD5": "\u0C36",  # Consonant SHA
	"\xD6": "\u0C37",  # Consonant Hard SHA
	"\xD7": "\u0C38",  # Consonant SA
	"\xD8": "\u0C39",  # Consonant HA
	"\xDA": "\u0C3E",  # Vowel Sign AA
	"\xDB": "\u0C3F",  # Vowel Sign I
	"\xDC": "\u0C40",  # Vowel Sign II
	"\xDD": "\u0C41",  # Vowel Sign U
	"\xDE": "\u0C42",  # Vowel Sign UU
	"\xDF": "\u0C43",  # Vowel Sign RI
	"\xE0": "\u0C46",  # Vowel Sign E (Southern Scripts)
	"\xE1": "\u0C47",  # Vowel Sign EY
	"\xE2": "\u0C48",  # Vowel Sign AI
	"\xE4": "\u0C4A",  # Vowel Sign O
	"\xE5": "\u0C4B",  # Vowel Sign OW
	"\xE6": "\u0C4C",  # Vowel Sign AU
	"\xE8": "\u0C4D",  # Vowel Omission Sign (Halant)
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0C66",  # Digit 0
	"\xF2": "\u0C67",  # Digit 1
	"\xF3": "\u0C68",  # Digit 2
	"\xF4": "\u0C69",  # Digit 3
	"\xF5": "\u0C6A",  # Digit 4
	"\xF6": "\u0C6B",  # Digit 5
	"\xF7": "\u0C6C",  # Digit 6
	"\xF8": "\u0C6D",  # Digit 7
	"\xF9": "\u0C6E",  # Digit 8
	"\xFA": "\u0C6F",  # Digit 9
}
INDICTRANS_HASHP_I2U = {
	"\xA1": "\u0A70",  # Vowel-modifier GURMUKHI TIPPI
	"\xA2": "\u0A02",  # Vowel-modifier ANUSWAR
	"\xA3": "\u0A03",  # Vowel-modifier VISARG
	"\xA4": "\u0A05",  # Vowel A
	"\xA5": "\u0A06",  # Vowel AA
	"\xA6": "\u0A07",  # Vowel I
	"\xA7": "\u0A08",  # Vowel II
	"\xA8": "\u0A09",  # Vowel U
	"\xA9": "\u0A0A",  # Vowel UU
	"\xAA": "\u0A0B",  # Vowel RI
	"\xAB": "\u0A0E",  # Vowel E
	"\xAC": "\u0A0F",  # Vowel EY
	"\xAD": "\u0A10",  # Vowel AI
	# "\xB2": "\u0A0D",  # Vowel AYE (Devanagari Script)  #FIXME
	"\xAF": "\u0A12",  # Vowel O
	"\xB0": "\u0A13",  # Vowel OW
	"\xB1": "\u0A14",  # Vowel AU
	"\xB2": "\u0A11",  # Vowel AWE
	"\xB3": "\u0A15",  # Consonant KA
	"\xB4": "\u0A16",  # Consonant KHA
	"\xB5": "\u0A17",  # Consonant GA
	"\xB6": "\u0A18",  # Consonant GHA
	"\xB7": "\u0A19",  # Consonant NGA
	"\xB8": "\u0A1A",  # Consonant CHA
	"\xB9": "\u0A1B",  # Consonant CHHA
	"\xBA": "\u0A1C",  # Consonant JA
	"\xBB": "\u0A1D",  # Consonant JHA
	"\xBC": "\u0A1E",  # Consonant JNA
	"\xBD": "\u0A1F",  # Consonant Hard TA
	"\xBE": "\u0A20",  # Consonant Hard THA
	"\xBF": "\u0A21",  # Consonant Hard DA
	"\xC0": "\u0A22",  # Consonant Hard DHA
	"\xC1": "\u0A23",  # Consonant Hard NA
	"\xC2": "\u0A24",  # Consonant Soft TA
	"\xC3": "\u0A25",  # Consonant Soft THA
	"\xC4": "\u0A26",  # Consonant Soft DA
	"\xC5": "\u0A27",  # Consonant Soft DHA
	"\xC6": "\u0A28",  # Consonant Soft NA
	"\xC7": "\u0A29",  # Consonant NA (Tamil)
	"\xC8": "\u0A2A",  # Consonant PA
	"\xC9": "\u0A2B",  # Consonant PHA
	"\xCA": "\u0A2C",  # Consonant BA
	"\xCB": "\u0A2D",  # Consonant BHA
	"\xCC": "\u0A2E",  # Consonant MA
	"\xCD": "\u0A2F",  # Consonant YA
	"\xCF": "\u0A30",  # Consonant RA
	"\xD0": "\u0A31",  # Consonant Hard RA (Southern Script)
	"\xD1": "\u0A32",  # Consonant LA
	"\xD2": "\u0A33",  # Consonant Hard LA
	"\xD3": "\u0A34",  # Consonant ZHA (Tamil & Malyalam)
	"\xD4": "\u0A35",  # Consonant VA
	"\xD5": "\u0A36",  # Consonant SHA
	"\xD6": "\u0A37",  # Consonant Hard SHA
	"\xD7": "\u0A38",  # Consonant SA
	"\xD8": "\u0A39",  # Consonant HA
	"\xDA": "\u0A3E",  # Vowel Sign AA
	"\xDB": "\u0A3F",  # Vowel Sign I
	"\xDC": "\u0A40",  # Vowel Sign II
	"\xDD": "\u0A41",  # Vowel Sign U
	"\xDE": "\u0A42",  # Vowel Sign UU
	"\xDF": "\u0A43",  # Vowel Sign RI
	"\xE0": "\u0A46",  # Vowel Sign E (Southern Scripts)
	"\xE1": "\u0A47",  # Vowel Sign EY
	"\xE2": "\u0A48",  # Vowel Sign AI
	"\xE3": "\u0A45",  # Vowel Sign AYE (Devanagari Script)
	"\xE4": "\u0A4A",  # Vowel Sign O
	"\xE5": "\u0A4B",  # Vowel Sign OW
	"\xE6": "\u0A4C",  # Vowel Sign AU
	"\xE7": "\u0A49",  # Vowel Sign AWE (Devanagari Script)
	"\xE8": "\u0A4D",  # Vowel Omission Sign (Halant)
	"\xE9": "\u0A3C",  # Diacritic Sign (Nukta)
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0A66",  # Digit 0
	"\xF2": "\u0A67",  # Digit 1
	"\xF3": "\u0A68",  # Digit 2
	"\xF4": "\u0A69",  # Digit 3
	"\xF5": "\u0A6A",  # Digit 4
	"\xF6": "\u0A6B",  # Digit 5
	"\xF7": "\u0A6C",  # Digit 6
	"\xF8": "\u0A6D",  # Digit 7
	"\xF9": "\u0A6E",  # Digit 8
	"\xFA": "\u0A6F",  # Digit 9
	"\xFB": "\u0A71"  # GURMUKHI ADDAK
}
INDICTRANS_HASHK_I2U = {
	"\xA2": "\u0C82",
	"\xA3": "\u0C83",
	"\xA4": "\u0C85",
	"\xA5": "\u0C86",
	"\xA6": "\u0C87",
	"\xA7": "\u0C88",
	"\xA8": "\u0C89",
	"\xA9": "\u0C8A",
	"\xAA": "\u0C8B",
	"\xAE": "\u0C8D",
	"\xAB": "\u0C8E",
	"\xAC": "\u0C8F",
	"\xAD": "\u0C90",
	"\xB2": "\u0C91",
	"\xAF": "\u0C92",
	"\xB0": "\u0C93",
	"\xB1": "\u0C94",
	"\xB3": "\u0C95",
	"\xB4": "\u0C96",
	"\xB5": "\u0C97",
	"\xB6": "\u0C98",
	"\xB7": "\u0C99",
	"\xB8": "\u0C9A",
	"\xB9": "\u0C9B",
	"\xBA": "\u0C9C",
	"\xBB": "\u0C9D",
	"\xBC": "\u0C9E",
	"\xBD": "\u0C9F",
	"\xBE": "\u0CA0",
	"\xBF": "\u0CA1",
	"\xC0": "\u0CA2",
	"\xC1": "\u0CA3",
	"\xC2": "\u0CA4",
	"\xC3": "\u0CA5",
	"\xC4": "\u0CA6",
	"\xC5": "\u0CA7",
	"\xC6": "\u0CA8",
	"\xC7": "\u0CA9",
	"\xC8": "\u0CAA",
	"\xC9": "\u0CAB",
	"\xCA": "\u0CAC",
	"\xCB": "\u0CAD",
	"\xCC": "\u0CAE",
	"\xCD": "\u0CAF",
	"\xCF": "\u0CB0",
	"\xD0": "\u0CB1",
	"\xD1": "\u0CB2",
	"\xD2": "\u0CB3",
	"\xD3": "\u0CB4",
	"\xD4": "\u0CB5",
	"\xD5": "\u0CB6",
	"\xD6": "\u0CB7",
	"\xD7": "\u0CB8",
	"\xD8": "\u0CB9",
	"\xE9": "\u0CBC",
	"\xDA": "\u0CBE",
	"\xDB": "\u0CBF",
	"\xDC": "\u0CC0",
	"\xDD": "\u0CC1",
	"\xDE": "\u0CC2",
	"\xDF": "\u0CC3",
	"\xE0": "\u0CC6",
	"\xE1": "\u0CC7",
	"\xE2": "\u0CC8",
	"\xE7": "\u0CC9",
	"\xE4": "\u0CCA",
	"\xE5": "\u0CCB",
	"\xE6": "\u0CCC",
	"\xE8": "\u0CCD",
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0CE6",
	"\xF2": "\u0CE7",
	"\xF3": "\u0CE8",
	"\xF4": "\u0CE9",
	"\xF5": "\u0CEA",
	"\xF6": "\u0CEB",
	"\xF7": "\u0CEC",
	"\xF8": "\u0CED",
	"\xF9": "\u0CEE",
	"\xFA": "\u0CEF"
}
INDICTRANS_HASHM_I2U = {
	"\xA2": "\u0D02",  # Vowel-modifier ANUSWAR
	"\xA3": "\u0D03",  # Vowel-modifier VISARG
	"\xA4": "\u0D05",  # Vowel A
	"\xA5": "\u0D06",  # Vowel AA
	"\xA6": "\u0D07",  # Vowel I
	"\xA7": "\u0D08",  # Vowel II
	"\xA8": "\u0D09",  # Vowel U
	"\xA9": "\u0D0A",  # Vowel UU
	"\xAA": "\u0D0B",  # Vowel RI
	"\xAB": "\u0D0E",  # Vowel E
	"\xAC": "\u0D0F",  # Vowel EY
	"\xAD": "\u0D10",  # Vowel AI
	"\xAF": "\u0D12",  # Vowel O
	"\xB0": "\u0D13",  # Vowel OW
	"\xB1": "\u0D14",  # Vowel AU
	"\xB2": "\u0D11",  # Vowel AWE
	"\xB3": "\u0D15",  # Consonant KA
	"\xB4": "\u0D16",  # Consonant KHA
	"\xB5": "\u0D17",  # Consonant GA
	"\xB6": "\u0D18",  # Consonant GHA
	"\xB7": "\u0D19",  # Consonant NGA
	"\xB8": "\u0D1A",  # Consonant CHA
	"\xB9": "\u0D1B",  # Consonant CHHA
	"\xBA": "\u0D1C",  # Consonant JA
	"\xBB": "\u0D1D",  # Consonant JHA
	"\xBC": "\u0D1E",  # Consonant JNA
	"\xBD": "\u0D1F",  # Consonant Hard TA
	"\xBE": "\u0D20",  # Consonant Hard THA
	"\xBF": "\u0D21",  # Consonant Hard DA
	"\xC0": "\u0D22",  # Consonant Hard DHA
	"\xC1": "\u0D23",  # Consonant Hard NA
	"\xC2": "\u0D24",  # Consonant Soft TA
	"\xC3": "\u0D25",  # Consonant Soft THA
	"\xC4": "\u0D26",  # Consonant Soft DA
	"\xC5": "\u0D27",  # Consonant Soft DHA
	"\xC6": "\u0D28",  # Consonant Soft NA
	"\xC7": "\u0D29",  # Consonant NA (Tamil)
	"\xC8": "\u0D2A",  # Consonant PA
	"\xC9": "\u0D2B",  # Consonant PHA
	"\xCA": "\u0D2C",  # Consonant BA
	"\xCB": "\u0D2D",  # Consonant BHA
	"\xCC": "\u0D2E",  # Consonant MA
	"\xCD": "\u0D2F",  # Consonant YA
	"\xCF": "\u0D30",  # Consonant RA
	"\xD0": "\u0D31",  # Consonant Hard RA (Southern Script)
	"\xD1": "\u0D32",  # Consonant LA
	"\xD2": "\u0D33",  # Consonant Hard LA
	"\xD3": "\u0D34",  # Consonant ZHA (Tamil & Malyalam)
	"\xD4": "\u0D35",  # Consonant VA
	"\xD5": "\u0D36",  # Consonant SHA
	"\xD6": "\u0D37",  # Consonant Hard SHA
	"\xD7": "\u0D38",  # Consonant SA
	"\xD8": "\u0D39",  # Consonant HA
	"\xDA": "\u0D3E",  # Vowel Sign AA
	"\xDB": "\u0D3F",  # Vowel Sign I
	"\xDC": "\u0D40",  # Vowel Sign II
	"\xDD": "\u0D41",  # Vowel Sign U
	"\xDE": "\u0D42",  # Vowel Sign UU
	"\xDF": "\u0D43",  # Vowel Sign RI
	"\xE0": "\u0D46",  # Vowel Sign E (Southern Scripts)
	"\xE1": "\u0D47",  # Vowel Sign EY
	"\xE2": "\u0D48",  # Vowel Sign AI
	"\xE4": "\u0D4A",  # Vowel Sign O
	"\xE5": "\u0D4B",  # Vowel Sign OW
	"\xE6": "\u0D4C",  # Vowel Sign AU
	"\xE8": "\u0D4D",  # Vowel Omission Sign (Halant)
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0D66",  # Digit 0
	"\xF2": "\u0D67",  # Digit 1
	"\xF3": "\u0D68",  # Digit 2
	"\xF4": "\u0D69",  # Digit 3
	"\xF5": "\u0D6A",  # Digit 4
	"\xF6": "\u0D6B",  # Digit 5
	"\xF7": "\u0D6C",  # Digit 6
	"\xF8": "\u0D6D",  # Digit 7
	"\xF9": "\u0D6E",  # Digit 8
	"\xFA": "\u0D6F",  # Digit 9
}
INDICTRANS_HASHB_I2U = {
	"\xA1": "\u0981",
	"\xA2": "\u0982",  # Vowel-modifier ANUSWAR
	"\xA3": "\u0983",  # Vowel-modifier VISARG
	"\xA4": "\u0985",  # Vowel A
	"\xA5": "\u0986",  # Vowel AA
	"\xA6": "\u0987",  # Vowel I
	"\xA7": "\u0988",  # Vowel II
	"\xA8": "\u0989",  # Vowel U
	"\xA9": "\u098A",  # Vowel UU
	"\xAA": "\u098B",  # Vowel RI
	"\xAB": "\u098F",  # Vowel
	"\xAD": "\u0990",  # Vowel AI
	"\xAF": "\u0993",  # Vowel O
	"\xB1": "\u0994",  # Vowel AU
	"\xB3": "\u0995",  # Consonant KA
	"\xB4": "\u0996",  # Consonant KHA
	"\xB5": "\u0997",  # Consonant GA
	"\xB6": "\u0998",  # Consonant GHA
	"\xB7": "\u0999",  # Consonant NGA
	"\xB8": "\u099A",  # Consonant CHA
	"\xB9": "\u099B",  # Consonant CHHA
	"\xBA": "\u099C",  # Consonant JA
	"\xBB": "\u099D",  # Consonant JHA
	"\xBC": "\u099E",  # Consonant JNA
	"\xBD": "\u099F",  # Consonant Hard TA
	"\xBE": "\u09A0",  # Consonant Hard THA
	"\xBF": "\u09A1",  # Consonant Hard DA
	"\xC0": "\u09A2",  # Consonant Hard DHA
	"\xC1": "\u09A3",  # Consonant Hard NA
	"\xC2": "\u09A4",  # Consonant Soft TA
	"\xC3": "\u09A5",  # Consonant Soft THA
	"\xC4": "\u09A6",  # Consonant Soft DA
	"\xC5": "\u09A7",  # Consonant Soft DHA
	"\xC6": "\u09A8",  # Consonant Soft NA
	"\xC8": "\u09AA",  # Consonant PA
	"\xC9": "\u09AB",  # Consonant PHA
	"\xCA": "\u09AC",  # Consonant BA
	"\xCB": "\u09AD",  # Consonant BHA
	"\xCC": "\u09AE",  # Consonant MA
	"\xCD": "\u09AF",  # Consonant YA
	"\xCF": "\u09B0",  # Consonant RA
	"\xD1": "\u09B2",  # Consonant LA
	"\xD5": "\u09B6",  # Consonant SHA
	"\xD6": "\u09B7",  # Consonant Hard SHA
	"\xD7": "\u09B8",  # Consonant SA
	"\xD8": "\u09B9",  # Consonant HA
	"\xDA": "\u09BE",  # Vowel Sign AA
	"\xDB": "\u09BF",  # Vowel Sign I
	"\xDC": "\u09C0",  # Vowel Sign II
	"\xDD": "\u09C1",  # Vowel Sign U
	"\xDE": "\u09C2",  # Vowel Sign UU
	"\xDF": "\u09C3",  # Vowel Sign RI
	"\xE0": "\u09C7",  # Vowel Sign E (Southern Scripts)
	"\xE2": "\u09C8",  # Vowel Sign AI
	"\xE4": "\u09CB",  # Vowel Sign O
	"\xE6": "\u09CC",  # Vowel Sign AU
	"\xE8": "\u09CD",  # Vowel Omission Sign (Halant)
	"\xE9": "\u09BC",
	"\xEA": ".",  # Fullstop
	"\xF1": "\u09E6",  # Digit 0
	"\xF2": "\u09E7",  # Digit 1
	"\xF3": "\u09E8",  # Digit 2
	"\xF4": "\u09E9",  # Digit 3
	"\xF5": "\u09EA",  # Digit 4
	"\xF6": "\u09EB",  # Digit 5
	"\xF7": "\u09EC",  # Digit 6
	"\xF8": "\u09ED",  # Digit 7
	"\xF9": "\u09EE",  # Digit 8
	"\xFA": "\u09EF",  # Digit 9
}
INDICTRANS_HASHCTA_I2U = {
	"\xA2": "\u0BAE\u0BCD",  # Vowel-modifier ANUSWAR is m + halant
	"\xA3": "\u0B83",  # Vowel-modifier VISARG
	"\xA4": "\u0B85",  # Vowel A
	"\xA5": "\u0B86",  # Vowel AA
	"\xA6": "\u0B87",  # Vowel I
	"\xA7": "\u0B88",  # Vowel II
	"\xA8": "\u0B89",  # Vowel U
	"\xA9": "\u0B8A",  # Vowel UU
	"\xAB": "\u0B8E",  # Vowel
	"\xAC": "\u0B8F",
	"\xAD": "\u0B90",  # Vowel AI
	"\xAF": "\u0B92",  # Vowel O
	"\xB0": "\u0B93",  # Vowel OW
	"\xB1": "\u0B94",  # Vowel AU
	"\xB3": "\u0B95",  # Consonant KA
	"\xB7": "\u0B99",  # Consonant NGA
	"\xB8": "\u0B9A",  # Consonant CHA
	"\xBA": "\u0B9C",  # Consonant JA
	"\xBC": "\u0B9E",  # Consonant JNA
	"\xBD": "\u0B9F",  # Consonant Hard TA
	"\xC1": "\u0BA3",  # Consonant Hard NA
	"\xC2": "\u0BA4",  # Consonant Soft TA
	"\xC6": "\u0BA8",  # Consonant Soft NA
	"\xC7": "\u0BA9",  # Consonant NA (Tamil)
	"\xC8": "\u0BAA",  # Consonant PA
	"\xCC": "\u0BAE",  # Consonant MA
	"\xCD": "\u0BAF",  # Consonant YA
	"\xCF": "\u0BB0",  # Consonant RA
	"\xD0": "\u0BB1",
	"\xD1": "\u0BB2",  # Consonant LA
	"\xD2": "\u0BB3",  # Consonant Hard LA
	"\xD3": "\u0BB4",  # Consonant ZHA (Tamil & Malyalam)
	"\xD4": "\u0BB5",  # Consonant VA
	"\xD5": "\u0BB7",  # Consonant SHA is nomore use in tamil
	"\xD6": "\u0BB7",  # Consonant Hard SHA
	"\xD7": "\u0BB8",  # Consonant SA
	"\xD8": "\u0BB9",  # Consonant HA
	"\xDA": "\u0BBE",  # Vowel Sign AA
	"\xDB": "\u0BBF",  # Vowel Sign I
	"\xDC": "\u0BC0",  # Vowel Sign II
	"\xDD": "\u0BC1",  # Vowel Sign U
	"\xDE": "\u0BC2",  # Vowel Sign UU
	"\xE0": "\u0BC6",  # Vowel Sign E (Southern Scripts)
	"\xE1": "\u0BC7",  # Vowel Sign EY
	"\xE2": "\u0BC8",  # Vowel Sign AI
	"\xE4": "\u0BCA",  # Vowel Sign O
	"\xE5": "\u0BCB",  # Vowel Sign OW
	"\xE6": "\u0BCC",  # Vowel Sign AU
	"\xE8": "\u0BCD",  # Vowel Omission Sign (Halant)
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0BE6",  # Digit 0
	"\xF2": "\u0BE7",  # Digit 1
	"\xF3": "\u0BE8",  # Digit 2
	"\xF4": "\u0BE9",  # Digit 3
	"\xF5": "\u0BEA",  # Digit 4
	"\xF6": "\u0BEB",  # Digit 5
	"\xF7": "\u0BEC",  # Digit 6
	"\xF8": "\u0BED",  # Digit 7
	"\xF9": "\u0BEE",  # Digit 8
	"\xFA": "\u0BEF",  # Digit 9
}
INDICTRANS_HASHO_I2U = {
	"\xA1": "\u0B01",  # Vowel-modifier CHANDRABINDU
	"\xA2": "\u0B02",  # Vowel-modifier ANUSWAR
	"\xA3": "\u0B03",  # Vowel-modifier VISARG
	"\xA4": "\u0B05",  # Vowel A
	"\xA5": "\u0B06",  # Vowel AA
	"\xA6": "\u0B07",  # Vowel I
	"\xA7": "\u0B08",  # Vowel II
	"\xA8": "\u0B09",  # Vowel U
	"\xA9": "\u0B0A",  # Vowel UU
	"\xAA": "\u0B0B",  # Vowel RI
	"\xAC": "\u0B0F",  # Vowel EY
	"\xAD": "\u0B10",  # Vowel AI
	"\xB0": "\u0B13",  # Vowel OW
	"\xB1": "\u0B14",  # Vowel AU
	"\xB3": "\u0B15",  # Consonant KA
	"\xB4": "\u0B16",  # Consonant KHA
	"\xB5": "\u0B17",  # Consonant GA
	"\xB6": "\u0B18",  # Consonant GHA
	"\xB7": "\u0B19",  # Consonant NGA
	"\xB8": "\u0B1A",  # Consonant CHA
	"\xB9": "\u0B1B",  # Consonant CHHA
	"\xBA": "\u0B1C",  # Consonant JA
	"\xBB": "\u0B1D",  # Consonant JHA
	"\xBC": "\u0B1E",  # Consonant JNA
	"\xBD": "\u0B1F",  # Consonant Hard TA
	"\xBE": "\u0B20",  # Consonant Hard THA
	"\xBF": "\u0B21",  # Consonant Hard DA
	"\xC0": "\u0B22",  # Consonant Hard DHA
	"\xC1": "\u0B23",  # Consonant Hard NA
	"\xC2": "\u0B24",  # Consonant Soft TA
	"\xC3": "\u0B25",  # Consonant Soft THA
	"\xC4": "\u0B26",  # Consonant Soft DA
	"\xC5": "\u0B27",  # Consonant Soft DHA
	"\xC6": "\u0B28",  # Consonant Soft NA
	"\xC8": "\u0B2A",  # Consonant PA
	"\xC9": "\u0B2B",  # Consonant PHA
	"\xCA": "\u0B2C",  # Consonant BA
	"\xCB": "\u0B2D",  # Consonant BHA
	"\xCC": "\u0B2E",  # Consonant MA
	"\xCD": "\u0B2F",  # Consonant YA
	"\xCF": "\u0B30",  # Consonant RA
	"\xD1": "\u0B32",  # Consonant LA
	"\xD2": "\u0B33",  # Consonant Hard LA
	"\xD4": "\u0B35",  # Consonant VA
	"\xD5": "\u0B36",  # Consonant SHA
	"\xD6": "\u0B37",  # Consonant Hard SHA
	"\xD7": "\u0B38",  # Consonant SA
	"\xD8": "\u0B39",  # Consonant HA
	"\xDA": "\u0B3E",  # Vowel Sign AA
	"\xDB": "\u0B3F",  # Vowel Sign I
	"\xDC": "\u0B40",  # Vowel Sign II
	"\xDD": "\u0B41",  # Vowel Sign U
	"\xDE": "\u0B42",  # Vowel Sign UU
	"\xDF": "\u0B43",  # Vowel Sign RI
	"\xE1": "\u0B47",  # Vowel Sign EY
	"\xE2": "\u0B48",  # Vowel Sign AI
	"\xE5": "\u0B4B",  # Vowel Sign OW
	"\xE6": "\u0B4C",  # Vowel Sign AU
	"\xE8": "\u0B4D",  # Vowel Omission Sign (Halant)
	"\xE9": "\u0B3C",  # Diacritic Sign (Nukta)
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0B66",  # Digit 0
	"\xF2": "\u0B67",  # Digit 1
	"\xF3": "\u0B68",  # Digit 2
	"\xF4": "\u0B69",  # Digit 3
	"\xF5": "\u0B6A",  # Digit 4
	"\xF6": "\u0B6B",  # Digit 5
	"\xF7": "\u0B6C",  # Digit 6
	"\xF8": "\u0B6D",  # Digit 7
	"\xF9": "\u0B6E",  # Digit 8
	"\xFA": "\u0B6F",  # Digit 9
}
INDICTRANS_HASHG_I2U = {
	"\xA1": "\u0A81",  # Vowel-modifier CHANDRABINDU
	"\xA2": "\u0A82",  # Vowel-modifier ANUSWAR
	"\xA3": "\u0A83",  # Vowel-modifier VISARG
	"\xA4": "\u0A85",  # Vowel A
	"\xA5": "\u0A86",  # Vowel AA
	"\xA6": "\u0A87",  # Vowel I
	"\xA7": "\u0A88",  # Vowel II
	"\xA8": "\u0A89",  # Vowel U
	"\xA9": "\u0A8A",  # Vowel UU
	"\xAA": "\u0A8B",  # Vowel RI
	"\xAE": "\u0A8D",  # Vowel AI -Rashid added
	# "\xB2": "\u0A8D",  # Vowel AYE (Devanagari Script) #FIXME
	"\xAC": "\u0A8F",  # Vowel EY
	"\xAD": "\u0A90",  # Vowel AI
	"\xB0": "\u0A93",  # Vowel OW
	"\xB1": "\u0A94",  # Vowel AU
	"\xB2": "\u0A91",  # Vowel AWE
	"\xB3": "\u0A95",  # Consonant KA
	"\xB4": "\u0A96",  # Consonant KHA
	"\xB5": "\u0A97",  # Consonant GA
	"\xB6": "\u0A98",  # Consonant GHA
	"\xB7": "\u0A99",  # Consonant NGA
	"\xB8": "\u0A9A",  # Consonant CHA
	"\xB9": "\u0A9B",  # Consonant CHHA
	"\xBA": "\u0A9C",  # Consonant JA
	"\xBB": "\u0A9D",  # Consonant JHA
	"\xBC": "\u0A9E",  # Consonant JNA
	"\xBD": "\u0A9F",  # Consonant Hard TA
	"\xBE": "\u0AA0",  # Consonant Hard THA
	"\xBF": "\u0AA1",  # Consonant Hard DA
	"\xC0": "\u0AA2",  # Consonant Hard DHA
	"\xC1": "\u0AA3",  # Consonant Hard NA
	"\xC2": "\u0AA4",  # Consonant Soft TA
	"\xC3": "\u0AA5",  # Consonant Soft THA
	"\xC4": "\u0AA6",  # Consonant Soft DA
	"\xC5": "\u0AA7",  # Consonant Soft DHA
	"\xC6": "\u0AA8",  # Consonant Soft NA
	"\xC8": "\u0AAA",  # Consonant PA
	"\xC9": "\u0AAB",  # Consonant PHA
	"\xCA": "\u0AAC",  # Consonant BA
	"\xCB": "\u0AAD",  # Consonant BHA
	"\xCC": "\u0AAE",  # Consonant MA
	"\xCD": "\u0AAF",  # Consonant YA
	"\xCF": "\u0AB0",  # Consonant RA
	"\xD1": "\u0AB2",  # Consonant LA
	"\xD2": "\u0AB3",  # Consonant Hard LA
	"\xD4": "\u0AB5",  # Consonant VA
	"\xD5": "\u0AB6",  # Consonant SHA
	"\xD6": "\u0AB7",  # Consonant Hard SHA
	"\xD7": "\u0AB8",  # Consonant SA
	"\xD8": "\u0AB9",  # Consonant HA
	"\xE9": "\u0ABC",  # Diacritic Sign (Nukta)
	"\xDA": "\u0ABE",  # Vowel Sign AA
	"\xDB": "\u0ABF",  # Vowel Sign I
	"\xDC": "\u0AC0",  # Vowel Sign II
	"\xDD": "\u0AC1",  # Vowel Sign U
	"\xDE": "\u0AC2",  # Vowel Sign UU
	"\xDF": "\u0AC3",  # Vowel Sign RI
	"\xE1": "\u0AC7",  # Vowel Sign EY
	"\xE2": "\u0AC8",  # Vowel Sign AI
	"\xE3": "\u0AC5",  # Vowel Sign AYE (Devanagari Script)
	"\xE5": "\u0ACB",  # Vowel Sign OW
	"\xE6": "\u0ACC",  # Vowel Sign AU
	"\xE7": "\u0AC9",  # Vowel Sign AWE (Devanagari Script)
	"\xE8": "\u0ACD",  # Vowel Omission Sign (Halant)
	"\xEA": ".",  # Fullstop
	"\xF1": "\u0AE6",  # Digit 0
	"\xF2": "\u0AE7",  # Digit 1
	"\xF3": "\u0AE8",  # Digit 2
	"\xF4": "\u0AE9",  # Digit 3
	"\xF5": "\u0AEA",  # Digit 4
	"\xF6": "\u0AEB",  # Digit 5
	"\xF7": "\u0AEC",  # Digit 6
	"\xF8": "\u0AED",  # Digit 7
	"\xF9": "\u0AEE",  # Digit 8
	"\xFA": "\u0AEF",  # Digit 9
}

## second set

INDICTRANS_HASHC_I2W = {
	"\xB3": "k",
	"\xB4": "K",
	"\xB5": "g",
	"\xB6": "G",
	"\xB7": "f",
	"\xB8": "c",
	"\xB9": "C",
	"\xBA": "j",
	"\xBB": "J",
	"\xBC": "F",
	"\xBD": "t",
	"\xBE": "T",
	"\xBF": "d",
	"\xC0": "D",
	"\xC1": "N",
	"\xC2": "w",
	"\xC3": "W",
	"\xC4": "x",
	"\xC5": "X",
	"\xC6": "n",
	"\xC7": "nY",
	"\xC8": "p",
	"\xC9": "P",
	"\xCA": "b",
	"\xCB": "B",
	"\xCC": "m",
	"\xCD": "y",
	"\xCF": "r",
	# Representation for Consonant HARD RA (Southern Script)
	"\xD0": "rY",
	"\xD1": "l",
	"\xD2": "lY",
	# Representation for Consonant ZHA (Tamil & Malyalam)
	"\xD3": "lYY",
	"\xD4": "v",
	"\xD5": "S",
	"\xD6": "R",
	"\xD7": "s",
	"\xD8": "h",
	"\xE9": "Z",  # NUKTA
}
INDICTRANS_HASHV_I2W = {
	"\xA4": "a",
	"\xA5": "A",
	"\xA6": "i",
	"\xA7": "I",
	"\xA8": "u",
	"\xA9": "U",
	"\xAA": "q",
	"\xAB": "eV",
	"\xAC": "e",
	"\xAD": "E",
	"\xAE": "EY",
	"\xAF": "oV",
	"\xB0": "o",
	"\xB1": "O",
	"\xB2": "OY",
}
INDICTRANS_HASHM_I2W = {
	"\xDA": "A",
	"\xDB": "i",
	"\xDC": "I",
	"\xDD": "u",
	"\xDE": "U",
	"\xDF": "q",
	"\xE0": "eV",
	"\xE1": "e",
	"\xE2": "E",
	"\xE3": "EY",
	"\xE4": "oV",
	"\xE5": "o",
	"\xE6": "O",
	"\xE7": "OY",
}
INDICTRANS_HASHMD_I2W = {
	"\xA1": "z",
	"\xA2": "M",
	"\xA3": "H",
}
INDICTRANS_DIGITS_I2W = {
	"\xF1": "0",
	"\xF2": "1",
	"\xF3": "2",
	"\xF4": "3",
	"\xF5": "4",
	"\xF6": "5",
	"\xF7": "6",
	"\xF8": "7",
	"\xF9": "8",
	"\xFA": "9",
}
INDICTRANS_HASHH_U2I = {
	"\u0901": "\xA1",  # Vowel-modifier CHANDRABINDU
	"\u0902": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0903": "\xA3",  # Vowel-modifier VISARG
	"\u0905": "\xA4",  # Vowel A
	"\u0906": "\xA5",  # Vowel AA
	"\u0907": "\xA6",  # Vowel I
	"\u0908": "\xA7",  # Vowel II
	"\u0909": "\xA8",  # Vowel U
	"\u090A": "\xA9",  # Vowel UU
	"\u090B": "\xAA",  # Vowel RI
	"\u090D": "\xAE",
	"\u090E": "\xAB",
	"\u090F": "\xAC",
	"\u0910": "\xAD",
	"\u0911": "\xB2",
	"\u0912": "\xAF",
	"\u0913": "\xB0",
	"\u0914": "\xB1",
	"\u0915": "\xB3",  # Consonant KA
	"\u0916": "\xB4",  # Consonant
	"\u0917": "\xB5",  # Consonant
	"\u0918": "\xB6",  # Consonant
	"\u0919": "\xB7",  # Consonant NGA
	"\u091A": "\xB8",  # Consonant
	"\u091B": "\xB9",  # Consonant
	"\u091C": "\xBA",  # Consonant
	"\u091D": "\xBB",  # Consonant
	"\u091E": "\xBC",  # Consonant JNA
	"\u091F": "\xBD",  # Consonant
	"\u0920": "\xBE",  # Consonant
	"\u0921": "\xBF",  # Consonant
	"\u0922": "\xC0",  # Consonant
	"\u0923": "\xC1",  # Consonant NA
	"\u0924": "\xC2",  # Consonant
	"\u0925": "\xC3",  # Consonant
	"\u0926": "\xC4",  # Consonant
	"\u0927": "\xC5",  # Consonant
	"\u0928": "\xC6",  # Consonant NA
	"\u0929": "\xC7",  # Consonant NNNA
	"\u092A": "\xC8",  # Consonant PA
	"\u092B": "\xC9",  # Consonant PHA
	"\u092C": "\xCA",  # Consonant BA
	"\u092D": "\xCB",  # Consonant BHA
	"\u092E": "\xCC",  # Consonant MA
	"\u092F": "\xCD",  # Consonant YA
	"\u0930": "\xCF",  # Consonant RA
	"\u0931": "\xD0",  # Consonant RRA
	"\u0932": "\xD1",  # Consonant LA
	"\u0933": "\xD2",  # Consonant LLA
	"\u0934": "\xD3",  # Consonant LLLA
	"\u0935": "\xD4",  # Consonant VA
	"\u0936": "\xD5",  # Consonant SHA
	"\u0937": "\xD6",  # Consonant SSA
	"\u0938": "\xD7",  # Consonant SA
	"\u0939": "\xD8",  # Consonant HA
	"\u093C": "\xE9",  # Consonant NUKTA
	"\u093E": "\xDA",  # Vowel Sign AA
	"\u093F": "\xDB",  # Vowel Sign I
	"\u0940": "\xDC",  # Vowel Sign II
	"\u0941": "\xDD",  # Vowel Sign U
	"\u0942": "\xDE",  # Vowel
	"\u0943": "\xDF",  # Vowel
	"\u0946": "\xE0",  # Vowel
	"\u0947": "\xE1",  # Vowel
	"\u0948": "\xE2",  # Vowel
	"\u0949": "\xE7",  # Vowel
	"\u094A": "\xE4",  # Vowel
	"\u094B": "\xE5",  # Vowel
	"\u094C": "\xE6",  # Vowel
	"\u094D": "\xE8",  # Halant
	"\u0960": "\xAA",  # Vowel Sanskrit
	"\u0966": "\xF1",  # Devanagari Digit 0
	"\u0967": "\xF2",  # Devanagari Digit 1
	"\u0968": "\xF3",  # Devanagari Digit 2
	"\u0969": "\xF4",  # Devanagari Digit 3
	"\u096A": "\xF5",  # Devanagari Digit 4
	"\u096B": "\xF6",  # Devanagari Digit 5
	"\u096C": "\xF7",  # Devanagari Digit 6
	"\u096D": "\xF8",  # Devanagari Digit 7
	"\u096E": "\xF9",  # Devanagari Digit 8
	"\u096F": "\xFA",  # Devanagari Digit 9
}
INDICTRANS_UNICODE_NORM_HASHH_U2I = {
	"\u0958": "\u0915",
	"\u0959": "\u0916",
	"\u095A": "\u0917",
	"\u095B": "\u091C",
	"\u095C": "\u0921",
	"\u095D": "\u0922",
	"\u095E": "\u092B",
	"\u095F": "\u092F",
}
INDICTRANS_HASHT_U2I = {
	"\u0C01": "\xA1",
	"\u0C02": "\xA2",
	"\u0C03": "\xA3",
	"\u0C05": "\xA4",
	"\u0C06": "\xA5",
	"\u0C07": "\xA6",
	"\u0C08": "\xA7",
	"\u0C09": "\xA8",
	"\u0C0A": "\xA9",
	"\u0C0B": "\xAA",
	"\u0C0D": "\xAE",
	"\u0C0E": "\xAB",
	"\u0C0F": "\xAC",
	"\u0C10": "\xAD",
	"\u0C11": "\xB2",
	"\u0C12": "\xAF",
	"\u0C13": "\xB0",
	"\u0C14": "\xB1",
	"\u0C15": "\xB3",
	"\u0C16": "\xB4",
	"\u0C17": "\xB5",
	"\u0C18": "\xB6",
	"\u0C19": "\xB7",
	"\u0C1A": "\xB8",
	"\u0C1B": "\xB9",
	"\u0C1C": "\xBA",
	"\u0C1D": "\xBB",
	"\u0C1E": "\xBC",
	"\u0C1F": "\xBD",
	"\u0C20": "\xBE",
	"\u0C21": "\xBF",
	"\u0C22": "\xC0",
	"\u0C23": "\xC1",
	"\u0C24": "\xC2",
	"\u0C25": "\xC3",
	"\u0C26": "\xC4",
	"\u0C27": "\xC5",
	"\u0C28": "\xC6",
	"\u0C29": "\xC7",
	"\u0C2A": "\xC8",
	"\u0C2B": "\xC9",
	"\u0C2C": "\xCA",
	"\u0C2D": "\xCB",
	"\u0C2E": "\xCC",
	"\u0C2F": "\xCD",
	"\u0C30": "\xCF",
	"\u0C31": "\xD0",
	"\u0C32": "\xD1",
	"\u0C33": "\xD2",
	"\u0C34": "\xD3",
	"\u0C35": "\xD4",
	"\u0C36": "\xD5",
	"\u0C37": "\xD6",
	"\u0C38": "\xD7",
	"\u0C39": "\xD8",
	"\u0C3E": "\xDA",
	"\u0C3F": "\xDB",
	"\u0C40": "\xDC",
	"\u0C41": "\xDD",
	"\u0C42": "\xDE",
	"\u0C43": "\xDF",
	"\u0C46": "\xE0",
	"\u0C47": "\xE1",
	"\u0C48": "\xE2",
	"\u0C4A": "\xE4",
	"\u0C4B": "\xE5",
	"\u0C4C": "\xE6",
	"\u0C4D": "\xE8",
	"\u0C64": "\xEA",
	"\u0C65": "\xEA",  # ADDED
	"\u0C66": "\xF1",
	"\u0C67": "\xF2",
	"\u0C68": "\xF3",
	"\u0C69": "\xF4",
	"\u0C6A": "\xF5",
	"\u0C6B": "\xF6",
	"\u0C6C": "\xF7",
	"\u0C6D": "\xF8",
	"\u0C6E": "\xF9",
	"\u0C6F": "\xFA",
}
INDICTRANS_HASHP_U2I = {
	"\u0A01": "\xA1",  # Vowel-modifier CHANDRABINDU
	"\u0A02": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0A03": "\xA3",  # Vowel-modifier VISARG
	"\u0A05": "\xA4",  # Vowel A
	"\u0A06": "\xA5",  # Vowel AA
	"\u0A07": "\xA6",  # Vowel I
	"\u0A08": "\xA7",  # Vowel II
	"\u0A09": "\xA8",  # Vowel U
	"\u0A0A": "\xA9",  # Vowel UU
	"\u0A0B": "\xAA",  # Vowel RI
	"\u0A0D": "\xAE",
	"\u0A0E": "\xAB",
	"\u0A0F": "\xAC",
	"\u0A10": "\xAD",
	"\u0A11": "\xB2",
	"\u0A12": "\xAF",
	"\u0A13": "\xB0",
	"\u0A14": "\xB1",
	"\u0A15": "\xB3",  # Consonant KA
	"\u0A16": "\xB4",  # Consonant
	"\u0A17": "\xB5",  # Consonant
	"\u0A18": "\xB6",  # Consonant
	"\u0A19": "\xB7",  # Consonant NGA
	"\u0A1A": "\xB8",  # Consonant
	"\u0A1B": "\xB9",  # Consonant
	"\u0A1C": "\xBA",  # Consonant
	"\u0A1D": "\xBB",  # Consonant
	"\u0A1E": "\xBC",  # Consonant JNA
	"\u0A1F": "\xBD",  # Consonant
	"\u0A20": "\xBE",  # Consonant
	"\u0A21": "\xBF",  # Consonant
	"\u0A22": "\xC0",  # Consonant
	"\u0A23": "\xC1",  # Consonant NA
	"\u0A24": "\xC2",  # Consonant
	"\u0A25": "\xC3",  # Consonant
	"\u0A26": "\xC4",  # Consonant
	"\u0A27": "\xC5",  # Consonant
	"\u0A28": "\xC6",  # Consonant NA
	"\u0A29": "\xC7",  # Consonant NNNA
	"\u0A2A": "\xC8",  # Consonant PA
	"\u0A2B": "\xC9",  # Consonant PHA
	"\u0A2C": "\xCA",  # Consonant BA
	"\u0A2D": "\xCB",  # Consonant BHA
	"\u0A2E": "\xCC",  # Consonant MA
	"\u0A2F": "\xCD",  # Consonant YA
	"\u0A30": "\xCF",  # Consonant RA
	"\u0A31": "\xD0",  # Consonant RRA
	"\u0A32": "\xD1",  # Consonant LA
	"\u0A33": "\xD2",  # Consonant LLA
	"\u0A34": "\xD3",  # Consonant LLLA
	"\u0A35": "\xD4",  # Consonant VA
	"\u0A36": "\xD5",  # Consonant SHA
	"\u0A37": "\xD6",  # Consonant SSA
	"\u0A38": "\xD7",  # Consonant SA
	"\u0A39": "\xD8",  # Consonant HA
	"\u0A3C": "\xE9",  # Consonant NUKTA
	"\u0A3E": "\xDA",  # Vowel Sign AA
	"\u0A3F": "\xDB",  # Vowel Sign I
	"\u0A40": "\xDC",  # Vowel Sign II
	"\u0A41": "\xDD",  # Vowel Sign U
	"\u0A42": "\xDE",  # Vowel
	"\u0A43": "\xDF",  # Vowel
	"\u0A46": "\xE0",  # Vowel
	"\u0A47": "\xE1",  # Vowel
	"\u0A48": "\xE2",  # Vowel
	"\u0A49": "\xE7",  # Vowel
	"\u0A4A": "\xE4",  # Vowel
	"\u0A4B": "\xE5",  # Vowel
	"\u0A4C": "\xE6",  # Vowel
	"\u0A4D": "\xE8",  # Vowel Omission Sign Halant
	"\u0A5C": "\xE8",  # Vowel Omission Sign Halant
	"\u0A64": "\xEA",  # PURNA VIRAM Reserved
	"\u0A65": "\xEA",  # DEERGH VIRAM
	"\u0A66": "\xF1",  # Consonant
	"\u0A67": "\xF2",  # Consonant
	"\u0A68": "\xF3",  # Consonant
	"\u0A69": "\xF4",  # Consonant
	"\u0A6A": "\xF5",  # Consonant
	"\u0A6B": "\xF6",
	"\u0A6C": "\xF7",
	"\u0A6D": "\xF8",
	"\u0A6E": "\xF9",
	"\u0A6F": "\xFA",
	"\u0A70": "\xA1",  # Vowel-modifier GURMUKHI TIPPI
	"\u0A71": "\xFB",  # GURMUKHI ADDAK
}
INDICTRANS_UNICODE_NORM_HASHP_U2I = {
	"\u0A59": "\u0A16",
	"\u0A5A": "\u0A17",
	"\u0A5B": "\u0A1C",
	"\u0A5E": "\u0A2B",
}
INDICTRANS_HASHK_U2I = {
	"\u0C82": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0C83": "\xA3",  # Vowel-modifier VISARG
	"\u0C85": "\xA4",  # Vowel A
	"\u0C86": "\xA5",  # Vowel AA
	"\u0C87": "\xA6",  # Vowel I
	"\u0C88": "\xA7",  # Vowel II
	"\u0C89": "\xA8",  # Vowel U
	"\u0C8A": "\xA9",  # Vowel UU
	"\u0C8B": "\xAA",  # Vowel RI
	"\u0C8D": "\xAE",
	"\u0C8E": "\xAB",
	"\u0C8F": "\xAC",
	"\u0C90": "\xAD",
	"\u0C91": "\xB2",
	"\u0C92": "\xAF",
	"\u0C93": "\xB0",
	"\u0C94": "\xB1",
	"\u0C95": "\xB3",  # Consonant KA
	"\u0C96": "\xB4",  # Consonant
	"\u0C97": "\xB5",  # Consonant
	"\u0C98": "\xB6",  # Consonant
	"\u0C99": "\xB7",  # Consonant NGA
	"\u0C9A": "\xB8",  # Consonant
	"\u0C9B": "\xB9",  # Consonant
	"\u0C9C": "\xBA",  # Consonant
	"\u0C9D": "\xBB",  # Consonant
	"\u0C9E": "\xBC",  # Consonant JNA
	"\u0C9F": "\xBD",  # Consonant
	"\u0CA0": "\xBE",  # Consonant
	"\u0CA1": "\xBF",  # Consonant
	"\u0CA2": "\xC0",  # Consonant
	"\u0CA3": "\xC1",  # Consonant NA
	"\u0CA4": "\xC2",  # Consonant
	"\u0CA5": "\xC3",  # Consonant
	"\u0CA6": "\xC4",  # Consonant
	"\u0CA7": "\xC5",  # Consonant
	"\u0CA8": "\xC6",  # Consonant NA
	"\u0CA9": "\xC7",  # Consonant NNNA
	"\u0CAA": "\xC8",  # Consonant PA
	"\u0CAB": "\xC9",  # Consonant PHA
	"\u0CAC": "\xCA",  # Consonant BA
	"\u0CAD": "\xCB",  # Consonant BHA
	"\u0CAE": "\xCC",  # Consonant MA
	"\u0CAF": "\xCD",  # Consonant YA
	"\u0CB0": "\xCF",  # Consonant RA
	"\u0CB1": "\xD0",  # Consonant RRA
	"\u0CB2": "\xD1",  # Consonant LA
	"\u0CB3": "\xD2",  # Consonant LLA
	"\u0CB4": "\xD3",  # Consonant LLLA
	"\u0CB5": "\xD4",  # Consonant VA
	"\u0CB6": "\xD5",  # Consonant SHA
	"\u0CB7": "\xD6",  # Consonant SSA
	"\u0CB8": "\xD7",  # Consonant SA
	"\u0CB9": "\xD8",  # Consonant HA
	"\u0CBC": "\xE9",  # Consonant NUKTA
	"\u0CBE": "\xDA",  # Vowel Sign AA
	"\u0CBF": "\xDB",  # Vowel Sign I
	"\u0CC0": "\xDC",  # Vowel Sign II
	"\u0CC1": "\xDD",  # Vowel Sign U
	"\u0CC2": "\xDE",  # Vowel
	"\u0CC3": "\xDF",  # Vowel
	"\u0CC6": "\xE0",  # Vowel
	"\u0CC7": "\xE1",  # Vowel
	"\u0CC8": "\xE2",  # Vowel
	"\u0CC9": "\xE7",  # Vowel
	"\u0CCA": "\xE4",  # Vowel
	"\u0CCB": "\xE5",  # Vowel
	"\u0CCC": "\xE6",  # Vowel
	"\u0CCD": "\xE8",  # Consonant
	"\u0CE4": "\xEA",  # PURNA VIRAM Reserved
	"\u0CE5": "\xEA",  # DEERGH VIRAM
	"\u0CE6": "\xF1",  # Consonant
	"\u0CE7": "\xF2",  # Consonant
	"\u0CE8": "\xF3",  # Consonant
	"\u0CE9": "\xF4",  # Consonant
	"\u0CEA": "\xF5",  # Consonant
	"\u0CEB": "\xF6",
	"\u0CEC": "\xF7",
	"\u0CED": "\xF8",
	"\u0CEE": "\xF9",
	"\u0CEF": "\xFA",
}
INDICTRANS_HASHM_U2I = {
	"\u0D02": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0D03": "\xA3",  # Vowel-modifier VISARG
	"\u0D05": "\xA4",  # Vowel A
	"\u0D06": "\xA5",  # Vowel AA
	"\u0D07": "\xA6",  # Vowel I
	"\u0D08": "\xA7",  # Vowel II
	"\u0D09": "\xA8",  # Vowel U
	"\u0D0A": "\xA9",  # Vowel UU
	"\u0D0B": "\xAA",  # Vowel RI
	"\u0D0E": "\xAB",
	"\u0D0F": "\xAC",
	"\u0D10": "\xAD",
	"\u0D11": "\xB2",
	"\u0D12": "\xAF",
	"\u0D13": "\xB0",
	"\u0D14": "\xB1",
	"\u0D15": "\xB3",  # Consonant KA
	"\u0D16": "\xB4",  # Consonant
	"\u0D17": "\xB5",  # Consonant
	"\u0D18": "\xB6",  # Consonant
	"\u0D19": "\xB7",  # Consonant NGA
	"\u0D1A": "\xB8",  # Consonant
	"\u0D1B": "\xB9",  # Consonant
	"\u0D1C": "\xBA",  # Consonant
	"\u0D1D": "\xBB",  # Consonant
	"\u0D1E": "\xBC",  # Consonant JNA
	"\u0D1F": "\xBD",  # Consonant
	"\u0D20": "\xBE",  # Consonant
	"\u0D21": "\xBF",  # Consonant
	"\u0D22": "\xC0",  # Consonant
	"\u0D23": "\xC1",  # Consonant NNA
	"\u0D24": "\xC2",  # Consonant
	"\u0D25": "\xC3",  # Consonant
	"\u0D26": "\xC4",  # Consonant
	"\u0D27": "\xC5",  # Consonant
	"\u0D28": "\xC6",  # Consonant NA
	"\u0D29": "\xC7",  # Consonant NNNA
	"\u0D2A": "\xC8",  # Consonant PA
	"\u0D2B": "\xC9",  # Consonant PHA
	"\u0D2C": "\xCA",  # Consonant BA
	"\u0D2D": "\xCB",  # Consonant BHA
	"\u0D2E": "\xCC",  # Consonant MA
	"\u0D2F": "\xCD",  # Consonant YA
	"\u0D30": "\xCF",  # Consonant RA
	"\u0D31": "\xD0",  # Consonant RRA
	"\u0D32": "\xD1",  # Consonant LA
	"\u0D33": "\xD2",  # Consonant LLA
	"\u0D34": "\xD3",  # Consonant LLLA
	"\u0D35": "\xD4",  # Consonant VA
	"\u0D36": "\xD5",  # Consonant SHA
	"\u0D37": "\xD6",  # Consonant SSA
	"\u0D38": "\xD7",  # Consonant SA
	"\u0D39": "\xD8",  # Consonant HA
	"\u0D3E": "\xDA",  # Vowel Sign AA
	"\u0D3F": "\xDB",  # Vowel Sign I
	"\u0D40": "\xDC",  # Vowel Sign II
	"\u0D41": "\xDD",  # Vowel Sign U
	"\u0D42": "\xDE",  # Vowel
	"\u0D43": "\xDF",  # Vowel
	"\u0D46": "\xE0",  # Vowel
	"\u0D47": "\xE1",  # Vowel
	"\u0D48": "\xE2",  # Vowel
	"\u0D4A": "\xE4",  # Vowel
	"\u0D4B": "\xE5",  # Vowel
	"\u0D4C": "\xE6",  # Vowel
	"\u0D4D": "\xE8",  # Consonant
	"\u0D64": "\xEA",  # PURNA VIRAM Reserved
	"\u0D65": "\xEA",  # DEERGH VIRAM
	"\u0D66": "\xF1",  # Consonant
	"\u0D67": "\xF2",  # Consonant
	"\u0D68": "\xF3",  # Consonant
	"\u0D69": "\xF4",  # Consonant
	"\u0D6A": "\xF5",  # Consonant
	"\u0D6B": "\xF6",
	"\u0D6C": "\xF7",
	"\u0D6D": "\xF8",
	"\u0D6E": "\xF9",
	"\u0D6F": "\xFA",
}
INDICTRANS_HASHB_U2I = {
	"\u0981": "\xA1",  # vowel-modifier CHANDRABINDU
	"\u0982": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0983": "\xA3",  # Vowel-modifier VISARG
	"\u0985": "\xA4",  # Vowel A
	"\u0986": "\xA5",  # Vowel AA
	"\u0987": "\xA6",  # Vowel I
	"\u0988": "\xA7",  # Vowel II
	"\u0989": "\xA8",  # Vowel U
	"\u098A": "\xA9",  # Vowel UU
	"\u098B": "\xAA",  # Vowel RI
	"\u098F": "\xAB",
	"\u0990": "\xAD",
	"\u0993": "\xAF",
	"\u0994": "\xB1",
	"\u0995": "\xB3",  # Consonant KA
	"\u0996": "\xB4",  # Consonant
	"\u0997": "\xB5",  # Consonant
	"\u0998": "\xB6",  # Consonant
	"\u0999": "\xB7",  # Consonant NGA
	"\u099A": "\xB8",  # Consonant
	"\u099B": "\xB9",  # Consonant
	"\u099C": "\xBA",  # Consonant
	"\u099D": "\xBB",  # Consonant
	"\u099E": "\xBC",  # Consonant JNA
	"\u099F": "\xBD",  # Consonant
	"\u09A0": "\xBE",  # Consonant
	"\u09A1": "\xBF",  # Consonant
	"\u09A2": "\xC0",  # Consonant
	"\u09A3": "\xC1",  # Consonant NA
	"\u09A4": "\xC2",  # Consonant
	"\u09A5": "\xC3",  # Consonant
	"\u09A6": "\xC4",  # Consonant
	"\u09A7": "\xC5",  # Consonant
	"\u09A8": "\xC6",  # Consonant NA
	"\u09AA": "\xC8",  # Consonant PA
	"\u09AB": "\xC9",  # Consonant PHA
	"\u09AC": "\xCA",  # Consonant BA
	"\u09AD": "\xCB",  # Consonant BHA
	"\u09AE": "\xCC",  # Consonant MA
	"\u09AF": "\xCD",  # Consonant YA
	"\u09B0": "\xCF",  # Consonant RA
	"\u09B2": "\xD1",  # Consonant LA
	"\u09B6": "\xD5",  # Consonant SHA
	"\u09B7": "\xD6",  # Consonant SSA
	"\u09B8": "\xD7",  # Consonant SA
	"\u09B9": "\xD8",  # Consonant HA
	"\u09BC": "\xE9",  # Consonant NUKTA
	"\u09BE": "\xDA",  # Vowel Sign AA
	"\u09BF": "\xDB",  # Vowel Sign I
	"\u09C0": "\xDC",  # Vowel Sign II
	"\u09C1": "\xDD",  # Vowel Sign U
	"\u09C2": "\xDE",  # Vowel
	"\u09C3": "\xDF",  # Vowel
	"\u09C7": "\xE0",  # Vowel
	"\u09C8": "\xE2",  # Vowel
	"\u09CB": "\xE4",  # Vowel
	"\u09CC": "\xE6",  # Vowel
	"\u09CD": "\xE8",  # Consonant
	"\u09E4": "\xEA",  # PURNA VIRAM Reserved
	"\u09E5": "\xEA",  # DEERGH VIRAM
	"\u09E6": "\xF1",  # Consonant
	"\u09E7": "\xF2",  # Consonant
	"\u09E8": "\xF3",  # Consonant
	"\u09E9": "\xF4",  # Consonant
	"\u09EA": "\xF5",  # Consonant
	"\u09EB": "\xF6",
	"\u09EC": "\xF7",
	"\u09ED": "\xF8",
	"\u09EE": "\xF9",
	"\u09EF": "\xFA",
}
INDICTRANS_UNICODE_NORM_HASHB_U2I = {
	"\u09DC": "\u09A1",  # ADDED
	"\u09DD": "\u09A2",  # ADDED
	"\u09DF": "\u09AF"  # ADDED
}
INDICTRANS_HASHTA_U2I = {
	"\u0B82": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0B83": "\xA3",  # Vowel-modifier VISARG
	"\u0B85": "\xA4",  # Vowel A
	"\u0B86": "\xA5",  # Vowel AA
	"\u0B87": "\xA6",  # Vowel I
	"\u0B88": "\xA7",  # Vowel II
	"\u0B89": "\xA8",  # Vowel U
	"\u0B8A": "\xA9",  # Vowel UU
	"\u0B8E": "\xAB",
	"\u0B8F": "\xAC",
	"\u0B90": "\xAD",
	"\u0B92": "\xAF",  # check here
	"\u0B93": "\xB0",
	"\u0B94": "\xB1",
	"\u0B95": "\xB3",  # Consonant KA
	"\u0B99": "\xB7",  # Consonant NGA
	"\u0B9A": "\xB8",  # Consonant
	"\u0B9C": "\xBA",  # Consonant
	"\u0B9E": "\xBC",  # Consonant JNA
	"\u0B9F": "\xBD",  # Consonant
	"\u0BA3": "\xC1",  # Consonant NA
	"\u0BA4": "\xC2",  # Consonant
	"\u0BA8": "\xC6",  # Consonant NA
	"\u0BA9": "\xC7",  # Consonant NNNA
	"\u0BAA": "\xC8",  # Consonant PA
	"\u0BAE": "\xCC",  # Consonant MA
	"\u0BAF": "\xCD",  # Consonant YA
	"\u0BB0": "\xCF",  # Consonant RA
	"\u0BB1": "\xD0",  # Consonant RRA
	"\u0BB2": "\xD1",  # Consonant LA
	"\u0BB3": "\xD2",  # Consonant LLA
	"\u0BB4": "\xD3",  # Consonant LLLA
	"\u0BB5": "\xD4",  # Consonant VA
	"\u0BB6": "\xD5",  # Consonant SHA
	"\u0BB7": "\xD6",  # Consonant SSA
	"\u0BB8": "\xD7",  # Consonant SA
	"\u0BB9": "\xD8",  # Consonant HA
	"\u0BBE": "\xDA",  # Vowel Sign AA
	"\u0BBF": "\xDB",  # Vowel Sign I
	"\u0BC0": "\xDC",  # Vowel Sign II
	"\u0BC1": "\xDD",  # Vowel Sign U
	"\u0BC2": "\xDE",  # Vowel
	"\u0BC6": "\xE0",  # Vowel
	"\u0BC7": "\xE1",  # Vowel
	"\u0BC8": "\xE2",  # Vowel
	"\u0BCA": "\xE4",  # Vowel
	"\u0BCB": "\xE5",  # Vowel
	"\u0BCC": "\xE6",  # Vowel
	"\u0BCD": "\xE8",  # Halant
	"\u0BE4": "\xEA",  # PURNA VIRAM Reserved
	"\u0BE5": "\xEA",  # DEERGH VIRAM
	"\u0BE6": "\xF1",  # Consonant
	"\u0BE7": "\xF2",  # Consonant
	"\u0BE8": "\xF3",  # Consonant
	"\u0BE9": "\xF4",  # Consonant
	"\u0BEA": "\xF5",  # Consonant
	"\u0BEB": "\xF6",
	"\u0BEC": "\xF7",
	"\u0BED": "\xF8",
	"\u0BEE": "\xF9",
	"\u0BEF": "\xFA",
}
INDICTRANS_HASHO_U2I = {
	"\u0B01": "\xA1",  # Vowel-modifier CHANDRABINDU
	"\u0B02": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0B03": "\xA3",  # Vowel-modifier VISARG
	"\u0B05": "\xA4",  # Vowel A
	"\u0B06": "\xA5",  # Vowel AA
	"\u0B07": "\xA6",  # Vowel I
	"\u0B08": "\xA7",  # Vowel II
	"\u0B09": "\xA8",  # Vowel U
	"\u0B0A": "\xA9",  # Vowel UU
	"\u0B0B": "\xAA",  # Vowel RI
	"\u0B0F": "\xAC",
	"\u0B10": "\xAD",
	"\u0B13": "\xB0",
	"\u0B14": "\xB1",
	"\u0B15": "\xB3",  # Consonant KA
	"\u0B16": "\xB4",  # Consonant
	"\u0B17": "\xB5",  # Consonant
	"\u0B18": "\xB6",  # Consonant
	"\u0B19": "\xB7",  # Consonant NGA
	"\u0B1A": "\xB8",  # Consonant
	"\u0B1B": "\xB9",  # Consonant
	"\u0B1C": "\xBA",  # Consonant
	"\u0B1D": "\xBB",  # Consonant
	"\u0B1E": "\xBC",  # Consonant JNA
	"\u0B1F": "\xBD",  # Consonant
	"\u0B20": "\xBE",  # Consonant
	"\u0B21": "\xBF",  # Consonant
	"\u0B22": "\xC0",  # Consonant
	"\u0B23": "\xC1",  # Consonant NA
	"\u0B24": "\xC2",  # Consonant
	"\u0B25": "\xC3",  # Consonant
	"\u0B26": "\xC4",  # Consonant
	"\u0B27": "\xC5",  # Consonant
	"\u0B28": "\xC6",  # Consonant NA
	"\u0B2A": "\xC8",  # Consonant PA
	"\u0B2B": "\xC9",  # Consonant PHA
	"\u0B2C": "\xCA",  # Consonant BA
	"\u0B2D": "\xCB",  # Consonant BHA
	"\u0B2E": "\xCC",  # Consonant MA
	"\u0B2F": "\xCD",  # Consonant YA
	"\u0B30": "\xCF",  # Consonant RA
	"\u0B32": "\xD1",  # Consonant LA
	"\u0B33": "\xD2",  # Consonant LLA
	"\u0935": "\xD4",  # Consonant VA
	"\u0B36": "\xD5",  # Consonant SHA
	"\u0B37": "\xD6",  # Consonant SSA
	"\u0B38": "\xD7",  # Consonant SA
	"\u0B39": "\xD8",  # Consonant HA
	"\u0B3C": "\xE9",  # Consonant NUKTA
	"\u0B3E": "\xDA",  # Vowel Sign AA
	"\u0B3F": "\xDB",  # Vowel Sign I
	"\u0B40": "\xDC",  # Vowel Sign II
	"\u0B41": "\xDD",  # Vowel Sign U
	"\u0B42": "\xDE",  # Vowel
	"\u0B43": "\xDF",  # Vowel
	"\u0B47": "\xE1",  # Vowel
	"\u0B48": "\xE2",  # Vowel
	"\u0B4B": "\xE5",  # Vowel O
	"\u0B4C": "\xE6",  # Vowel OU
	"\u0B4D": "\xE8",  # Halant
	"\u0B64": "\xEA",  # PURNA VIRAM Reserved
	"\u0B65": "\xEA",  # DEERGH VIRAM
	"\u0B66": "\xF1",  # Digit 0
	"\u0B67": "\xF2",  # Digit 1
	"\u0B68": "\xF3",  # Digit 2
	"\u0B69": "\xF4",  # Digit 3
	"\u0B6A": "\xF5",  # Digit 4
	"\u0B6B": "\xF6",  # Digit 5
	"\u0B6C": "\xF7",  # Digit 6
	"\u0B6D": "\xF8",  # Digit 7
	"\u0B6E": "\xF9",  # Digit 8
	"\u0B6F": "\xFA",  # Digit 9
}
INDICTRANS_UNICODE_NORM_HASHO_U2I = {
	"\u0B5C": "\u0B21",  # ADDED
	"\u0B5D": "\u0B22",  # ADDED
	"\u0B5F": "\u0B2F"  # ADDED FOR EASE
}
INDICTRANS_HASHG_U2I = {
	"\u0A81": "\xA1",  # Vowel-modifier CHANDRABINDU
	"\u0A82": "\xA2",  # Vowel-modifier ANUSWAR
	"\u0A83": "\xA3",  # Vowel-modifier VISARG
	"\u0A85": "\xA4",  # Vowel A
	"\u0A86": "\xA5",  # Vowel AA
	"\u0A87": "\xA6",  # Vowel I
	"\u0A88": "\xA7",  # Vowel II
	"\u0A89": "\xA8",  # Vowel U
	"\u0A8A": "\xA9",  # Vowel UU
	"\u0A8B": "\xAA",  # Vowel RI
	"\u0A8D": "\xAE",
	"\u0A8F": "\xAC",
	"\u0A90": "\xAD",
	"\u0A91": "\xB2",
	"\u0A93": "\xB0",
	"\u0A94": "\xB1",
	"\u0A95": "\xB3",  # Consonant KA
	"\u0A96": "\xB4",  # Consonant
	"\u0A97": "\xB5",  # Consonant
	"\u0A98": "\xB6",  # Consonant
	"\u0A99": "\xB7",  # Consonant NGA
	"\u0A9A": "\xB8",  # Consonant
	"\u0A9B": "\xB9",  # Consonant
	"\u0A9C": "\xBA",  # Consonant
	"\u0A9D": "\xBB",  # Consonant
	"\u0A9E": "\xBC",  # Consonant JNA
	"\u0A9F": "\xBD",  # Consonant
	"\u0AA0": "\xBE",  # Consonant
	"\u0AA1": "\xBF",  # Consonant
	"\u0AA2": "\xC0",  # Consonant
	"\u0AA3": "\xC1",  # Consonant NA
	"\u0AA4": "\xC2",  # Consonant
	"\u0AA5": "\xC3",  # Consonant
	"\u0AA6": "\xC4",  # Consonant
	"\u0AA7": "\xC5",  # Consonant
	"\u0AA8": "\xC6",  # Consonant NA
	"\u0AAA": "\xC8",  # Consonant PA
	"\u0AAB": "\xC9",  # Consonant PHA
	"\u0AAC": "\xCA",  # Consonant BA
	"\u0AAD": "\xCB",  # Consonant BHA
	"\u0AAE": "\xCC",  # Consonant MA
	"\u0AAF": "\xCD",  # Consonant YA
	"\u0AB0": "\xCF",  # Consonant RA
	"\u0AB2": "\xD1",  # Consonant LA
	"\u0AB3": "\xD2",  # Consonant LLA
	"\u0AB5": "\xD4",  # Consonant VA
	"\u0AB6": "\xD5",  # Consonant SHA
	"\u0AB7": "\xD6",  # Consonant SSA
	"\u0AB8": "\xD7",  # Consonant SA
	"\u0AB9": "\xD8",  # Consonant HA
	"\u0ABC": "\xE9",  # Consonant NUKTA
	"\u0ABE": "\xDA",  # Vowel Sign AA
	"\u0ABF": "\xDB",  # Vowel Sign I
	"\u0AC0": "\xDC",  # Vowel Sign II
	"\u0AC1": "\xDD",  # Vowel Sign U
	"\u0AC2": "\xDE",  # Vowel
	"\u0AC3": "\xDF",  # Vowel
	"\u0AC7": "\xE1",  # Vowel
	"\u0AC8": "\xE2",  # Vowel
	"\u0AC9": "\xE7",  # Vowel
	"\u0ACB": "\xE5",  # Vowel
	"\u0ACC": "\xE6",  # Vowel
	"\u0ACD": "\xE8",  # Halant
	"\u0AE0": "\xAA",  # Vowel Sanskrit
	"\u0AE4": "\xEA",  # PURNA VIRAM Reserved
	"\u0AE5": "\xEA",  # DEERGH VIRAM
	"\u0AE6": "\xF1",  # Digit 0
	"\u0AE7": "\xF2",  # Digit 1
	"\u0AE8": "\xF3",  # Digit 2
	"\u0AE9": "\xF4",  # Digit 3
	"\u0AEA": "\xF5",  # Digit 4
	"\u0AEB": "\xF6",  # Digit 5
	"\u0AEC": "\xF7",  # Digit 6
	"\u0AED": "\xF8",  # Digit 7
	"\u0AEE": "\xF9",  # Digit 8
	"\u0AEF": "\xFA",  # Digit 9
}
