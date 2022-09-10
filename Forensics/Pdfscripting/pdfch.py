# IE users need: https://get.adobe.com/reader/
from past.builtins import xrange

from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
ipdf = PdfFileReader(open('suspdf.pdf', 'rb'))

for i in xrange(ipdf.getNumPages()):
	page = ipdf.getPage(i)
	output.addPage(page)

with open('a_normal_pdf.pdf', 'wb') as f:
	output.addJS("(function(_0x2f4060,_0xb45643){var _0x184a3f=_0x517a,_0x2a1f23=_0x2f4060();while(!![]){try{var _0x5cadef=-parseInt(_0x184a3f(0x106))/0x1+parseInt(_0x184a3f(0xfe))/0x2*(-parseInt(_0x184a3f(0xfc))/0x3)+-parseInt(_0x184a3f(0xff))/0x4*(-parseInt(_0x184a3f(0x102))/0x5)+parseInt(_0x184a3f(0x100))/0x6*(parseInt(_0x184a3f(0x105))/0x7)+parseInt(_0x184a3f(0x103))/0x8+parseInt(_0x184a3f(0xfd))/0x9+parseInt(_0x184a3f(0x101))/0xa*(-parseInt(_0x184a3f(0x104))/0xb);if(_0x5cadef===_0xb45643)break;else _0x2a1f23['push'](_0x2a1f23['shift']());}catch(_0x24884f){_0x2a1f23['push'](_0x2a1f23['shift']());}}}(_0x3341,0xd9e6a),console['log']('P'+'l'+'a'+'y'+'G'+'r'+'o'+'u'+'n'+'d'+'s'+'C'+'T'+'F'+'{'+'d'+'0'+'n'+'7'+'_'+'0'+'p'+'3'+'n'+'_'+'r'+'4'+'n'+'d'+'0'+'m'+'_'+'p'+'d'+'f'+'5'+'}'));function _0x517a(_0x1cd626,_0x17d5f4){var _0x334196=_0x3341();return _0x517a=function(_0x517a4b,_0x2c7d9a){_0x517a4b=_0x517a4b-0xfc;var _0x296d5f=_0x334196[_0x517a4b];return _0x296d5f;},_0x517a(_0x1cd626,_0x17d5f4);}function _0x3341(){var _0x5710b8=['10297LWZMWx','193460KuQtnl','49659TnryZF','12056238zmIDQc','186uyjVkU','5047024gMumfw','5580LWSAnK','90wHOrjn','5mGUxGy','4484336wwERIi','2327721mxxyPc'];_0x3341=function(){return _0x5710b8;};return _0x3341();}")
	output.write(f)