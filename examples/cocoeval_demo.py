import matplotlib.pyplot as plt
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import pylab


annType = ['segm','bbox','keypoints']
annType = annType[1]      #specify type here
prefix = 'person_keypoints' if annType=='keypoints' else 'instances'
print (f'Running demo for *{annType}* results.')


#initialize COCO ground truth api
dataDir='..'
dataType='val2017'
annFile = f'{dataDir}/annotations/{prefix}_{dataType}.json'
cocoGt=COCO(annFile)

#initialize COCO detections api
resFile = f'{dataDir}/results/{prefix}_val2014_fake{annType}100_results.json'
cocoDt=cocoGt.loadRes(resFile)

imgIds=sorted(cocoGt.getImgIds())
imgIds=imgIds[0:100]
imgId = imgIds[np.random.randint(100)]

# running evaluation
cocoEval = COCOeval(cocoGt,cocoDt,annType)
cocoEval.params.imgIds  = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()