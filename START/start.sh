PATH=$PATH:$HOME/voxforge/bin/htk/bin:$HOME/voxforge/bin/julius4/julius
amixer sget Mic -c 1
amixer sset Mic 16 -c 1
export ALSADEV="plughw:1,0"
echo $ALSADEV
cd /home/pi/voxforge/manual1
julius -input mic -C sample.jconf > output.txt