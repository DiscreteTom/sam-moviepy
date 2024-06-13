# sam-moviepy

An example project to demonstrate how to use MoviePy to create a video with text on AWS Lambda.

## Key Points

- Only `/tmp` folder is writable on AWS Lambda.
- Use container deployment (instead of Zip) to install ImageMagick.