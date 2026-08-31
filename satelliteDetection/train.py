if __name__ == "__main__":
    print("running script OI OI OI OI")
    from ultralytics import YOLO
    print("imported yolo SUIIIIIIIIIII")
    
    model = YOLO("yolov8n-obb.pt")
    print("training started HEE HEEEEEEEEEEEEEE")

    results = model.train(
        data='dataset.yaml',
        epochs=50,
        imgsz=1024,
        batch=4,
        device=0,
        workers = 0, #work in main process
                     #not in separate worker processes
                     #slower 
        project='results',
        name='yolov8n_obb_dota',
        exist_ok=True
    )

##epoch output skeleton:
#GPU_mem = how much VRAM being used, 8GB physical but borrowing from RAM
#box_loss = how badly model is drawing bounding boxes, lower = better
#cls_loss = how badly model guessing class, lower = better
#dfl_loss = precise measure of bounding box edge quality, lower = better
#angle_loss = how badly model predicts rotation angle of bounding box, lower = better
#instances = avg # of object per image in this batch 

#after each epoch, model runs on 458 val images, to check performance on unseen data 

#using rand numbers to illustruate: 
#box(P.0715) = of all drawn boxes drawn, 71.5% were right 
#R(0.323) = recall of actual objects in images, it only found 32.3%, low recall = missing a lot of objects
#mAP50 (0.355) = mean avg precision at 50% overlap threshold, 0 = useless, 1 = perfect
#mAP50-95 (0.248) = stricter version of above, averages across many overlap thresholds

#explanation of the mAP50 and mAP50-95 metrics:
#both metrics use IoU; intersection over union, it calculates overlap area / total area of combined boxes

#using lasso analogy, target is a wooden post, the lasso loop is the box drawn by model

#mAP50 is "close enough", as long as lasso lands and covers 50%, you get full credit
#you dont have to be perfect, loop can be huge, sloppy, off center, it is LENIENT 
#just means the model is good @ simply finding the object

#mAP50-95 is an average of 10 lasso throws, with these thresholds = 0.50, 0.55, 0.60, 0.65 ... 0.95
#you have to be very near perfect to be credited by this metric, it is STRICT
#measures if model is good at perfectly framing object. 
