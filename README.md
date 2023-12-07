![python](https://img.shields.io/badge/python-3.11-blue)
![django](https://img.shields.io/badge/django-4.2.7-orange)
# 🚀 백엔드 개발 과제
**게시판 만들기**
## 🔖 **사용 방법**
### 1️⃣ 가상환경 생성 & 패키지 설치
#### **Step 1: 가상환경 생성**
```python
python -m venv <가상환경이름>
```
- ex) `python -m venv venv`
#### **Step 2: 가상환경 실행**
```
# macOS / Linux
source <가상환경이름>/bin/activate

# Windows
<가상환경이름>\Scripts\activate
```
#### **Step 3: 가상환경 실행 후 requirements.txt 설치**
```
pip install -r requirements.txt
```
### 2️⃣ migrate하기

### 3️⃣ urls 설명
1. /post/
    - 게시글 목록
2. /post/new/
   - 게시글 생성
3. /post/<int:pk>/
   - 게시글내용 보기(연관 게시글 포함)
### 4️⃣ 테스트
#### **Step 1: pytest 실행**
```python
pytest
```
- print 같이 출력하기
    ```python
  pytest -s
  ```
- 특정 파일만 실행
    ```python
  pytest apps/tests/test_post.py
  ```
- 특정 함수만 실행
    ```python
  pytest apps/tests/test_post.py::test_create_post
  ```
