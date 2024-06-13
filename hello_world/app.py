from moviepy.editor import *


def main():
    video = VideoFileClip("buggy.mp4")
    txt_clip = TextClip(
        "My Holidays 2013",
        font="./fonts/MiSans-Regular.ttf",
        fontsize=70,
        color="white",
    ).set_duration(2)
    result = CompositeVideoClip([video, txt_clip])
    result.write_videofile(
        "/tmp/edited.mp4",
        temp_audiofile="/tmp/temp_audio.mp3",
        fps=25,
    )


def lambda_handler(event, context):
    main()
    return {"statusCode": 200, "body": "done"}


if __name__ == "__main__":
    main()
