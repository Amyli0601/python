## 一、requests模块发送请求

- 发送get请求
    - 方法：requests.get()

- 发送post请求
    - 方法：requests.post()


## 二、请求需要登录才能访问的接口
- http请求是无状态的，不会记录上次的请求数据，
- 使用requests发送请求，不会记录上次请求的cookie信息，需要使用session对象来发送请求


## 三、session对象发送请求
- session对象发请求相对于requests的不同点：
- session对象可以自动传递cookies信息（下一次请求会自动携带上次请求的cookies）


## 四、对requests模块进行二度封装
###1、 封装一个能记住cookie信息的请求类：HttpSession

###2、 封装一个不需要记住cookie信息的请求类：HttpRequest


- 为什么要封装？
    - 为了使用的时候更方便，提高代码的重用率

- 封装的需求？
    - 逻辑代码进行封装成方法，关键的数据参数化，

- 那些数据需要参数化？

     -请求地址、请求方法、请求参数








