"""Demo of MultiModalEmotionRecognizer.
多模态情绪识别示例
"""
from aiya_core.emotion import MultiModalEmotionRecognizer

if __name__ == "__main__":
    recog = MultiModalEmotionRecognizer()
    # In a real system, audio_path/video_path would be file paths to media.
    # 实际系统中会使用实际的音频或视频文件
    print(recog.analyze_audio("dummy.wav"))
    print(recog.analyze_video("dummy.mp4"))
    print(recog.analyze(audio_path="dummy.wav", video_path="dummy.mp4"))
