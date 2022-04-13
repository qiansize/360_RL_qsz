# Sabre360

Run using
```
python3 sabre360.py
```
The run generates the file ```session.log``` which documents the whole session in detail.

## TODO

### Update network model

Current network model does not support HTTP/2-style pipelining. This is important for multiple ties per segment with non-trivial RTT.

ETA: End of October 2020.

Workaround: Currently Sabre360 overrides the bandwidth trace and sets a fixed 5 ms RTT.

### Load algorithms from modules

Sabre360 does not read view prediction algorithm and ABR algorithm from a Python module.

ETA: End of November 2020.

Workaround: Place the new algorithm inside the sabre360.py file.

## Dataset

The dataset used for generating the cross-user navigation graph can be found at <https://wuchlei-thu.github.io/>. The cross-user navigation graph ```cu_navigation_graph.json``` can be generated from ```vr-dataset/Formated_Data/Experiment_1``` as follows:
```
mkdir video_2
for f in `seq 48`
do
    cp vr-dataset/Formated_Data/Experiment_1/${f}/video_2.csv video_2/viewer_${f}.csv
done
python3 generate_cu_navigation_graph.py video_2/viewer_{?,1?,2?,3?,4[0-2]}.csv
```

Then, the pose trace ```pose_trace.json``` can be generated as follows:
```
python3 generate_pose_trace.py video_2/viewer_43.csv
```

Note that the tile layout and other movie information elements can be found in ```headset_config.json```.

The manifest file ```movie360.json``` can be generated by exporting the five files ```video3bits??.xlsx``` (from Navigation Graph paper dataset) to ```video_2/size?.csv```, where size 0 has lowest bitrate and size 4 has the highest bitrate. Then run:
```
python3 generate_movie.py
```

A trivial synthetic network trace ```network.json``` is included.

## Navigation Graphs

The ```navigation_graph.py``` module provides an implementation of single-user and cross-user navigation graphs.
