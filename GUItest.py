# CamTracker GUI test

from camtracker import Setup
from sklearn.cluster import KMeans
# initialize setup
setup = Setup()

# run GUI
tracker = setup.start()
