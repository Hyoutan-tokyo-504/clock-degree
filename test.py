import unittest
import contextlib
import Clock_degree as cd


class redirect_stdin(contextlib._RedirectStream):
    _stream = "stdin"


class ClockTest(unittest.TestCase):
    def setUp(self):
        # Initialization process
        pass

    def tearDown(self):
        # End precess
        pass
    
    #input test
    def _calinput(self):
        return cd.clockinput()
    
    def test1(self):
        from io import StringIO
        buf = StringIO()
        buf.write("22 40\n")
        buf.seek(0)

        with redirect_stdin(buf):
            degree = self._calinput()
        expected = ['22','40']
        self.assertEqual(degree, expected)

    #error test
    def test2(self):
        #testpatterns = [normal,hour_over,min_over,hour_str,min_str]
        testpatterns = [('22','40',False),('25','40',True),('25','100',True),('aa','40',True),('30','bb',True)]
        for hour, minute, result in testpatterns:
            self.assertEqual(cd.errorjudge(hour,minute),result)
            

    #degree test
    def test3(self):
        #testpatterns = [normal, hour+12, (degree>180)_process, 0test]
        testpatterns = [(10,40,60),(22,40,60),(11,10,90),(0,0,0)]
        for hour, minute, result in testpatterns:
            self.assertEqual(cd.clock_degree(hour,minute),result)

if __name__ == "__main__":
    unittest.main()
