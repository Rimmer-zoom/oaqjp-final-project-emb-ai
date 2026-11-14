import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector('I am glad this happened')
        self.assertIn('joy', str(result))


if __name__ == '__main__':
    unittest.main()
