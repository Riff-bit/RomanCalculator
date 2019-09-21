
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

    def testToArabic(self):
        self.assertEqual(1, roman.toArabic("I"))
        self.assertEqual(3, roman.toArabic("III"))
        self.assertEqual(4, roman.toArabic("IV"))
        self.assertEqual(9, roman.toArabic("IX"))
        self.assertEqual(10, roman.toArabic("X"))
        self.assertEqual(42, roman.toArabic("XLII"))
        self.assertEqual(57, roman.toArabic("LVII"))
        self.assertEqual(98, roman.toArabic("XCVIII"))
        self.assertEqual(106, roman.toArabic("CVI"))
        self.assertEqual(225, roman.toArabic("CCXXV"))
        self.assertEqual(444, roman.toArabic("CDXLIV"))
        self.assertEqual(555, roman.toArabic("DLV"))
        self.assertEqual(733, roman.toArabic("DCCXXXIII"))
        self.assertEqual(876, roman.toArabic("DCCCLXXVI"))
        self.assertEqual(999, roman.toArabic("CMXCIX"))
        self.assertEqual(1024, roman.toArabic("MXXIV"))
        self.assertEqual(2048, roman.toArabic("MMXLVIII"))