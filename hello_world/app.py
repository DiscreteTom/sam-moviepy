import json
from moviepy.editor import *


def main():
    video = VideoFileClip("buggy.mp4")

    # Make the text. Many more options are available.
    txt_clip = TextClip("My Holidays 2013", fontsize=70, color="white").set_duration(2)

    result = CompositeVideoClip([video, txt_clip])  # Overlay text on video
    result.write_videofile("edited.mp4", fps=25)  # Many options...


def lambda_handler(event, context):
    main()

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }


if __name__ == "__main__":
    main()
