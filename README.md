# MyCoin_Backend

> 我当时居然没有写API文档！摔

## 注册
|URL|Header|Method|
| --- | -- | -- |
|/api/signup/| None| POST| 

**URL Params: None** 

**POST Data:**

```
{
  "password" : string,
  "username" : string
}
```
**RETURN Data**
```
{
    "create": int
}
```

**Status Code :**
```
200 // 成功 
401 // 用户名占用
```

*** 

## 登录
|URL|Header|Method|
| --- | -- | -- |
|/api/signin/| None| POST| 

**URL Params: None** 

**POST Data:**

```
{
  "password" : string,
  "username" : string, 
  "month" : int,
  "day" : int
}
```
**RETURN Data：**
```
{
    "token": string
}
```

**Status Code :**
```
200 // 成功 
401 // 密码错误
403 // 用户不存在
```

*** 


## 改头像
|URL|Header|Method|
| --- | -- | -- |
|/api/profile/|token:string | PUT| 

**URL Params: None** 

**POST Data:**

```
{  
  "avatar" : string 
}
```
**RETURN Data:**
```
{
    "avatar" : string
}
```

**Status Code :**
```
200 // 成功 
```

*** 



