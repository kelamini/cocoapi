from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab


if __name__ == "__main__":
    dataDir = "."
    dataType='val2017'
    annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
    cocoset = COCO(annFile)

    
    # display COCO categories and supercategories
    cats = cocoset.loadCats(cocoset.getCatIds())
    
    nms=[cat['name'] for cat in cats]
    print('COCO categories: \n{}\n'.format(' '.join(nms)))

    nms = set([cat['supercategory'] for cat in cats])
    print('COCO supercategories: \n{}'.format(' '.join(nms)))


    # get all images containing given categories, select one at random
    catIds = cocoset.getCatIds(catNms=['person','dog','skateboard'])
    print(f"catIds: {catIds}")
    imgIds = cocoset.getImgIds(imgIds=[324158])
    print(f"imgIds: {imgIds}")
    imgIds = cocoset.getImgIds(catIds=catIds)
    print(f"imgIds: {imgIds}")
    img = cocoset.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[0]

    # load and display image
    # I = io.imread('%s/images/%s/%s'%(dataDir,dataType,img['file_name']))
    # use url to load image
    I = io.imread(img['coco_url'])
    plt.axis('off')
    plt.imshow(I)
    plt.show()


    # load and display instance annotations
    # plt.imshow(I); plt.axis('off')
    annIds = cocoset.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
    print(annIds)
    anns = cocoset.loadAnns(annIds)
    cocoset.showAnns(anns)
