$(function () {
    $("title").html("iTennis | 用户信息");
    path = window.location.pathname;
    if (path.split("/")[3] == 1) {
        $("#login_form_data").attr('style', 'display: none;');
        $("#register_form_data").attr('style', 'display: block;');
        $("#forget_form_data").attr('style', 'display: none;');
    } else if (path.split("/")[3] == 3) {
        $("#login_form_data").attr('style', 'display: none;');
        $("#register_form_data").attr('style', 'display: none;');
        $("#forget_form_data").attr('style', 'display: block;');
    } else {
        $("#login_form_data").attr('style', 'display: block;');
        $("#register_form_data").attr('style', 'display: none;');
        $("#forget_form_data").attr('style', 'display: none;');
    }

    $.get("/apc/login_t/", function (data) {
        // alert(data)
        var data = JSON.parse(data);
        if (data["status_code"] == 20000) {
            window.location.href = '/'
        }
        else
            console.log(get_status_code_desc(data["status_code"]))
    });
    $("#login_submit").click(function () {
        $.post({
            url: '/apc/login_t/',
            headers: {"X-CSRFToken": $.cookie('csrftoken')},
            data: $("#login_form_data").serialize(),
            contentType: 'application/x-www-form-urlencoded',
            success: function (data) {
                var data = JSON.parse(data);
                $("title").html(data["title"]);
                if (data["status_code"] == 20000) {
                    if (data['reurl'] != '')
                        window.location.href = data['reurl'];
                    else
                        window.location.href = '/';
                } else
                    alert(get_status_code_desc(data["status_code"]));

            }
        });
    });
    $("#register_submit").click(function () {
        $.post({
            url: '/apc/register_t/',
            headers: {"X-CSRFToken": $.cookie('csrftoken')},
            data: $("#register_form_data").serialize(),
            contentType: 'application/x-www-form-urlencoded',
            success: function (data) {
                var data = JSON.parse(data);
                $("title").html(data["title"]);
                if (data["status_code"] == 20000)
                    window.location.href = '/apc/login/2';
                else
                    alert(get_status_code_desc(data["status_code"]));
                //
            }
        });
    });

    $("#forget_submit").click(function () {
        $.post({
            url: '/apc/forget_t/',
            headers: {"X-CSRFToken": $.cookie('csrftoken')},
            data: $("#forget_form_data").serialize(),
            contentType: 'application/x-www-form-urlencoded',
            success: function (data) {
                var data = JSON.parse(data);
                $("title").html(data["title"]);
                if (data["status_code"] == 20000)
                    window.location.href = '/apc/login/2/';
                else
                    alert(get_status_code_desc(data["status_code"]));
            }
        });
    });

    //#给验证码刷新
    $(".vialdcode_img").click(function () {
        $(this)[0].src += "?";
        $(this).attr("src", $(this).attr("src") + '?');
    });


    $('#rusername').attr("readonly", "readonly");
    $('#remail').keyup(function () {
        remail = $('#remail').val();
        $('#rusername').val(remail);
        $.get('/apc/checkuser/' + remail, function (data) {
            var data = JSON.parse(data);
            if (data["status_code"] == 20000) {
                $("#remail").css({"border-color": "green"});
            } else {
                $("#remail").css({"border-color": "red"});
            }
        })
    });
    $("body").keydown(function () {
        if (event.keyCode == "13") {//keyCode=13是回车键
            $('#login_submit').focus();
            if ($('#login_form_data').css("display") == 'block') {
                obj = $('#login_submit');
            } else if ($('#register_form_data').css("display") == 'block')
                obj = $('#register_submit');
            else
                obj = $('#forget_submit');
            obj.click();
        }
    });

});