from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = sentiment_analyzer('I am glad this happened')
        print(result_1)
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        #result_1 = sentiment_analyzer('I am really mad about this')
        #self.assertEqual(result_1'dominant_emotion']], 'anger')

        #result_1 = sentiment_analyzer('I feel disgusted just hearing about this')
        #self.assertEqual(result_1['dominant_emotion'], 'disgust')

        #result_1 = sentiment_analyzer('I am so sad about this')
        #self.assertEqual(result_1['dominant_emotion'], 'sadness')

        #result_1 = sentiment_analyzer('I am really afraid that this will happen')
        #self.assertEqual(result_1['dominant_emotion'], 'fear')
