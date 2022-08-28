import cv2
import random
import json
import os
from torch.utils.data import Dataset, DataLoader
import torch, torchvision
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torchvision
from torch.nn.utils.rnn import pad_sequence

from tqdm import tqdm
import torchvision
from torchvision import datasets, models, transforms
from sklearn.metrics import precision_score

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def precision_in_top(y_pred, y_test, persent=0.05, thr=0.5):
    p = np.argsort(y_pred)
    cnt = int(persent * len(y_test))
    
    top_pred = y_pred[p[-cnt:]] > thr
    top_y = y_test[p[-cnt:]]
    return top_y.mean()
    

def train_epoch(model, batch_gen, criterion, optimizer, is_train = True) :
    epoch_loss = 0.0
    count = 0
    loss_dict = {'precision_in_top': 0, 'loss': 0}
    model.train(is_train)

    all_pred = None
    all_labels = None
    for input, labels in tqdm(batch_gen) :
        # print(input.shape, labels)
        if type(input) == dict:
            input = {k: v.to(device) for k, v in input.items()}
        else:
            input = input.to(device)

        labels = labels.to(device).to(torch.long)

        with torch.set_grad_enabled(is_train) :
            pred = model(input)
            loss = criterion(pred, labels)
            if is_train :
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            all_pred = np.concatenate([all_pred, pred.detach().numpy()]) if all_pred is not None else pred.detach().numpy()
            all_labels = np.concatenate([all_labels, labels.detach().numpy()]) if all_labels is not None else labels.detach().numpy()
            loss_dict['loss'] += loss.item()
            count += 1
            
    loss_dict['precision_in_top'] = precision_in_top(all_pred[:, 1], all_labels)
    loss_dict['loss'] /= count
    return loss_dict


def train_model(model, train_loader, test_loader, criterion, optimizer, num_epochs, save_name='model', scheduler=None, verbose=True):
    loader = {'train': train_loader, 'test': test_loader}
    loss_names = ['precision_in_top', 'loss']
    history = {'train': {el: [] for el in loss_names},
               'test': {el: [] for el in loss_names}}
    best_loss = 0

    for epoch in range(num_epochs):
        if verbose:
            print('Epoch {}/{}'.format(epoch, num_epochs - 1))
            print('-' * 10)

        for phase in ['train', 'test']:
            epoch_loss = train_epoch(model, loader[phase], criterion, optimizer, phase == 'train')
            if verbose:
                print('{} {}'.format(phase, epoch_loss))

            for k, v in epoch_loss.items():
                history[phase][k].append(v)
        
        if scheduler is not None:
            scheduler.step()
        
        if best_loss < history['test']['precision_in_top'][-1]:
            best_loss = history['test']['precision_in_top'][-1]
        #   torch.save(model, '/content/drive/MyDrive/НТИ ИИ /team/sergey_models/{}_best'.format(save_name))
            torch.save(model, '{}_best'.format(save_name))
            
            if verbose:
                print('updated best loss, now it {}'.format(best_loss))
          
        torch.save(model, '{}_last'.format(save_name))

        if verbose:
            print()

    return history
