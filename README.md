# pycocotools 使用

## coco 数据格式

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
	"id": int, 
    "name": str, 
    "supercategory": str,
}]
```





COCO 

COCO.getCatIds()

COCO.loadCats(ids)