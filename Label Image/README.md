# LabelImg

LabelImg is a graphical image annotation tool that supports creating annotations in PASCAL VOC and YOLO formats. This tool is commonly used for training machine learning and deep learning models.

## Installation and Setup
[labelImg](https://github.com/HumanSignal/labelImg)

### Prerequisites

Please make sure you have [Anaconda](https://www.anaconda.com/products/distribution) installed on your system and open anaconda prompt.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/HumanSignal/labelImg.git
   cd labelImg
   ```

2. Install the required dependencies:
   ```bash
   conda install pyqt=5
   conda install -c anaconda lxml
   ```

3. Compile the resource file:
   ```bash
   pyrcc5 -o libs/resources.py resources.qrc
   ```

4. Run LabelImg:
   ```bash
   python labelImg.py
   ```

### Optional Command

To start LabelImg with a specific image path and pre-defined class file:
```bash
python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

## Example

![LabelImg Example](https://github.com/user-attachments/assets/3d9d2583-68b6-49e2-8716-f146eb08a361)

## Repository

Find the LabelImg repository here: [LabelImg on GitHub](https://github.com/HumanSignal/labelImg).

python labelImg.py [IMAGE_PATH] [PRE-DEFINED CLASS FILE]

