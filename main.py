import image_worker
from pydub import AudioSegment
from pydub.playback import play
import time

def main():
    print('This program helps you keep your head in the right place during screen work')
    print('You may have a tendency to lurch your chin forward without realizing it')
    print('This leads to undue strain on your neck and back muscles, and if you are like this dev it puts you in a world of hurt')
    print('----------------------------------')
    print('----------------------------------')
    print('The program starts by defining good and bad head posture')
    print('Then, it takes a picture every 10 seconds and rings a bell if you are straining your head forward')
    print('For good posture, pull your chin back towards your neck')
    print('For bad posture, push your chin forward')
    ready = input('ready?? (press enter to start)')

    config = image_worker.get_config()
    good_posture = image_worker.set_posture(config, 'good')
    bad_posture = image_worker.set_posture(config, 'bad')

    # Load an audio file
    audio = AudioSegment.from_file("bad_posture.mp3")

    input('ok go back to good posture and press start')

    while True:
        image_worker.capture_image('current')
        eyepop_results = image_worker.parse_image(config, 'current.jpg')
        left_eye, right_eye = image_worker.find_eye_positions(eyepop_results)
        dx = left_eye['x'] - right_eye['x']
        eye_distance_range = bad_posture['dx'] - good_posture['dx']
        print('current eye distance: ', dx)
        print('bad posture eye distance: ', bad_posture['dx'])
        print('good posture eye distance: ', good_posture['dx'])
        print('eye distance range: ', eye_distance_range)
        if dx > (.75 * eye_distance_range + good_posture['dx']):
            print('bad posture')
            play(audio)
        else:
            print('your head position is ok!')
        time.sleep(10)

if __name__ == '__main__':
    main()

