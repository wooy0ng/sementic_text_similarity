<div align="center">
 <h1> 문장 간 유사도 계산 </h1>
 <img src="https://user-images.githubusercontent.com/37149278/230639203-bd7d2031-0b86-479b-b344-c48cb7d64b72.PNG" width="750">
 
 <br>
 복수의 문장에 대한 유사도를 수치로 제시하는 NLP Task입니다.  <br />
 <b>정보 추출, QA 및 요약</b>과 같은 NLP 문제에 널리 활용됩니다. <br />
 실제 어플리케이션에서는 <b>데이터 증강, 질문 제안, 중복 문장 탐지</b> 등에 응용됩니다.<br />
<br>
</div>

<br><br><br>

## ✓ 활용 장비 및 환경
- GPU : NVIDIA GeForce GTX 1650
- OS : Ubuntu 20.04 LTS

<br><br>

## ✓ 모델 구조

<img src="https://user-images.githubusercontent.com/37149278/230636506-2a06de2a-8d1e-4f09-9b02-9cb32964aa90.png" width="400">

- 두 개의 sentence를 [SEP] special token으로 이어 붙인 후 얻은 input_ids를 모델의 input으로 사용합니다.
- [CLS] token의 output hidden_state를 이용해 두 문장 간 유사도를 계산합니다. 

<br><br>

## ✓ 서비스 아키텍처

- 데이터 & 모델 학습 파이프라인

<img src="https://user-images.githubusercontent.com/37149278/230636962-8c2645f1-06ff-4c12-ad68-8be6de4027e2.png" width="800">

<br>

- inference

<img width="800" src="https://user-images.githubusercontent.com/37149278/230637332-aba29832-6f66-4f0f-8787-f6f0eae1a6b6.png">


<br><br>

## ✓ 사용 기술 스택

<img src="https://user-images.githubusercontent.com/37149278/230637496-2c17c358-f10c-46c3-b8a2-140ecf3f00f7.png" width="550">

<br><br>

자세한 정보 및 인사이트는 <a href="https://blog.naver.com/wooy0ng">wooy0ng의 기술 블로그</a>를 참고해주세요! 

<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fwooy0ng%2Fhit-counter&count_bg=%23ADC83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
