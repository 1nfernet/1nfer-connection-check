import unittest
from probe import check
class Probe(unittest.TestCase):
 def test_only_public_reads(self):
  paths=[]
  def get(path):
   paths.append(path);return {'data':[{'id':'test'}]} if path=='models' else {'enabled':False}
  self.assertEqual(check(get),{'model-count':'1','funding-enabled':'false'});self.assertEqual(paths,['models','payments/terms'])
 def test_invalid_or_empty_catalogue_rejected(self):
  for data in ({},{'data':[]},{'data':[1]}):
   with self.assertRaises(ValueError):check(lambda p:data if p=='models' else {'enabled':True})
 def test_invalid_payment_state_rejected(self):
  with self.assertRaises(ValueError):check(lambda p:{'data':[{'id':'test'}]} if p=='models' else {'enabled':'true'})
if __name__=='__main__':unittest.main()
