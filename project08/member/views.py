from django.shortcuts import render,redirect
from member.models import Member

# 로그인페이지 - session : 서버에 저장, cookie : 로컬컴퓨터에 저장
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print(f'로그인정보 : {id},{pw}')
        try:
            qs = Member.objects.get(id=id,pw=pw)   # id=='aaa' && pw=='1111' / 없으면:None
            request.session['session_id'] = qs.id   # 세션저장
            request.session['session_nickname'] = qs.nickname
            print('로그인 완료')
            context = {'temp':1}
            return render(request, 'login.html', context)
        except Member.DoesNotExist:
            print('아이디 or 비번 불일치 삐-삐')
            context = {'temp':0}
            return render(request, 'login.html', context)

# 로그아웃페이지
def logout(request):
    request.session.clear() # 세션을 모두삭제
    context = {'temp':2}
    return render(request, 'login.html', context)