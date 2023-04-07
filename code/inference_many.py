import argparse
import pandas as pd
import torch
import pytorch_lightning as pl

from torch.utils.data import DataLoader
from transformers import AutoTokenizer
from tqdm.auto import tqdm
from data.data_module import Dataloader
    
    
if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', default='klue/roberta-small', type=str)
    parser.add_argument('--batch_size', default=4, type=int)
    parser.add_argument('--max_epoch', default=1, type=int)
    parser.add_argument('--shuffle', default=True)
    parser.add_argument('--learning_rate', default=1e-5, type=float)
    parser.add_argument('--train_path', default='dataset/train.csv')
    parser.add_argument('--dev_path', default='dataset/dev.csv')
    parser.add_argument('--test_path', default='dataset/dev.csv')
    parser.add_argument('--predict_path', default='dataset/test.csv')
    args = parser.parse_args(args=[])

    dataloader = Dataloader(args.model_name, args.batch_size, args.shuffle, args.train_path, args.dev_path,
                            args.test_path, args.predict_path)

    trainer = pl.Trainer(
        accelerator='gpu', 
        max_epochs=args.max_epoch, 
        log_every_n_steps=1
    )

    model = torch.load('model.pt')
    predictions = trainer.predict(model=model, datamodule=dataloader)

    # 예측된 결과를 형식에 맞게 반올림
    predictions = list(round(float(i), 1) for i in torch.cat(predictions))

    # output 형식을 불러와서 예측된 결과로 바꿔주고, output.csv로 출력
    output = pd.read_csv('../data/sample_submission.csv')
    output['target'] = predictions
    output.to_csv('output.csv', index=False)
