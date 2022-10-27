# pycocotools 使用

## coco 数据文件格式

```json
{
	"info": info, 
    "images": [image], 
    "annotations": [annotation], 
    "licenses": [license],
}

info{
    "year": int, 
    "version": str, 
    "description": str, 
    "contributor": str, 
    "url": str, 
    "date_created": datetime,
}

image{
	"id": int, 
    "width": int, 
    "height": int, 
    "file_name": str, 
    "license": int, 
    "flickr_url": str, 
    "coco_url": str, 
    "date_captured": datetime,
}

license{
	"id": int, 
    "name": str, 
    "url": str,
}
```



### 1. Object Detection

```json
annotation{
	"id": int, 
    "image_id": int, 
    "category_id": int, 
    "segmentation": RLE or [polygon], 
	"area": float, 
	"bbox": [x,y,width,height], 
	"iscrowd": 0 or 1,
}

categories[{
	"id": int, b
    "name": str, 
    "supercategory": str,
}]
```



## 预测结果文件格式

### 1. Object Detection

```json
[{
	"image_id": int, 
    "category_id": int, 
    "bbox": [x,y,width,height], 
    "score": float,
}]
```

### 2. Detection with Object Segments

```json
[{
	"image_id": int, 
    "category_id": int, 
    "segmentation": RLE, 
    "score": float,
}]
```

## 函数和功能

### COCO 类

#### createIndex() 函数

对数据作映射

- anns 是一个字典，键为 annotation 的 ID 号，值为 annotation 字典；

- cats 是一个字典，键为 categorie 的 ID 号，值为 categorie 字典；

- imgs 是一个字典，键为 image 的 ID 号，值为 image 字典

- imgToAnns 是一个字典，键为 image 的 ID 号，值为 annitation 字典；

- catToImgs 是一个字典，键为 categorie 的 ID 号，值为 image 的 ID 号；

#### getAnnIds() 函数

可以通过 image 的 ID 号、categorie 的 ID 号、areaRng 的面积大小获取 annotation 的 ID 号

- 输入参数：
  - imgIds：image 的 ID 号
  - catIds：categorie 的 ID 号
  - areaRng：
- 函数返回：
  - ids：annotation 的 ID 号

#### getCatIds() 函数

可以通过 categorie 的名称、supercategory 的名称、categorie 的 ID 号获取 categorie 的 ID 号

- 输入参数：
  - catNms：categorie 的名称
  - supNms：supercategory 的名称
  - catIds：categorie 的 ID 号
- 函数返回：
  - ids：categorie 的 ID 号

#### getImgIds() 函数

可以通过 image 的 ID 号、categorie 的 ID 号获取 image 的 ID 号

- 输入参数：
  - imgIds：image 的 ID 号
  - catIds：categorie 的 ID 号
- 函数返回：
  - ids：image 的 ID 号

#### loadAnns() 函数

可以通过给定 annotation 的 ID 号获取 annotation 字典

- 输入参数：
  - ids：annotation 的 ID 号
- 函数返回：
  - 包含 annotation 字典的列表

#### loadCats() 函数

可以通过给定 categorie 的 ID 号获取 categorie 字典

- 输入参数：
  - ids：categorie 的 ID 号
- 函数返回：
  - 包含 categorie 字典的列表

#### loadImgs() 函数

可以通过给定 image 的 ID 号获取 image 字典

- 输入参数：
  - ids：image 的 ID 号
- 函数返回：
  - 包含 image 字典的列表

#### showAnns() 函数

显示经过标记的图像

- 输入参数：
  - anns：包含 annotation 字典的列表
  - draw_bbox：是否画框（bool 值）
- 函数返回：
  - annotation 标记后的图像

#### loadRes() 函数

- 输入参数：
  - resFile：包含预测结果的 json 文件的路径
- 函数返回：
  - res：COCO 类

#### download() 函数

#### loadNumpyAnnotations() 函数

#### annToRLE() 函数

#### annToMask() 函数

### COCOeval 类

#### _prepare() 函数

#### evaluate() 函数

#### computeIoU() 函数

- 输入参数：
  - imgId：image 的 ID 号
  - catId：categorie 的 ID 号
- 函数返回：
  - ious：计算的 IoU 值





### Params 类

#### setDetParams() 函数

初始化检测类的参数

- self.imgIds：[]	# image 的 ID 号
- self.catIds：[]     # categorie 的 ID 号
- self.iouThrs：[0.5, 0.55, ..., 0.95]    # IoU 的阈值，范围为 [0.5, 0.95]，间隔为 0.05
- self.recThrs：[0, 0.01, ..., 1]
- self.maxDets：[1, 10, 100]    # 最大的检测数量
- self.areaRng：[[0 ** 2, 1e5 ** 2], [0 ** 2, 32 ** 2], [32 ** 2, 96 ** 2], [96 ** 2, 1e5 ** 2]]    # 面积的范围
- self.areaRngLbl：['all', 'small', 'medium', 'large']    # 面积范围的标签
- self.useCats：1    # 是否使用 categorie 的 ID 号

#### setKpParams() 函数

初始化关键点类的参数

- self.imgIds：[]	# image 的 ID 号
- self.catIds：[]     # categorie 的 ID 号
- self.iouThrs：[0.5, 0.55, ..., 0.95]    # IoU 的阈值，范围为 [0.5, 0.95]，间隔为 0.05
- self.recThrs：[0, 0.01, ..., 1]
- self.maxDets：[20]    # 最大的检测数量
- self.areaRng：[[0 ** 2, 1e5 ** 2], [32 ** 2, 96 ** 2], [96 ** 2, 1e5 ** 2]]    # 面积的范围
- self.areaRngLbl：['all', 'medium', 'large']    # 面积范围的标签
- self.useCats：1    # 是否使用 categorie 的 ID 号
- self.kpt_oks_sigmas：[.26, .25, .25, .35, .35, .79, .79, .72, .72, .62,.62, 1.07, 1.07, .87, .87, .89, .89]/10.0