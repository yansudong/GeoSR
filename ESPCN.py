#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@CreateTime:   2018-10-10T12:16:31+09:00
@Email:  guozhilingty@gmail.com
@Copyright: Chokurei
@License: MIT

Geosr - A Computer Vision Package for Remote Sensing Image Super Resolution
"""
from __future__ import print_function
import argparse
import os
import torch
import torch.optim as optim
from models.espcn import ESPCN
from utils.loader import get_training_set, get_val_set, get_test_set
from utils.runner import Trainer

DIR = os.path.dirname(os.path.abspath(__file__))
method = os.path.basename(__file__).split(".")[0]

def main(args):
    print(args)
    if args.cuda and not torch.cuda.is_available():
        raise Exception("No GPU found, please run without --cuda")
    torch.manual_seed(args.seed)
    device = torch.device("cuda" if args.cuda else "cpu")
   
    print('===> Loading datasets')
    train_set = get_training_set(args.band_mode, args.data_dir, args.aug, args.aug_mode, args.crop_size, args.upscale_factor)
    # tensor, len = 600, for each : (input, target) 
    val_set = get_val_set(args.band_mode, args.data_dir, args.aug, args.aug_mode, args.crop_size, args.upscale_factor)
    test_set = get_test_set(args.band_mode, args.data_dir, args.aug, args.aug_mode, args.crop_size, args.upscale_factor)
    
    datasets = [train_set, val_set]
       
    print('===> Building model')
    model = ESPCN(nb_channel=args.nb_channel, upscale_factor=args.upscale_factor, base_kernel=args.base_kernel).to(device)
    #criterion = nn.MSELoss()
    model.optimizer = optim.Adam(model.parameters(), lr=args.lr)
    
    run = Trainer(args, method)
    run.training(model, datasets)
    run.save_log()
    run.learning_curve()
    
    run.evaluating(model, train_set, 'train')
    run.evaluating(model, val_set, 'val')
    run.evaluating(model, test_set, "test")
    print('===> Complete training')
    run.save_checkpoint(model)
    

if __name__ == '__main__':
    # Training settings
    parser = argparse.ArgumentParser(description='PyTorch Super Res Example')
    parser.add_argument('--band_mode', type=str, default='Y', choices=['Y', 'YCbCr', 'RGB'], help="band mode")
    parser.add_argument('--data_dir', type=str, default=os.path.join(DIR, 'dataset','map-rand'), help="data directory")
    parser.add_argument('--crop_size', type=int, default=224, help='crop size from each data. Default=224 (same to image size)')
    parser.add_argument('--nb_channel', type=int, default=1, help="input image band")
    parser.add_argument('--upscale_factor', type=int, default=2, help="super resolution upscale factor")
    parser.add_argument('--aug', type=lambda x: (str(x).lower() == 'true'), default=True, help='data augmentation or not') 
    parser.add_argument('--aug_mode', type=str, default='c', choices=['a', 'b', 'c', 'd', 'e'], 
                        help='data augmentation mode: a, b, c, d, e')
    parser.add_argument('--base_kernel', type=int, default=64, help="base kernel")
    parser.add_argument('--batch_size', type=int, default=64, help='training batch size')
    parser.add_argument('--testbatch_size', type=int, default=10, help='testing batch size')
    parser.add_argument('--nEpochs', type=int, default=10, help='number of epochs to train for')
    parser.add_argument('--lr', type=float, default=0.01, help='Learning Rate. Default=0.01')
    
    parser.add_argument('--trigger', type=str, default='epoch', choices=['epoch', 'iter'],
                        help='trigger type for logging')
    parser.add_argument('--interval', type=int, default=2,
                        help='interval for logging')
    
#    parser.add_argument('--cuda', action='store_true', help='use cuda?')
    parser.add_argument('--cuda', type=lambda x: (str(x).lower() == 'true'), default=True, help='use cuda?')
    parser.add_argument('--threads', type=int, default=6, help='number of threads for data loader to use')
    parser.add_argument('--seed', type=int, default=123, help='random seed to use. Default=123')
    args = parser.parse_args()
    result = main(args)
    
    