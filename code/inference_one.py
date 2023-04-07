import torch
import pymongo
from transformers import AutoTokenizer


@torch.no_grad()
def inference(sentence_1, sentence_2, is_db=False):
    '''
    두 문장을 입력하여 추론을 진행하는 함수
    args:
        sentence_1 : 첫 번째 문장
        sentence_2 : 두 번째 문장
    return:
        0 ~ 5 사이의 실수
    '''
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model_name = 'klue/roberta-small'
    tokenizer = AutoTokenizer.from_pretrained(
        pretrained_model_name_or_path=model_name,
        max_length=64
    )
    
    text = '[SEP]'.join([sentence_1, sentence_2])
    inputs = tokenizer(text, add_special_tokens=True, padding='max_length', return_tensors='pt')['input_ids']
    inputs = inputs.to(device)

    model = torch.load('models/model.pt').to(device)
    prediction = model(inputs)
    prediction = round(prediction.squeeze().item(), 1)
    
    if is_db:
        try:
            connection = pymongo.MongoClient("0.0.0.0", 27017)
            db = connection.sts
            collection = db.user_input
            collection.insert_one({
                'sentence_1': sentence_1,
                'sentence_2': sentence_2,
                'Label': prediction
            })
        except BaseException as e:
            # db not connected
            print(e)

    return prediction

if __name__ == '__main__':
    inference("test1", "test2")