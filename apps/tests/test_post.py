import pytest
from apps.models import Post
from django.urls import reverse


@pytest.mark.django_db(transaction=True)
def test_create_post(db, client):
    '''
    post 생성 테스트 - 성공
    '''
    url = reverse("apps:post_new")
    data = {"title": f"첫 번째", "text": "하나 둘 셋"}
    response = client.post(url, data)

    post_cnt = Post.objects.all().count()

    assert response.status_code == 302
    assert post_cnt == 1


@pytest.mark.django_db(transaction=True)
def test_get_post_list(db, client, post_1_obj):
    '''
    post 목록 조회 테스트 - 성공
    '''
    url = reverse('apps:post')
    response = client.get(url)
    assert response.status_code == 200



@pytest.mark.django_db(transaction=True)
def test_get_post_detail(db, client, post_1_obj):
    '''
    게시글 내용 조회 테스트 - 성공
    '''
    post = Post.objects.first()
    url = reverse('apps:post_detail', kwargs={'pk' : post.pk})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.parametrize(
    "title, text, expected",
    [
        ("테스트1", "하나 둘 셋", 0),
        ("테스트2", "하나 둘 셋 넷 다섯", 1),
        ("테스트3", "하나 둘 셋 넷 다섯 여섯", 1),
        ("테스트4", "하나 둘 넷", 0),
    ],
)
@pytest.mark.django_db(transaction=True)
def test_create_relation_post (client, post_11_dumps, title, text, expected):
    '''
    relation_post 저장 테스트 - 성공
    '''
    url = reverse('apps:post_new')
    data = {"title": title, "text": text}
    response = client.post(url, data)

    post = Post.objects.last()
    assert response.status_code == 302
    assert post.relation_posts.count() == expected

