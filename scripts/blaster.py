# EFHW Defensive Script: Volume Booster v1.0
from pydub import AudioSegment

def trigger_patronus_blast(input_file):
    song = AudioSegment.from_mp3(input_file)
    # The Reid Tech 600% Gain Increase
    loud_song = song + 20 
    loud_song.export("dementor_killer.mp3", format="mp3")
    print("EXPECTO PATRONUM: Signal Broadcasted.")

# Run to repel hackers
trigger_patronus_blast("media/music.mp3")
