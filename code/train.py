import argparse
import pandas as pd
import torch
import pytorch_lightning as pl
import wandb

from tqdm.auto import tqdm
from data.data_module import Dataloader
from models.model import Model
from pytorch_lightning.loggers import WandbLogger
from datetime import datetime, timezone, timedelta


def wandb_init(project="sementic text similarity", name="name") -> WandbLogger:
    try:
        wandb.login(key='')
    except:
        anony = "must"
        print('If you want to use your W&B account, go to Add-ons -> Secrets and provide your W&B access token. Use the Label name as wandb_api. \nGet your W&B access token from here: https://wandb.ai/authorize')
    
    time_serial = datetime.now(timezone(timedelta(hours=9))).strftime("%y%m%d-%h%M%S")

    wandb.init(project=project, name=f"{name}+{time_serial}")
    wandb_logger = WandbLogger('project')
    return wandb_logger


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', default='klue/roberta-small', type=str)
    parser.add_argument('--batch_size', default=4, type=int)
    parser.add_argument('--max_epoch', default=3, type=int)
    parser.add_argument('--shuffle', default=True)
    parser.add_argument('--logger', default=False)
    parser.add_argument('--learning_rate', default=1e-5, type=float)
    parser.add_argument('--train_path', default='dataset/train_tokenizer_len.csv')
    parser.add_argument('--dev_path', default='dataset/dev.csv')
    parser.add_argument('--test_path', default='dataset/dev.csv')
    parser.add_argument('--predict_path', default='dataset/test.csv')
    args = parser.parse_args(args=[])

    dataloader = Dataloader(args.model_name, args.batch_size, args.shuffle, args.train_path, args.dev_path,
                            args.test_path, args.predict_path)
    model = Model(args.model_name, args.learning_rate)

    # wandb init
    wandb_logger = wandb_init(name=args.model_name) if args.logger else None
    trainer = pl.Trainer(
        accelerator='gpu',
        devices=1,
        max_epochs=args.max_epoch, 
        log_every_n_steps=1,
        logger=wandb_logger
    )

    # Train part
    trainer.fit(model=model, datamodule=dataloader)
    trainer.test(model=model, datamodule=dataloader)

    torch.save(model, 'model.pt')
