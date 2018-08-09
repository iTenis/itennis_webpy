var countdown = 60;
var sending = false;

$(function () {
    // console.log($.cookie('validateCodeCountdown'));
    countdown = $.cookie('validateCodeCountdown');
    if (countdown > 0) {
        sending = true;
        var obj = $("#btn");
        obj.attr("disabled", true);
        obj.val("重新发送(" + countdown + ")");
        settime(obj);
    }

    $(window).on('beforeunload unload', function () {
        if (sending) {
            // console.log(countdown);
            $.cookie('validateCodeCountdown', countdown);
        }
        if (!sending) {
            // console.log(countdown);
            $.cookie('validateCodeCountdown', 0);
        }
    });
});

function send() {
    if ($('#femail').val()) {
        sending = true;
        var obj = $("#btn");
        settime(obj);
        $.get('/apc/send_mail', {'maillist': $('#femail').val()}, function (data) {
            data = JSON.parse(data);
            if (data["status_code"] == 20000) {
                sending = true;
                var obj = $("#btn");
                settime(obj);
            } else
                alert(get_status_code_desc(data["status_code"]));
        });

    } else {
        alert('请填写正确的邮箱地址!');
    }
}

function settime(obj) { //发送验证码倒计时
    console.log(countdown);
    if (countdown == 0) {
        obj.attr('disabled', false);
        obj.val("发送验证码");
        countdown = 60;
        $.cookie('countdown', 60);
        sending = false;
        return;
    } else {
        obj.attr('disabled', true);
        obj.val("重新发送(" + countdown + ")");
        countdown--;
    }
    setTimeout(function () {
        settime(obj);
    }, 1000)
}
