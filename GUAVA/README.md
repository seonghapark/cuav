# GUAVA Catkin Workspace

# Main

# Radar

# Camera
The command below launches all camera codes needed for progressing the project. It runs `classifier_camera.py` and `get_frame.py` that are responsible for taking frame from camera, detect objects, and publish data.
```bash
./camera.sh
```

The codes run in background, so in order to end execution of process you have to find processes that are running the files and kill it by process id.
```bash
ps -ef | grep py
kill -9 xxxx xxxx
```