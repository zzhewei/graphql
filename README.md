# GraphQL範例


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
  users(id:2){
    username,
    passwordHash,
		role{
      name
    }
  }
}

# 更新user
mutation {
  UpdateUser(userData:{id:1,roleId:1, username:"x",passwordHash:"zz"}) {
    user{
      id,
      username
    }
  }
}

# 根據ID刪除user並秀出msg
mutation {
  DelUser(id:1) {
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


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **ZheWei** - *Initial work* - [ZheWei](https://github.com/zzhewei)
