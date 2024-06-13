from moviepy.editor import *


def main():
    video = VideoFileClip("buggy.mp4")

    txt_clip = (
        TextClip(
            "My Holidays 2013",
            fontsize=70,
            size=[1000, 500],
            color="black",
        )
        .set_position("center")
        .set_duration(2)
    )
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
