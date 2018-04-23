PATH=$PATH:$HOME/voxforge/bin/htk/bin:$HOME/voxforge/bin/julius4/adintool
amixer sget Mic -c 1
amixer sset Mic 16 -c 1
export ALSADEV="plughw:1,0"
echo $ALSADEV
cd /Desktop/START
adintool -input mic -output file -filename data