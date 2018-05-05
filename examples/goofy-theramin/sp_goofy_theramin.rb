# Welcome to Sonic Pi v2.10
puts "starting"
use_synth :fm
s = play 60, release: 100, note_slide: 0.1


live_loop :listen do
  a = sync "/osc/play"
  control s, note: a
end
