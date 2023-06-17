import torch
import os
from data import Dataset
from torch.utils import data
import torch.nn.functional as F
from models import *
from utils import Visualizer, view_model
import torch
from config import Config
from torch.nn import DataParallel
from torch.optim.lr_scheduler import StepLR
from test import *
from models.arcface import get_triplet_model
from tqdm.auto import tqdm

eval_losses=[]
train_val_loss=[]
def validate(model, device, test_loader, criterion, check_train = False, save_ckpt = True, callbacks = None):
    """
    a method to validate the model

    Parameters:
            model: your created model
            device: specify to use GPU or CPU
            test_loader: The dataloader for testing
            criterion: the loss function
    
    """
    torch.manual_seed(100)
    model.eval()
    test_loss = 0
    iters = 0
    with torch.no_grad():
        for ii, data in enumerate(trainloader):
            data_input, label = data
            data_input = data_input.to(device)
            label = label.to(device).long()
            feature = model(data_input)
            output = metric_fc(feature, label)
            loss = criterion(output, label)
            test_loss += loss.item()
        if not check_train:
            eval_losses.append(test_loss/len(test_loader))
        else:
            train_val_loss.append(test_loss/len(test_loader))
        print('\nTest set: Average loss: {:.4f}\n'.format(test_loss/len(test_loader)))
        if not os.path.exists('./weights/'):
            os.makedirs('./weights/')

    if save_ckpt:
        torch.save(model.backbone.state_dict(), "weight/model_finetune_arcface_iresNet.pth")
        torch.save(arcface.state_dict(), "weight/arcface_IresNet_weight.pth")
        if callbacks is not None:
            callbacks[0](test_loss/len(test_loader), model.backbone)
            callbacks[1](test_loss/len(test_loader), arcface)