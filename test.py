from main import parse, translate
from unittest import TestCase, main

class Test(TestCase):

    def test_parse(self):
        self.assertEqual(parse("(a[i]-1;b[s]-hello;c[f]-1.5)"), {
            "a": 1,
            "b": "hello",
            "c": 1.5,
        })

    def test_translate(self):
        FML = [
            "(a[i]-1;b[s]-hello;c[f]-1.5)",
            "(a[i]-1;c[f]-1.5)",
            "(a[i]-1;b[s]-world)",
        ]
        self.assertEqual(translate(FML, ["a", "b", "c"]), [
            [1, "hello", 1.5],
            [1, "NAN", 1.5],
            [1, "world", "NAN"],
        ])

if __name__ == "__main__": main()