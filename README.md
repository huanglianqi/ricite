
# ricite

>管理平台搭建记录：结合Vuejs和Django，并且通过REST API调用其他网站应用的数据
也记录负责的工具使用方法

### PATCH METHOD DOES NOT WORK IN DJANGO

Need to REwrite the view.py and serializers.py for this.

### Git

在github建好repo之后，上传git将本地文件

```bash
git add ...
git commit -m "some comment"
git push
```
将github上的repo下载到本地

```bash
git add ...
git commit -m "some comment"
git pull
```

### Fontend init

选择nvm作为node的版本管理器：
[nvm-sh/nvm](https://github.com/nvm-sh/nvm/blob/master/README.md#installing-and-updating)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

node选用LTS（稳定版本）

```bash
nvm install --lts
```

安装Vuejs

```bash
npm install -g vue-cli
```

使用Webpack template创建项目：[vuejs-templates/webpack](https://github.com/vuejs-templates)

```bash
vue init webpack frontend
cd frontend
npm install
```

### Backend init

安装python3, pip（python3包管理器），venv（虚拟环境）

```bash
sudo apt-get install python3 python3-pip python3-venv
```

安装Django，创建项目（project）和应用（app）

```bash
source venv/bin/activate
pip3 install django
django-admin startproject backend
cd backend/
python3 manage.py startapp users
```

### Representational state transfer (REST)

搭建API以供前端抓取后端数据：[Django-rest-framework](https://www.django-rest-framework.org/)

```bash
pip3 install djangorestframework
touch backend/users/serializers.py
```

```python3
# backend/backend/setting.py
# ...
INSTALL_APPS = [
    # ...
    'rest_framework',
    # ...
]

# backend/users/serializers.py
from django.contrib.auth.forms import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# backend/users/views.py
from django.contrib.auth.forms import User

from .serializers import UserSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# backend/backend/urls.py
# ...

from django.urls import include

from rest_framework import routers

from users.views import UserViewSet

router = routers.DefaultRouter()

router.register(
    'users',
    UserViewSet
)

urlpatterns = [
    # ...
    path('api/', include(router.urls)),
    # ...
]

```

### Cross-Origin Resource Sharing (CORS)

由于前后端在本地运行时是处于不同的端口的，需要部署[跨域共享](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)，使用[Django-cors-headers](https://pypi.org/project/django-cors-headers/)。

```bash
pip3 install django-cors-headers
```

```python3
# backend/backend/settings.py
# ...

INSTALL_APPS = [
    # ...
    'corsheaders',
]

# ...

MIDDLEWARE = [
    # ...
    # 位置有要求， 具体见官方文档
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]

# ...

# product时要改为False，并加上白名单
CORS_ORIGIN_ALLOW_ALL = Ture

# ...

```

### JWT

安全性考虑，使用JWT进行验证，详见[REST framework JWT Auth](https://jpadilla.github.io/django-rest-framework-jwt/)

```bash
pip3 install djangorestframework-jwt
```

```python3
# backend/backend/settings.py
# ...

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# ...

# backend/backend/urls.py
# ...

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # ...
    path('api/token_auth/', obtain_jwt_token),
    #...
]

```

### Axios Vuex

前端调用时使用[axios](https://github.com/axios/axios)
使用[Vuex](https://vuex.vuejs.org/)进行配置

```bash
mkdir fontend/src/store
touch fontend/src/store/index.js
```

```javascript

```

### 服务器部署与SSL证书
域名和服务器选购
apache和wsgi_mod
certbot
