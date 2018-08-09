function get_status_code_desc(code) {
    var mesg;
    switch (code) {
        case ("20000"):
            mesg = '操作成功';
            break;
        case ("20001"):
            mesg = '昵称为空';
            break;
        case ("20002"):
            mesg = '邮箱为空';
            break;
        case ("20003"):
            mesg = '用户名为空';
            break;
        case ("20004"):
            mesg = '密码为空';
            break;
        case ("20005"):
            mesg = '确认密码为空';
            break;
        case ("20006"):
            mesg = '密码不一致';
            break;
        case ("20007"):
            mesg = '用户名或者密码错误';
            break;
        case ("20008"):
            mesg = 'Cookie不存在';
            break;
        case ("20009"):
            mesg = '验证码不一致';
            break;
        case ("20010"):
            mesg = '用户名已经存在';
            break;
        case ("30001"):
            mesg = '数据库操作失败';
            break;
        case ("40001"):
            mesg = 'GET操作失败';
            break;
        case ("40002"):
            mesg = 'POST操作失败';
            break;
        case ("40003"):
            mesg = '邮件服务器错误或者邮件地址错误';
            break;
        default:
            mesg = '未知错误!'
    }
    return mesg;
}