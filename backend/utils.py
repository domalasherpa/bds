
"""

utils

"""
import torch
import numpy as np
import torchvision.transforms as T
from yolo import Yolov1


'''

        new_class_label = {
                0:'Whimbrel'           ,
                1:'Osprey'             ,
                2:'Barn Swallow'       ,
                3:'Ruddy Turnstone'    ,
                4:'Barn Owl'           ,
                5:'Horned Lark'        ,
                6:'Common Raven'       ,
                7:'House Sparrow'      ,
                8:'Mallard'            ,
                9:'American Pipit'     ,
                10:'Peregrine Falcon',
                11:'Golden Eagle'
        }

        upper_left_x = box_coords[0] - box_coords[2] / 2
        upper_left_y = box_coords[1] - box_coords[3] / 2
        lower_right_x = box_coords[0] + box_coords[2] / 2
        lower_right_y = box_coords[1] + box_coords[3] / 2

        rect = patches.Rectangle(
            (upper_left_x * width, upper_left_y * height),
            lower_right_x * width,
            lower_right_y  * height,
            linewidth=1,
            edgecolor="r",
            facecolor="none",
        )


        json format = {
            prediction: [
                {
                    class: new_class_label[box[0]],
                    confidence: box[1],
                    box_coords: [upper_left_x, upper_left_y, lower_right_x, lower_right_y]
                }
                for box in bboxes
            ]
        }
'''

def format_prediction_string(image, bboxes):
    im = np.array(image)
    height, width, _ = im.shape

    new_class_label = {
        0:'Whimbrel'           ,
        1:'Osprey'             ,
        2:'Barn Swallow'       ,
        3:'Ruddy Turnstone'    ,
        4:'Barn Owl'           ,
        5:'Horned Lark'        ,
        6:'Common Raven'       ,
        7:'House Sparrow'      ,
        8:'Mallard'            ,
        9:'American Pipit'     ,
        10:'Peregrine Falcon',
        11:'Golden Eagle'
    }

    json_format = {
        'prediction': [
            {
                'class': new_class_label[int(box[0])],
                'confidence': float(box[1]),
                'box_coords': [
                    (box[2] - box[4] / 2) * width, 
                    (box[3] - box[5] / 2) * height, 
                    (box[2] + box[4] / 2) * width, 
                    (box[3] + box[5] / 2) * height
                ]
            }
            for box in bboxes
        ]
    }
    return json_format

