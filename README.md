# YOLOv5_on_healthcare__X-Ray_lesion_detection
Chest X-Ray Lesion Detection with YOLOv5 

Overview
This project aims to improve patient outcomes and ease healthcare professionals’ workflows with a deep learning model - YOLOv5. The model is trained to identify suspicious findings in Chest X-Rays (CXR) on a hospital scale. The ultimate goal is to flag patients who may require priority attention and forward them to more detailed diagnostic exams. 
The model was trained on the NIH Chest X-Ray dataset available here:
https://www.kaggle.com/datasets/nih-chest-xrays/data/data

Get Started
If you want to deep dive with this, you can start with install and import dependencies  (I did it on Anaconda prompt)
- used Python 3.10 on the project environment);
- Pytorch (CPU version for my AMD laptop) and install the code provided;
- YOLOv5 repository: https://github.com /ultralytics/yolov5
Download zip and >pip install -r requirements.txt
- Import torch

Define your yaml file:
path: data  #dataset root dir
train: yolov5-master\data\images # train images (relative to ‘path’)
val: yolov5-master\data\images # val images(relative to ‘path’)
test: #test images (optional) 
# classes
nc: 1 # just used one to define “suspicious lesion”
names/label: [“Finding”]

Training the model
!python train.py --img 640 --batch 16 --epochs 150 --data dataset.yml --weights yolov5s.pt


Load the model and Inference
model = torch.hub.load('ultralytics/yolov5', 'custom', path = path/to/ dataset', force_reload = True)
img=os.path.join(‘path/to/dataset’,'img','01.png')
results = model(img)
results.print()

Results visualization
%matplotlib inline
plt.imshow(np.squeeze(results.render()))
plt.show()

