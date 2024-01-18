# GraphQL範例
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Getting Started
**這是一個簡單實現GraphQL的範例。下面是如何安裝和使用這個工具的步驟。**

### Prerequisites
* python3.11
* pip

### Installing
**1.clone repository到local。**
```shell
git clone https://github.com/zzhewei/graphql.git
```

**2.創建虛擬環境並安裝相關套件**
```shell
python -m venv .venv
pip install -r requirements.txt
```

**3.初始化資料庫**
```shell
python -m flask init
```

**4. 修改config.py裡的資料庫參數** 


### Usage
**1.命令列輸入:**
```shell
python -m flask run --host=0.0.0.0
```

**2.url輸入:**
http://127.0.0.1:5000/graphql


**3.簡單範例測試:**
```shell
# 根據ID搜尋user並關聯出使用的role
query {
  users(uid:2){
    username,
    passwordHash,
		role{
      name
    }
  }
}

# 更新user
mutation {
  UpdateUser(userData:{uid:1,roleId:1, username:"x",passwordHash:"zz"}) {
    user{
      id,
      username
    }
  }
}

# 根據ID刪除user並秀出msg
mutation {
  DelUser(uid:1) {
    msg
  }
}

# 根據ID搜尋role並關聯出使用此role的users
query {
  roles(id:2){
    name,
    permissions,
		users{
      edges{
        node{
          username
        }
      }
    }
  }
}

# 用 fragment 實現複用
query {
  u1: users(uid:1){
    ...userData
  },
  u2: users(uid:2) {
    ...userData
  }
}

fragment userData on User {
    username,
		role{
      name
    }
}
```


### And coding style tests
**想分析測試專案程式碼，可另外使用pylint進行分析**

**首先**
```shell
pip install pylint
```

**之後針對要分析的py檔執行:**
```shell
python -m pylint main.py
```
**即可觀看測試結果**


# 常用指令
## 自動生成requirements.txt
```shell
pipreqs ./ --encoding=utf8 --force 
```

## Authors

* **ZheWei** - *Initial work* - [ZheWei](https://github.com/zzhewei)
