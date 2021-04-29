import cv2
import glob

# 1, snaps to video
ONE = True
TWO = True

if ONE:
    img_array = []
    for filename in sorted(glob.glob('snaps/snap*.png')):
        print("reading ", filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
     
    print("size is: ", size)

    #fourcc = cv2.cv.CV_FOURCC(*'mp4v') 
    out = cv2.VideoWriter('video/output_rip.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
 
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

# 2: add audio
import moviepy.editor as mpe

if TWO:
    my_clip = mpe.VideoFileClip('video/output_rip.mp4')
    audio = mpe.AudioFileClip('audio/theme_cut.mp3')
    #final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
    final_clip = my_clip.set_audio(audio)
    final_clip.write_videofile("video/output_mix.mp4",
                                 codec= 'libx264',
                                 audio_codec='aac', 
                                 temp_audiofile='temp-audio.m4a', 
                                 remove_temp=True
                                 )




