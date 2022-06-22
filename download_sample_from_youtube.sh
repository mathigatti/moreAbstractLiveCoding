
URL=$1
FROM=$2
TO=$3
OUTPUT_PATH=$4

yt-dlp $URL -x --audio-format wav -o temp_audio_file.wav

ffmpeg -i temp_audio_file.wav -ss $FROM -to $TO $OUTPUT_PATH

rm temp_audio_file.wav