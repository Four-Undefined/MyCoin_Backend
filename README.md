# MyCoin_Backend


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

## 查重并发邮件
|URL|Header|Method|
| --- | -- | -- |
|/api/signup/unique/ | None| POST| 

**URL Params: None** 

**POST Data:**

```
{
  "email" : string,
  "username" : string
}
```
**RETURN Data**
```
{
    "msg": string
}
```

**Status Code :**
```
200 // 成功，并发送邮件  
403 // 用户名占用或邮箱占用
```

*** 

## 验证码，注册
|URL|Header|Method|
| --- | -- | -- |
|/api/signup/captcha/ | None| POST| 

**URL Params: None** 

**POST Data:**

```
{
  "email" : string,
  "username" : string,
  "captcha" : string,
  "password : string
}
```
**RETURN Data**
```
{
    "msg": string
}
```

**Status Code :**
```
200 // 注册成功 
401 // 验证吗错误
```

*** 

## 校园卡消费记录
|URL|Header|Method|
| --- | -- | -- |
|/api/card/| None| GET| 

**URL Params:** 

```
    "time" : string,
    "sid" : string,
```

**POST Data: None**

**RETURN Data**
```
{
    "response": {
        "list": [
            {
                "data": [
                    {
                        "date": "昨天",
                        "smtDealDateTimeTxt": "2018-07-05 11:49:09",
                        "smtDealName": "消费",
                        "smtInMoney": "41.06",
                        "smtOrgName": "卤肉饭",
                        "smtOutMoney": "30.06",
                        "smtTransMoney": "11.0",
                        "time": "11:49"
                    }
                ],
                "title": "2018-07"
            }
        ],
        "msg": "",
        "result": true
    }
}
```

**Status Code :**
```
200 // 成功 
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


## 查姓名
|URL|Header|Method|
| --- | -- | -- |
|/api/show_profile/|token:string | GET| 

**URL Params: None** 

**POST Data: None**

**RETURN Data:**
```
{
    "username" : string
}
```

**Status Code :**
```
200 // 成功 
```

*** 


## 添加预算
|URL|Header|Method|
| --- | -- | -- |
|/api/budget/|token:string | POST | 

**URL Params: None** 

**POST Data:**
```
{
  "budget" : int, 
  "month" : int
}
```

**RETURN Data:**
```
{
      "budget": {
        "budget": 1200,
        "month": 4,
        "user_id": 15
    }
}
```

**Status Code :**
```
200 // 成功 
```

*** 

## 查看预算
|URL|Header|Method|
| --- | -- | -- |
|/api/view_budget/|token:string | GET | 

**URL Params: None** 

**POST Data:**
```
{
  "month" : int
}
```

**RETURN Data:**
```
{
      "budget": {
        "budget": 1200,
        "month": 4,
        "user_id": 15
    }
}
```

**Status Code :**
```
200 // 成功 
```
*** 


## 添加账单
|URL|Header|Method|
| --- | -- | -- |
|/api/add_accont/|token:string | POST | 

**URL Params:None** 

**POST Data:**
```
{
       
    "trip" : 100,
    "edu" : 200,
    "diet" : 300,
    "normal" : 400, 
    "clothes" : 500,
    "enter" : 10,
    "month" : 4, 
    "day" : 21 
}
```

**RETURN Data:**
```
{
    "expend": {
        "date": "4月21日",
        "id": 44,
        "sum": 1510
    }
}
```

**Status Code :**
```
200 // 成功 
```
*** 




## 查看一周
|URL|Header|Method|
| --- | -- | -- |
|/api/get_seven/|token:string | GET | 

**URL Params:None** 

**POST Data: None**

**RETURN Data:**
```
{
    "TotalExpend": 1510,
    "maxDay": {
        "date": "4月21日",
        "expend": 1510,
        "id": 44
    },
    "result": [
        {
            "class": "教育",
            "expend": 200
        },
        {
            "class": "一般",
            "expend": 400
        },
        {
            "class": "饮食",
            "expend": 300
        },
        {
            "class": "出行",
            "expend": 100
        },
        {
            "class": "娱乐",
            "expend": 10
        },
        {
            "class": "服饰",
            "expend": 500
        }
    ]
```

**Status Code :**
```
200 // 成功 
```
*** 


## 查看一个月
|URL|Header|Method|
| --- | -- | -- |
|/api/get_month/<month:int>/|token:string | GET | 

**URL Params:None** 

**POST Data: None**

**RETURN Data:**
```
{
    "MaxClass": "服饰",
    "maxExpend": 500,
    "result": [
        {
            "class": "教育",
            "expend": 200
        },
        {
            "class": "一般",
            "expend": 400
        },
        {
            "class": "饮食",
            "expend": 300
        },
        {
            "class": "出行",
            "expend": 100
        },
        {
            "class": "娱乐",
            "expend": 10
        },
        {
            "class": "服饰",
            "expend": 500
        },
        {
            "class": "sumup",
            "expend": 1510
        }
    ]
```

**Status Code :**
```
200 // 成功 
```
*** 

## 查看前一天
|URL|Header|Method|
| --- | -- | -- |
|/api/get_some/|token:string | GET | 

**URL Params:None** 

**POST Data: None**

**RETURN Data:**
```
{
    "result": [
        {
            "class": "教育",
            "expend": 200
        },
        {
            "class": "一般",
            "expend": 400
        },
        {
            "class": "饮食",
            "expend": 300
        },
        {
            "class": "出行",
            "expend": 100
        },
        {
            "class": "娱乐",
            "expend": 10
        },
        {
            "class": "服饰",
            "expend": 500
        },
        {
            "class": "sumup",
            "expend": 1510
        }
    ]
}
```

**Status Code :**
```
200 // 成功 
```
*** 


## 查看一个月的总和
|URL|Header|Method|
| --- | -- | -- |
|/api/get_one/<month:int>/|token:string | GET| 

**URL Params:None** 

**POST Data: None**

**RETURN Data:**
```
{
    "sum" : int 
}
```

**Status Code :**
```
200 // 成功 
```
*** 


## 查看最近2天
|URL|Header|Method|
| --- | -- | -- |
|/api/get_two/|token:string | GET | 

**URL Params:None** 

**POST Data: None**

**RETURN Data:**
```
{
    "expend": [
        {
            "一般": 44,
            "出行": 200,
            "娱乐": 19,
            "总和": 774,
            "教育": 200,
            "日期": "7月5日",
            "服饰": 11,
            "饮食": 300
        },
        {
            "一般": 400,
            "出行": 200,
            "娱乐": 19,
            "总和": 1130,
            "教育": 200,
            "日期": "7月4日",
            "服饰": 11,
            "饮食": 300
        }
    ]
}
```

**Status Code :**
```
200 // 成功 
```
*** 
