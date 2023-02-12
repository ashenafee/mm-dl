# https://sgcappres.opencast.utoronto.ca/paella/ui/watch.html?id=23d6bc1e-5c13-46c6-aa06-3c212b223baf
# https://sgcappres.opencast.utoronto.ca/static/mh_default_org/engage-player/23d6bc1e-5c13-46c6-aa06-3c212b223baf/4f63d6d1-418f-46ed-b947-574afb3687f2/presentation_715a9cd4_3582_4ff4_abc2_87aaca7edaa9.mp4


import requests


r = requests.get("https://sgcappres.opencast.utoronto.ca/paella/ui/watch.html?id=23d6bc1e-5c13-46c6-aa06-3c212b223baf")
print(r.text)
