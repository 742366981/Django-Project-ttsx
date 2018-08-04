function changeAddressStatus(id) {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        type:'POST',
        url:'/contents/changeAddressStatus/',
        data:{'id':id},
        dataType:'json',
        headers:{'X-CSRFToken': csrf},
        success:function (data) {

        }
    });
}

function getPrice() {
            $.get('/contents/getPrice/',function (data) {
                 $('.total_goods_count b').add($('.total_pay b')).text(data.prices);
                 $('.total_goods_count em').text(data.counts)
            });
        }
getPrice();

function submitOrder() {
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        type:'POST',
        url:'/contents/submitOrder/',
        dataType:'json',
        headers:{'X-CSRFToken':csrf},
        success:function (data) {
            if(data.code=='200'){
                location.href='/contents/userCenterOrder/';
            }
        }
    });
}

