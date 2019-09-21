
import unittest
import roman

class TestRoman(unittest.TestCase):

    def testFromArabic(self):
        self.assertEqual(roman.fromArabic(1),"I")
        self.assertEqual(roman.fromArabic(2),"II")
        self.assertEqual(roman.fromArabic(3),"III")
        self.assertEqual(roman.fromArabic(4),"IV")
        self.assertEqual(roman.fromArabic(10), "X")
        self.assertEqual(roman.fromArabic(14), "XIV")
        self.assertEqual(roman.fromArabic(24), "XXIV")
        self.assertEqual(roman.fromArabic(49), "XLIX")
        self.assertEqual(roman.fromArabic(67), "LXVII")
        self.assertEqual(roman.fromArabic(69), "LXIX")
        self.assertEqual(roman.fromArabic(89), "LXXXIX")
        self.assertEqual(roman.fromArabic(87), "LXXXVII")
        self.assertEqual(roman.fromArabic(342), "CCCXLII")
        self.assertEqual(roman.fromArabic(499), "CDXCIX")
        self.assertEqual(roman.fromArabic(998), "CMXCVIII")
        self.assertEqual(roman.fromArabic(1586), "MDLXXXVI")
        self.assertEqual(roman.fromArabic(2019), "MMXIX")