def detect(image):
    # Load model
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

    model = Yolov1(split_size=7, num_boxes=2, num_classes=12).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters())  # Replace with actual optimizer used
    load_checkpoint(torch.load('checkpoint_epoch_200.pth.tar'), model, optimizer)
    
    # Prepare input image
    transform = T.Compose([
        T.Resize((448, 448)),
        T.ToTensor(),
        # T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    x = transform(image).unsqueeze(0).to(DEVICE)  # Add batch dimension and send to device

    # Run model
    model.eval()
    with torch.no_grad():
        output = model(x)
    
    # Post-process the output
    bboxes = cellboxes_to_boxes(output)  # Assuming you have defined cellboxes_to_boxes function
    
    bboxes = non_max_suppression(bboxes[0], iou_threshold=0.7, threshold=0.5, box_format="midpoint")
    return format_prediction_string(image, bboxes)


def intersection_over_union(boxes_preds, boxes_labels, box_format="midpoint"):
    """
    Calculates intersection over union

    Parameters:
        boxes_preds (tensor): Predictions of Bounding Boxes (BATCH_SIZE, 4)
        boxes_labels (tensor): Correct labels of Bounding Boxes (BATCH_SIZE, 4)
        box_format (str): midpoint/corners, if boxes (x,y,w,h) or (x1,y1,x2,y2)

    Returns:
        tensor: Intersection over union for all examples
    """

    if box_format == "midpoint":
        box1_x1 = boxes_preds[..., 0:1] - boxes_preds[..., 2:3] / 2
        box1_y1 = boxes_preds[..., 1:2] - boxes_preds[..., 3:4] / 2
        box1_x2 = boxes_preds[..., 0:1] + boxes_preds[..., 2:3] / 2
        box1_y2 = boxes_preds[..., 1:2] + boxes_preds[..., 3:4] / 2
        box2_x1 = boxes_labels[..., 0:1] - boxes_labels[..., 2:3] / 2
        box2_y1 = boxes_labels[..., 1:2] - boxes_labels[..., 3:4] / 2
        box2_x2 = boxes_labels[..., 0:1] + boxes_labels[..., 2:3] / 2
        box2_y2 = boxes_labels[..., 1:2] + boxes_labels[..., 3:4] / 2

    if box_format == "corners":
        box1_x1 = boxes_preds[..., 0:1]
        box1_y1 = boxes_preds[..., 1:2]
        box1_x2 = boxes_preds[..., 2:3]
        box1_y2 = boxes_preds[..., 3:4]  # (N, 1)
        box2_x1 = boxes_labels[..., 0:1]
        box2_y1 = boxes_labels[..., 1:2]
        box2_x2 = boxes_labels[..., 2:3]
        box2_y2 = boxes_labels[..., 3:4]

    x1 = torch.max(box1_x1, box2_x1)
    y1 = torch.max(box1_y1, box2_y1)
    x2 = torch.min(box1_x2, box2_x2)
    y2 = torch.min(box1_y2, box2_y2)

    # .clamp(0) is for the case when they do not intersect
    intersection = (x2 - x1).clamp(0) * (y2 - y1).clamp(0)

    box1_area = abs((box1_x2 - box1_x1) * (box1_y2 - box1_y1))
    box2_area = abs((box2_x2 - box2_x1) * (box2_y2 - box2_y1))

    return intersection / (box1_area + box2_area - intersection + 1e-6)


def non_max_suppression(bboxes, iou_threshold, threshold, box_format="midpoint"):
    """
    Does Non Max Suppression given bboxes

    Parameters:
        bboxes (list): list of lists containing all bboxes with each bboxes
        specified as [class_pred, prob_score, x1, y1, x2, y2]
        iou_threshold (float): threshold where predicted bboxes is correct
        threshold (float): threshold to remove predicted bboxes (independent of IoU)
        box_format (str): "midpoint" or "corners" used to specify bboxes

    Returns:
        list: bboxes after performing NMS given a specific IoU threshold
    """

    assert type(bboxes) == list

    bboxes = [box for box in bboxes if box[1] > threshold]
    bboxes = sorted(bboxes, key=lambda x: x[1], reverse=True)
    bboxes_after_nms = []

    while bboxes:
        chosen_box = bboxes.pop(0)

        bboxes = [
            box
            for box in bboxes
            if box[0] != chosen_box[0]
            or intersection_over_union(
                torch.tensor(chosen_box[2:]),
                torch.tensor(box[2:]),
                box_format=box_format,
            )
            < iou_threshold
        ]

        bboxes_after_nms.append(chosen_box)

    return bboxes_after_nms

def convert_cellboxes(predictions, S=7, C=12):
    """
    Converts bounding boxes output from YOLO with
    an image split size of S into entire image ratios
    rather than relative to cell ratios.
    """

    # Ensure predictions are on the same device as the input
    device = predictions.device
    
    batch_size = predictions.shape[0]
    predictions = predictions.reshape(batch_size, S, S, C+10)
    
    bboxes1 = predictions[..., C+1:C+5]
    bboxes2 = predictions[..., C+6:C+10]
    
    scores = torch.cat(
        (predictions[..., C].unsqueeze(0), predictions[..., C+5].unsqueeze(0)), dim=0
    )
    
    best_box = scores.argmax(0).unsqueeze(-1)
    best_boxes = bboxes1 * (1 - best_box) + best_box * bboxes2
    
    cell_indices = torch.arange(S, device=device).repeat(batch_size, S, 1).unsqueeze(-1)
    
    x = 1 / S * (best_boxes[..., :1] + cell_indices)
    y = 1 / S * (best_boxes[..., 1:2] + cell_indices.permute(0, 2, 1, 3))
    w_y = 1 / S * best_boxes[..., 2:4]
    
    converted_bboxes = torch.cat((x, y, w_y), dim=-1)
    predicted_class = predictions[..., :C].argmax(-1).unsqueeze(-1)
    best_confidence = torch.max(predictions[..., C], predictions[..., C+5]).unsqueeze(-1)
    
    converted_preds = torch.cat(
        (predicted_class, best_confidence, converted_bboxes), dim=-1
    )

    return converted_preds

def cellboxes_to_boxes(out, S=7):
    converted_pred = convert_cellboxes(out.to('cuda')).reshape(out.shape[0], S * S, -1)
    converted_pred[..., 0] = converted_pred[..., 0].long()
    all_bboxes = []

    for ex_idx in range(out.shape[0]):
        bboxes = []

        for bbox_idx in range(S * S):
            bboxes.append([x.item() for x in converted_pred[ex_idx, bbox_idx, :]])
        all_bboxes.append(bboxes)

    return all_bboxes

def load_checkpoint(checkpoint, model, optimizer):
    print("=> Loading checkpoint")
    model.load_state_dict(checkpoint["state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer"])
